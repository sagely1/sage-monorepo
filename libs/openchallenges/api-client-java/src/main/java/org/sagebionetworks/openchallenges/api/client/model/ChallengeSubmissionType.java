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
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.annotation.JsonTypeName;
import com.fasterxml.jackson.annotation.JsonValue;
import java.util.Arrays;
import java.util.Objects;

/**
 * The submission type of the challenge.
 */
public enum ChallengeSubmissionType {
  CONTAINER_IMAGE("container_image"),

  PREDICTION_FILE("prediction_file"),

  NOTEBOOK("notebook"),

  MLCUBE("mlcube"),

  OTHER("other");

  private String value;

  ChallengeSubmissionType(String value) {
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
  public static ChallengeSubmissionType fromValue(String value) {
    for (ChallengeSubmissionType b : ChallengeSubmissionType.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }
}
