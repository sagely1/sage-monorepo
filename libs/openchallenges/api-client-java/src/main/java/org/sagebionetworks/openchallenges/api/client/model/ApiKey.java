/*
 * OpenChallenges API
 * Discover, explore, and contribute to open biomedical challenges.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

package org.sagebionetworks.openchallenges.api.client.model;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.annotation.JsonTypeName;
import com.fasterxml.jackson.annotation.JsonTypeName;
import com.fasterxml.jackson.annotation.JsonValue;
import java.time.OffsetDateTime;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.Objects;
import java.util.UUID;
import org.openapitools.jackson.nullable.JsonNullable;
import org.openapitools.jackson.nullable.JsonNullable;

/**
 * ApiKey
 */
@JsonPropertyOrder(
  {
    ApiKey.JSON_PROPERTY_ID,
    ApiKey.JSON_PROPERTY_NAME,
    ApiKey.JSON_PROPERTY_PREFIX,
    ApiKey.JSON_PROPERTY_CREATED_AT,
    ApiKey.JSON_PROPERTY_EXPIRES_AT,
    ApiKey.JSON_PROPERTY_LAST_USED_AT,
  }
)
@jakarta.annotation.Generated(
  value = "org.openapitools.codegen.languages.JavaClientCodegen",
  comments = "Generator version: 7.13.0"
)
public class ApiKey {

  public static final String JSON_PROPERTY_ID = "id";

  @jakarta.annotation.Nullable
  private UUID id;

  public static final String JSON_PROPERTY_NAME = "name";

  @jakarta.annotation.Nullable
  private String name;

  public static final String JSON_PROPERTY_PREFIX = "prefix";

  @jakarta.annotation.Nullable
  private String prefix;

  public static final String JSON_PROPERTY_CREATED_AT = "createdAt";

  @jakarta.annotation.Nullable
  private OffsetDateTime createdAt;

  public static final String JSON_PROPERTY_EXPIRES_AT = "expiresAt";

  @jakarta.annotation.Nullable
  private JsonNullable<OffsetDateTime> expiresAt = JsonNullable.<OffsetDateTime>undefined();

  public static final String JSON_PROPERTY_LAST_USED_AT = "lastUsedAt";

  @jakarta.annotation.Nullable
  private JsonNullable<OffsetDateTime> lastUsedAt = JsonNullable.<OffsetDateTime>undefined();

  public ApiKey() {}

  public ApiKey id(@jakarta.annotation.Nullable UUID id) {
    this.id = id;
    return this;
  }

  /**
   * API key ID
   * @return id
   */
  @jakarta.annotation.Nullable
  @JsonProperty(JSON_PROPERTY_ID)
  @JsonInclude(value = JsonInclude.Include.USE_DEFAULTS)
  public UUID getId() {
    return id;
  }

  @JsonProperty(JSON_PROPERTY_ID)
  @JsonInclude(value = JsonInclude.Include.USE_DEFAULTS)
  public void setId(@jakarta.annotation.Nullable UUID id) {
    this.id = id;
  }

  public ApiKey name(@jakarta.annotation.Nullable String name) {
    this.name = name;
    return this;
  }

  /**
   * Human-readable name for the API key
   * @return name
   */
  @jakarta.annotation.Nullable
  @JsonProperty(JSON_PROPERTY_NAME)
  @JsonInclude(value = JsonInclude.Include.USE_DEFAULTS)
  public String getName() {
    return name;
  }

  @JsonProperty(JSON_PROPERTY_NAME)
  @JsonInclude(value = JsonInclude.Include.USE_DEFAULTS)
  public void setName(@jakarta.annotation.Nullable String name) {
    this.name = name;
  }

  public ApiKey prefix(@jakarta.annotation.Nullable String prefix) {
    this.prefix = prefix;
    return this;
  }

  /**
   * First 8 characters of the API key for identification
   * @return prefix
   */
  @jakarta.annotation.Nullable
  @JsonProperty(JSON_PROPERTY_PREFIX)
  @JsonInclude(value = JsonInclude.Include.USE_DEFAULTS)
  public String getPrefix() {
    return prefix;
  }

  @JsonProperty(JSON_PROPERTY_PREFIX)
  @JsonInclude(value = JsonInclude.Include.USE_DEFAULTS)
  public void setPrefix(@jakarta.annotation.Nullable String prefix) {
    this.prefix = prefix;
  }

  public ApiKey createdAt(@jakarta.annotation.Nullable OffsetDateTime createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * When the API key was created
   * @return createdAt
   */
  @jakarta.annotation.Nullable
  @JsonProperty(JSON_PROPERTY_CREATED_AT)
  @JsonInclude(value = JsonInclude.Include.USE_DEFAULTS)
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }

  @JsonProperty(JSON_PROPERTY_CREATED_AT)
  @JsonInclude(value = JsonInclude.Include.USE_DEFAULTS)
  public void setCreatedAt(@jakarta.annotation.Nullable OffsetDateTime createdAt) {
    this.createdAt = createdAt;
  }

  public ApiKey expiresAt(@jakarta.annotation.Nullable OffsetDateTime expiresAt) {
    this.expiresAt = JsonNullable.<OffsetDateTime>of(expiresAt);

    return this;
  }

  /**
   * When the API key expires (null if no expiration)
   * @return expiresAt
   */
  @jakarta.annotation.Nullable
  @JsonIgnore
  public OffsetDateTime getExpiresAt() {
    return expiresAt.orElse(null);
  }

  @JsonProperty(JSON_PROPERTY_EXPIRES_AT)
  @JsonInclude(value = JsonInclude.Include.USE_DEFAULTS)
  public JsonNullable<OffsetDateTime> getExpiresAt_JsonNullable() {
    return expiresAt;
  }

  @JsonProperty(JSON_PROPERTY_EXPIRES_AT)
  public void setExpiresAt_JsonNullable(JsonNullable<OffsetDateTime> expiresAt) {
    this.expiresAt = expiresAt;
  }

  public void setExpiresAt(@jakarta.annotation.Nullable OffsetDateTime expiresAt) {
    this.expiresAt = JsonNullable.<OffsetDateTime>of(expiresAt);
  }

  public ApiKey lastUsedAt(@jakarta.annotation.Nullable OffsetDateTime lastUsedAt) {
    this.lastUsedAt = JsonNullable.<OffsetDateTime>of(lastUsedAt);

    return this;
  }

  /**
   * When the API key was last used (null if never used)
   * @return lastUsedAt
   */
  @jakarta.annotation.Nullable
  @JsonIgnore
  public OffsetDateTime getLastUsedAt() {
    return lastUsedAt.orElse(null);
  }

  @JsonProperty(JSON_PROPERTY_LAST_USED_AT)
  @JsonInclude(value = JsonInclude.Include.USE_DEFAULTS)
  public JsonNullable<OffsetDateTime> getLastUsedAt_JsonNullable() {
    return lastUsedAt;
  }

  @JsonProperty(JSON_PROPERTY_LAST_USED_AT)
  public void setLastUsedAt_JsonNullable(JsonNullable<OffsetDateTime> lastUsedAt) {
    this.lastUsedAt = lastUsedAt;
  }

  public void setLastUsedAt(@jakarta.annotation.Nullable OffsetDateTime lastUsedAt) {
    this.lastUsedAt = JsonNullable.<OffsetDateTime>of(lastUsedAt);
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ApiKey apiKey = (ApiKey) o;
    return (
      Objects.equals(this.id, apiKey.id) &&
      Objects.equals(this.name, apiKey.name) &&
      Objects.equals(this.prefix, apiKey.prefix) &&
      Objects.equals(this.createdAt, apiKey.createdAt) &&
      equalsNullable(this.expiresAt, apiKey.expiresAt) &&
      equalsNullable(this.lastUsedAt, apiKey.lastUsedAt)
    );
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return (
      a == b ||
      (a != null &&
        b != null &&
        a.isPresent() &&
        b.isPresent() &&
        Objects.deepEquals(a.get(), b.get()))
    );
  }

  @Override
  public int hashCode() {
    return Objects.hash(
      id,
      name,
      prefix,
      createdAt,
      hashCodeNullable(expiresAt),
      hashCodeNullable(lastUsedAt)
    );
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[] { a.get() }) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ApiKey {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    prefix: ").append(toIndentedString(prefix)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    expiresAt: ").append(toIndentedString(expiresAt)).append("\n");
    sb.append("    lastUsedAt: ").append(toIndentedString(lastUsedAt)).append("\n");
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
}
