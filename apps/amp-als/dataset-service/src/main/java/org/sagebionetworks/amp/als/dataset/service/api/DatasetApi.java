/**
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech) (6.2.1).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
package org.sagebionetworks.amp.als.dataset.service.api;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.Parameters;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import io.swagger.v3.oas.annotations.tags.Tag;
import java.util.List;
import java.util.Map;
import javax.annotation.Generated;
import javax.validation.Valid;
import javax.validation.constraints.*;
import org.sagebionetworks.amp.als.dataset.service.model.dto.BasicErrorDto;
import org.sagebionetworks.amp.als.dataset.service.model.dto.DatasetDto;
import org.sagebionetworks.amp.als.dataset.service.model.dto.DatasetJsonLdDto;
import org.sagebionetworks.amp.als.dataset.service.model.dto.DatasetSearchQueryDto;
import org.sagebionetworks.amp.als.dataset.service.model.dto.DatasetsPageDto;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@Generated(value = "org.openapitools.codegen.languages.SpringCodegen")
@Validated
@Tag(name = "Dataset", description = "Operations about datasets.")
public interface DatasetApi {
  default DatasetApiDelegate getDelegate() {
    return new DatasetApiDelegate() {};
  }

  /**
   * GET /datasets/{datasetId} : Get a dataset
   * Returns the dataset specified
   *
   * @param datasetId The unique identifier of the dataset. (required)
   * @return A dataset (status code 200)
   *         or The specified resource was not found (status code 404)
   *         or The request cannot be fulfilled due to an unexpected server error (status code 500)
   */
  @Operation(
    operationId = "getDataset",
    summary = "Get a dataset",
    tags = { "Dataset" },
    responses = {
      @ApiResponse(
        responseCode = "200",
        description = "A dataset",
        content = {
          @Content(
            mediaType = "application/json",
            schema = @Schema(implementation = DatasetDto.class)
          ),
          @Content(
            mediaType = "application/ld+json",
            schema = @Schema(implementation = DatasetDto.class)
          ),
          @Content(
            mediaType = "application/problem+json",
            schema = @Schema(implementation = DatasetDto.class)
          ),
        }
      ),
      @ApiResponse(
        responseCode = "404",
        description = "The specified resource was not found",
        content = {
          @Content(
            mediaType = "application/json",
            schema = @Schema(implementation = BasicErrorDto.class)
          ),
          @Content(
            mediaType = "application/ld+json",
            schema = @Schema(implementation = BasicErrorDto.class)
          ),
          @Content(
            mediaType = "application/problem+json",
            schema = @Schema(implementation = BasicErrorDto.class)
          ),
        }
      ),
      @ApiResponse(
        responseCode = "500",
        description = "The request cannot be fulfilled due to an unexpected server error",
        content = {
          @Content(
            mediaType = "application/json",
            schema = @Schema(implementation = BasicErrorDto.class)
          ),
          @Content(
            mediaType = "application/ld+json",
            schema = @Schema(implementation = BasicErrorDto.class)
          ),
          @Content(
            mediaType = "application/problem+json",
            schema = @Schema(implementation = BasicErrorDto.class)
          ),
        }
      ),
    }
  )
  @RequestMapping(
    method = RequestMethod.GET,
    value = "/datasets/{datasetId}",
    produces = { "application/json", "application/ld+json", "application/problem+json" }
  )
  default ResponseEntity<DatasetDto> getDataset(
    @Parameter(
      name = "datasetId",
      description = "The unique identifier of the dataset.",
      required = true
    ) @PathVariable("datasetId") Long datasetId
  ) {
    return getDelegate().getDataset(datasetId);
  }

  /**
   * GET /datasets : List datasets
   * List datasets
   *
   * @param datasetSearchQuery The search query used to find datasets. (optional)
   * @return Success (status code 200)
   *         or Invalid request (status code 400)
   *         or The request cannot be fulfilled due to an unexpected server error (status code 500)
   */
  @Operation(
    operationId = "listDatasets",
    summary = "List datasets",
    tags = { "Dataset" },
    responses = {
      @ApiResponse(
        responseCode = "200",
        description = "Success",
        content = {
          @Content(
            mediaType = "application/json",
            schema = @Schema(implementation = DatasetsPageDto.class)
          ),
          @Content(
            mediaType = "application/problem+json",
            schema = @Schema(implementation = DatasetsPageDto.class)
          ),
        }
      ),
      @ApiResponse(
        responseCode = "400",
        description = "Invalid request",
        content = {
          @Content(
            mediaType = "application/json",
            schema = @Schema(implementation = BasicErrorDto.class)
          ),
          @Content(
            mediaType = "application/problem+json",
            schema = @Schema(implementation = BasicErrorDto.class)
          ),
        }
      ),
      @ApiResponse(
        responseCode = "500",
        description = "The request cannot be fulfilled due to an unexpected server error",
        content = {
          @Content(
            mediaType = "application/json",
            schema = @Schema(implementation = BasicErrorDto.class)
          ),
          @Content(
            mediaType = "application/problem+json",
            schema = @Schema(implementation = BasicErrorDto.class)
          ),
        }
      ),
    }
  )
  @RequestMapping(
    method = RequestMethod.GET,
    value = "/datasets",
    produces = { "application/json", "application/problem+json" }
  )
  default ResponseEntity<DatasetsPageDto> listDatasets(
    @Parameter(
      name = "datasetSearchQuery",
      description = "The search query used to find datasets."
    ) @Valid DatasetSearchQueryDto datasetSearchQuery
  ) {
    return getDelegate().listDatasets(datasetSearchQuery);
  }
}
