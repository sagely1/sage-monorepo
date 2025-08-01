package org.sagebionetworks.openchallenges.api.client.api;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Objects;
import java.util.stream.Collectors;
import org.sagebionetworks.openchallenges.api.client.ApiClient;
import org.sagebionetworks.openchallenges.api.client.model.BasicError;
import org.sagebionetworks.openchallenges.api.client.model.ChallengesPerYear;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.core.io.FileSystemResource;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestClient.ResponseSpec;
import org.springframework.web.client.RestClientResponseException;

@jakarta.annotation.Generated(
  value = "org.openapitools.codegen.languages.JavaClientCodegen",
  comments = "Generator version: 7.13.0"
)
public class ChallengeAnalyticsApi {

  private ApiClient apiClient;

  public ChallengeAnalyticsApi() {
    this(new ApiClient());
  }

  @Autowired
  public ChallengeAnalyticsApi(ApiClient apiClient) {
    this.apiClient = apiClient;
  }

  public ApiClient getApiClient() {
    return apiClient;
  }

  public void setApiClient(ApiClient apiClient) {
    this.apiClient = apiClient;
  }

  /**
   * Get the number of challenges tracked per year
   * Returns the number of challenges tracked per year
   * <p><b>200</b> - An object
   * <p><b>500</b> - The request cannot be fulfilled due to an unexpected server error
   * @return ChallengesPerYear
   * @throws RestClientResponseException if an error occurs while attempting to invoke the API
   */
  private ResponseSpec getChallengesPerYearRequestCreation() throws RestClientResponseException {
    Object postBody = null;
    // create path and map variables
    final Map<String, Object> pathParams = new HashMap<>();

    final MultiValueMap<String, String> queryParams = new LinkedMultiValueMap<>();
    final HttpHeaders headerParams = new HttpHeaders();
    final MultiValueMap<String, String> cookieParams = new LinkedMultiValueMap<>();
    final MultiValueMap<String, Object> formParams = new LinkedMultiValueMap<>();

    final String[] localVarAccepts = { "application/json", "application/problem+json" };
    final List<MediaType> localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);
    final String[] localVarContentTypes = {};
    final MediaType localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);

    String[] localVarAuthNames = new String[] {};

    ParameterizedTypeReference<ChallengesPerYear> localVarReturnType =
      new ParameterizedTypeReference<>() {};
    return apiClient.invokeAPI(
      "/challenge-analytics/challenges-per-year",
      HttpMethod.GET,
      pathParams,
      queryParams,
      postBody,
      headerParams,
      cookieParams,
      formParams,
      localVarAccept,
      localVarContentType,
      localVarAuthNames,
      localVarReturnType
    );
  }

  /**
   * Get the number of challenges tracked per year
   * Returns the number of challenges tracked per year
   * <p><b>200</b> - An object
   * <p><b>500</b> - The request cannot be fulfilled due to an unexpected server error
   * @return ChallengesPerYear
   * @throws RestClientResponseException if an error occurs while attempting to invoke the API
   */
  public ChallengesPerYear getChallengesPerYear() throws RestClientResponseException {
    ParameterizedTypeReference<ChallengesPerYear> localVarReturnType =
      new ParameterizedTypeReference<>() {};
    return getChallengesPerYearRequestCreation().body(localVarReturnType);
  }

  /**
   * Get the number of challenges tracked per year
   * Returns the number of challenges tracked per year
   * <p><b>200</b> - An object
   * <p><b>500</b> - The request cannot be fulfilled due to an unexpected server error
   * @return ResponseEntity&lt;ChallengesPerYear&gt;
   * @throws RestClientResponseException if an error occurs while attempting to invoke the API
   */
  public ResponseEntity<ChallengesPerYear> getChallengesPerYearWithHttpInfo()
    throws RestClientResponseException {
    ParameterizedTypeReference<ChallengesPerYear> localVarReturnType =
      new ParameterizedTypeReference<>() {};
    return getChallengesPerYearRequestCreation().toEntity(localVarReturnType);
  }

  /**
   * Get the number of challenges tracked per year
   * Returns the number of challenges tracked per year
   * <p><b>200</b> - An object
   * <p><b>500</b> - The request cannot be fulfilled due to an unexpected server error
   * @return ResponseSpec
   * @throws RestClientResponseException if an error occurs while attempting to invoke the API
   */
  public ResponseSpec getChallengesPerYearWithResponseSpec() throws RestClientResponseException {
    return getChallengesPerYearRequestCreation();
  }
}
