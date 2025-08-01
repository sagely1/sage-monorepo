package org.sagebionetworks.openchallenges.challenge.service.client;

import org.sagebionetworks.openchallenges.challenge.service.model.dto.auth.ValidateApiKeyRequestDto;
import org.sagebionetworks.openchallenges.challenge.service.model.dto.auth.ValidateApiKeyResponseDto;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

/**
 * Feign client for communicating with the OpenChallenges Auth Service
 */
@FeignClient(
  name = "auth-service",
  url = "${openchallenges-challenge-service.auth-service.base-url:http://openchallenges-auth-service:8087}",
  path = "/v1"
)
public interface AuthServiceClient {
  /**
   * Validates an API key with the auth service
   *
   * @param request the validation request containing the API key
   * @return the validation response with user details and permissions
   */
  @PostMapping("/auth/validate")
  ValidateApiKeyResponseDto validateApiKey(@RequestBody ValidateApiKeyRequestDto request);
}
