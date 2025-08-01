package org.sagebionetworks.openchallenges.auth.service.model.dto;

import java.net.URI;
import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonTypeName;
import com.fasterxml.jackson.annotation.JsonValue;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.UUID;
import org.springframework.lang.Nullable;
import java.time.OffsetDateTime;
import jakarta.validation.Valid;
import jakarta.validation.constraints.*;
import io.swagger.v3.oas.annotations.media.Schema;


import java.util.*;
import jakarta.annotation.Generated;

/**
 * ValidateApiKeyResponseDto
 */

@JsonTypeName("ValidateApiKeyResponse")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", comments = "Generator version: 7.14.0")
public class ValidateApiKeyResponseDto {

  private @Nullable Boolean valid;

  private @Nullable UUID userId;

  private @Nullable String username;

  /**
   * Role of the API key owner (only if valid)
   */
  public enum RoleEnum {
    ADMIN("admin"),
    
    USER("user"),
    
    READONLY("readonly"),
    
    SERVICE("service");

    private final String value;

    RoleEnum(String value) {
      this.value = value;
    }

    @JsonValue
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    @JsonCreator
    public static RoleEnum fromValue(String value) {
      for (RoleEnum b : RoleEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }
  }

  private @Nullable RoleEnum role;

  @Valid
  private List<String> scopes = new ArrayList<>();

  public ValidateApiKeyResponseDto valid(@Nullable Boolean valid) {
    this.valid = valid;
    return this;
  }

  /**
   * Whether the API key is valid
   * @return valid
   */
  
  @Schema(name = "valid", example = "true", description = "Whether the API key is valid", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("valid")
  public @Nullable Boolean getValid() {
    return valid;
  }

  public void setValid(@Nullable Boolean valid) {
    this.valid = valid;
  }

  public ValidateApiKeyResponseDto userId(@Nullable UUID userId) {
    this.userId = userId;
    return this;
  }

  /**
   * ID of the user who owns this API key (only if valid)
   * @return userId
   */
  @Valid 
  @Schema(name = "userId", example = "123e4567-e89b-12d3-a456-426614174000", description = "ID of the user who owns this API key (only if valid)", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("userId")
  public @Nullable UUID getUserId() {
    return userId;
  }

  public void setUserId(@Nullable UUID userId) {
    this.userId = userId;
  }

  public ValidateApiKeyResponseDto username(@Nullable String username) {
    this.username = username;
    return this;
  }

  /**
   * Username of the API key owner (only if valid)
   * @return username
   */
  
  @Schema(name = "username", example = "admin", description = "Username of the API key owner (only if valid)", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("username")
  public @Nullable String getUsername() {
    return username;
  }

  public void setUsername(@Nullable String username) {
    this.username = username;
  }

  public ValidateApiKeyResponseDto role(@Nullable RoleEnum role) {
    this.role = role;
    return this;
  }

  /**
   * Role of the API key owner (only if valid)
   * @return role
   */
  
  @Schema(name = "role", example = "admin", description = "Role of the API key owner (only if valid)", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("role")
  public @Nullable RoleEnum getRole() {
    return role;
  }

  public void setRole(@Nullable RoleEnum role) {
    this.role = role;
  }

  public ValidateApiKeyResponseDto scopes(List<String> scopes) {
    this.scopes = scopes;
    return this;
  }

  public ValidateApiKeyResponseDto addScopesItem(String scopesItem) {
    if (this.scopes == null) {
      this.scopes = new ArrayList<>();
    }
    this.scopes.add(scopesItem);
    return this;
  }

  /**
   * Permissions granted to this API key (only if valid)
   * @return scopes
   */
  
  @Schema(name = "scopes", example = "[\"organizations:read\",\"organizations:write\"]", description = "Permissions granted to this API key (only if valid)", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("scopes")
  public List<String> getScopes() {
    return scopes;
  }

  public void setScopes(List<String> scopes) {
    this.scopes = scopes;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ValidateApiKeyResponseDto validateApiKeyResponse = (ValidateApiKeyResponseDto) o;
    return Objects.equals(this.valid, validateApiKeyResponse.valid) &&
        Objects.equals(this.userId, validateApiKeyResponse.userId) &&
        Objects.equals(this.username, validateApiKeyResponse.username) &&
        Objects.equals(this.role, validateApiKeyResponse.role) &&
        Objects.equals(this.scopes, validateApiKeyResponse.scopes);
  }

  @Override
  public int hashCode() {
    return Objects.hash(valid, userId, username, role, scopes);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ValidateApiKeyResponseDto {\n");
    sb.append("    valid: ").append(toIndentedString(valid)).append("\n");
    sb.append("    userId: ").append(toIndentedString(userId)).append("\n");
    sb.append("    username: ").append(toIndentedString(username)).append("\n");
    sb.append("    role: ").append(toIndentedString(role)).append("\n");
    sb.append("    scopes: ").append(toIndentedString(scopes)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
  
  public static class Builder {

    private ValidateApiKeyResponseDto instance;

    public Builder() {
      this(new ValidateApiKeyResponseDto());
    }

    protected Builder(ValidateApiKeyResponseDto instance) {
      this.instance = instance;
    }

    protected Builder copyOf(ValidateApiKeyResponseDto value) { 
      this.instance.setValid(value.valid);
      this.instance.setUserId(value.userId);
      this.instance.setUsername(value.username);
      this.instance.setRole(value.role);
      this.instance.setScopes(value.scopes);
      return this;
    }

    public ValidateApiKeyResponseDto.Builder valid(Boolean valid) {
      this.instance.valid(valid);
      return this;
    }
    
    public ValidateApiKeyResponseDto.Builder userId(UUID userId) {
      this.instance.userId(userId);
      return this;
    }
    
    public ValidateApiKeyResponseDto.Builder username(String username) {
      this.instance.username(username);
      return this;
    }
    
    public ValidateApiKeyResponseDto.Builder role(RoleEnum role) {
      this.instance.role(role);
      return this;
    }
    
    public ValidateApiKeyResponseDto.Builder scopes(List<String> scopes) {
      this.instance.scopes(scopes);
      return this;
    }
    
    /**
    * returns a built ValidateApiKeyResponseDto instance.
    *
    * The builder is not reusable (NullPointerException)
    */
    public ValidateApiKeyResponseDto build() {
      try {
        return this.instance;
      } finally {
        // ensure that this.instance is not reused
        this.instance = null;
      }
    }

    @Override
    public String toString() {
      return getClass() + "=(" + instance + ")";
    }
  }

  /**
  * Create a builder with no initialized field (except for the default values).
  */
  public static ValidateApiKeyResponseDto.Builder builder() {
    return new ValidateApiKeyResponseDto.Builder();
  }

  /**
  * Create a builder with a shallow copy of this instance.
  */
  public ValidateApiKeyResponseDto.Builder toBuilder() {
    ValidateApiKeyResponseDto.Builder builder = new ValidateApiKeyResponseDto.Builder();
    return builder.copyOf(this);
  }

}

