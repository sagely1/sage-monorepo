#!/usr/bin/env python3
"""
Example script instrumented with OpenTelemetry to send telemetry data to the Sage monorepo
observability stack.

This script demonstrates how to:
1. Configure OpenTelemetry logging, metrics, and traces
2. Configure Pyroscope profiles
3. Instrument this script to send data to the observability stack
"""

import argparse
import logging
import os
import sys
import time
import random
from functools import wraps

# OpenTelemetry imports
from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter

# Pyroscope profiling
try:
    import pyroscope

    has_pyroscope = True
except ImportError:
    print("Pyroscope not installed. Profiling will not be available.")
    has_pyroscope = False

# Constants
SERVICE_NAME = "sandbox-observability-python"
SERVICE_VERSION = "0.1.0"
OTLP_ENDPOINT = "http://observability-otel-collector:8508"  # gRPC endpoint
PYROSCOPE_ENDPOINT = "http://observability-pyroscope:8511"

# Setup the OpenTelemetry resources
resource = Resource.create(
    {
        "service.name": SERVICE_NAME,
        "service.version": SERVICE_VERSION,
    }
)


# Configure Logging with OpenTelemetry
def setup_logging():
    # Create a logger
    logger = logging.getLogger(SERVICE_NAME)
    logger.setLevel(logging.INFO)

    # Configure standard output handler
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Set up the OTLP log exporter
    log_exporter = OTLPLogExporter(
        endpoint=OTLP_ENDPOINT,
        insecure=True,
    )

    # Create logger provider with our resource
    logger_provider = LoggerProvider(resource=resource)

    # Add exporter to logger provider
    logger_provider.add_log_record_processor(BatchLogRecordProcessor(log_exporter))

    # Create and add OTLP handler to logger
    otlp_handler = LoggingHandler(logger_provider=logger_provider)
    logger.addHandler(otlp_handler)

    # Instrument logging with OpenTelemetry
    LoggingInstrumentor().instrument(set_logging_format=True)

    return logger


# Configure Tracing with OpenTelemetry
def setup_tracing():
    # Create a tracer provider
    tracer_provider = TracerProvider(resource=resource)

    # Create an OTLP exporter and add it to the tracer provider
    otlp_exporter = OTLPSpanExporter(
        endpoint=OTLP_ENDPOINT,
        insecure=True,
    )
    span_processor = BatchSpanProcessor(otlp_exporter)
    tracer_provider.add_span_processor(span_processor)

    # Set the tracer provider
    trace.set_tracer_provider(tracer_provider)

    # Get a tracer
    tracer = trace.get_tracer(SERVICE_NAME, SERVICE_VERSION)

    return tracer


# Configure Metrics with OpenTelemetry
def setup_metrics():
    # Create a metric reader
    metric_reader = PeriodicExportingMetricReader(
        OTLPMetricExporter(
            endpoint=OTLP_ENDPOINT,
            insecure=True,
        ),
        export_interval_millis=5000,  # 5 seconds - reduced for more frequent updates
    )

    # Create a meter provider with the shared resource
    meter_provider = MeterProvider(resource=resource, metric_readers=[metric_reader])

    # Set the meter provider globally
    metrics.set_meter_provider(meter_provider)

    # Get a meter
    meter = metrics.get_meter(
        SERVICE_NAME, SERVICE_VERSION
    )  # Create some metrics with more specific names
    request_counter = meter.create_counter(
        name=f"{SERVICE_NAME}.requests",
        description="Number of requests processed",
        unit="1",
    )

    request_duration = meter.create_histogram(
        name=f"{SERVICE_NAME}.request_duration",
        description="Duration of requests",
        unit="ms",
    )

    # Add a metric to track the time the script has been running
    runtime_gauge = meter.create_up_down_counter(
        name=f"{SERVICE_NAME}.runtime_seconds",
        description="How long the script has been running in seconds",
        unit="s",
    )

    # Add an up metric that will always be present and set to 1
    # This helps confirm the metrics pipeline is working
    up_gauge = meter.create_up_down_counter(
        name=f"{SERVICE_NAME}.up",
        description="Indicates the service is running and exporting metrics",
        unit="1",
    )

    # Set the up metric to 1 (service is up) with service attributes
    up_gauge.add(
        1,
        {
            "service.name": SERVICE_NAME,
            "service.version": SERVICE_VERSION,
        },
    )

    return request_counter, request_duration, runtime_gauge


# Configure Profiling with Pyroscope
def setup_profiling():
    if not has_pyroscope:
        return None

    try:
        # Initialize Pyroscope directly with more explicit settings
        pyroscope.configure(
            application_name=SERVICE_NAME,
            server_address=PYROSCOPE_ENDPOINT,
            sample_rate=10,
            tags={
                "service.version": SERVICE_VERSION,
                "environment": "development",
                "language": "python",
            },
            enable_logging=True,
        )
        return True
    except Exception as e:
        print(f"Failed to configure Pyroscope: {e}")
        return None


# Tracing decorator for functions
def trace_function(tracer):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with tracer.start_as_current_span(func.__name__):
                return func(*args, **kwargs)

        return wrapper

    return decorator


# Main function to simulate work
def main():
    # Setup telemetry
    logger = setup_logging()
    tracer = setup_tracing()
    request_counter, request_duration, runtime_gauge = setup_metrics()
    profiling_enabled = setup_profiling()

    # Store meter provider reference for shutdown
    meter_provider = metrics.get_meter_provider()

    # Record start time
    start_time = time.time()

    # Log initialization
    logger.info(f"Starting {SERVICE_NAME} v{SERVICE_VERSION}")
    logger.info(f"Tracing enabled: {tracer is not None}")
    logger.info(
        f"Metrics enabled: {request_counter is not None and request_duration is not None}"
    )
    logger.info(f"Profiling enabled: {profiling_enabled is True}")

    # Parse arguments
    parser = argparse.ArgumentParser(
        description="Script with OpenTelemetry instrumentation"
    )
    parser.add_argument(
        "--iterations", type=int, default=10, help="Number of iterations to run"
    )
    args = parser.parse_args()

    # Simulate work
    @trace_function(tracer)
    # By default, the span is named after the annotated function.
    # To override this, use the annotation below to specify a custom span name.
    # @tracer.start_as_current_span("process_work_item")
    def process_item(item_id):
        logger.info(f"Processing item {item_id}")

        # Add CPU-intensive work to demonstrate profiling
        if item_id % 2 == 0:
            # CPU-intensive operation - recursive Fibonacci calculation
            n = 35  # Large enough to be visible in profiles
            result = calculate_fibonacci(n)
            logger.info(f"Calculated Fibonacci({n}) = {result}")

        # Simulate some work
        sleep_time = random.uniform(0.1, 0.5)
        time.sleep(sleep_time)

        # Record metrics with additional attributes
        attributes = {
            "item_id": str(item_id),
            "service.name": SERVICE_NAME,
            "service.version": SERVICE_VERSION,
        }
        request_counter.add(1, attributes)
        request_duration.record(sleep_time * 1000, attributes)

        # Sometimes generate an error
        if random.random() < 0.2:
            try:
                raise ValueError(f"Simulated error processing item {item_id}")
            except ValueError as e:
                logger.exception(f"Error processing item {item_id}")

        return sleep_time

    # CPU-intensive function that will show up in profiles
    def calculate_fibonacci(n):
        if n <= 1:
            return n
        return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)

    # Main processing loop
    with tracer.start_as_current_span("main_processing"):
        total_time = 0
        for i in range(args.iterations):
            try:
                # Add profiling label for each iteration if profiling is enabled
                profiling_ctx = None
                if has_pyroscope:
                    profiling_ctx = pyroscope.tag_wrapper(
                        {"iteration": str(i), "operation": "process_item"}
                    )
                    profiling_ctx.__enter__()

                processing_time = process_item(i)
                total_time += processing_time

                # Update the runtime gauge with the elapsed time
                elapsed = time.time() - start_time
                runtime_gauge.add(
                    elapsed, {"service.name": SERVICE_NAME, "iteration": str(i)}
                )

                logger.info(f"Completed item {i} in {processing_time:.2f} seconds")

                # Exit the profiling context if it exists
                if profiling_ctx:
                    profiling_ctx.__exit__(None, None, None)

            except Exception as e:
                # Exit profiling context in case of error
                if "profiling_ctx" in locals() and profiling_ctx:
                    profiling_ctx.__exit__(None, None, None)
                logger.exception(f"Unhandled exception in process_item")

        logger.info(f"Processed {args.iterations} items in {total_time:.2f} seconds")

    logger.info(f"Shutting down {SERVICE_NAME}")

    # Force flush metrics before shutdown
    logger.info("Flushing metrics before shutdown...")

    # Force a metrics collection/export cycle
    if hasattr(meter_provider, "force_flush"):
        meter_provider.force_flush()  # type: ignore

    # Give time for metrics to be exported
    logger.info("Waiting for metrics to be exported...")
    time.sleep(6)  # Wait 6 seconds to allow metrics to be exported

    # Close Pyroscope profiler if it was enabled
    if has_pyroscope and "pyroscope" in globals() and hasattr(pyroscope, "stop"):
        logger.info("Stopping Pyroscope profiler...")
        pyroscope.stop()

    logger.info("Shutdown complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
