import * as echarts from 'echarts';
import { ECharts, EChartsOption } from 'echarts';

// Chart must have initial height to be visible
export function ensureChartDomHasHeight(chartDom: HTMLDivElement | HTMLCanvasElement) {
  const computedHeight = window.getComputedStyle(chartDom, null).getPropertyValue('height');
  const inlineHeight = chartDom.style.height;
  if (!computedHeight || computedHeight === '0px' || !inlineHeight || inlineHeight === '0px') {
    chartDom.style.height = '350px';
  }
}

export function initChart(chartDom: HTMLDivElement | HTMLCanvasElement) {
  ensureChartDomHasHeight(chartDom);
  const chart = echarts.init(chartDom);
  resizeChartOnWindowResize(chartDom, chart);
  return chart;
}

// ensure chart resizes -- see https://github.com/apache/echarts/issues/17428#issuecomment-1723693844
// if there are issues in the future, check ngx-echarts: https://github.com/xieziyu/ngx-echarts/blob/master/projects/ngx-echarts/src/lib/ngx-echarts.directive.ts
export function resizeChartOnWindowResize(
  chartDom: HTMLDivElement | HTMLCanvasElement,
  chart: ECharts,
) {
  const resizeObserver = new ResizeObserver(() => {
    chart.resize();
  });
  resizeObserver.observe(chartDom);
}

export function setNoDataOption(chart: ECharts) {
  const noDataOptions: EChartsOption = {
    title: {
      text: 'No data is currently available.',
      left: 'center',
      top: 'middle',
      textStyle: {
        color: 'rgb(174, 181, 188)',
        fontStyle: 'italic',
        fontWeight: 400,
        fontSize: 18,
      },
    },
    aria: {
      enabled: true,
      label: {
        description: 'No data is currently available.',
      },
    },
  };

  // notMerge must be set to true to override any existing options set on the chart
  chart.setOption(noDataOptions, true);
}

/**
 * Measures the rendered width of text using canvas context.
 *
 * @param text - The text to measure
 * @param font - CSS font specification (e.g., "16px Arial", "bold 14px sans-serif")
 * @returns The width in pixels, or a fallback estimate if canvas is not available
 */
export function getTextWidth(text: string, font: string): number {
  const canvas = document.createElement('canvas');
  const context = canvas.getContext('2d');

  if (!context) {
    return text.length * 8;
  }

  context.font = font;
  return context.measureText(text).width;
}
