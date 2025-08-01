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

package org.sagebionetworks.openchallenges.api.client.api;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.sagebionetworks.openchallenges.api.client.model.BasicError;
import org.sagebionetworks.openchallenges.api.client.model.Image;
import org.sagebionetworks.openchallenges.api.client.model.ImageQuery;

/**
 * API tests for ImageApi
 */
@Disabled
public class ImageApiTest {

  private final ImageApi api = new ImageApi();

  /**
   * Get an image
   *
   * Returns the image specified.
   */
  @Test
  public void getImageTest() {
    ImageQuery imageQuery = null;
    Image response = api.getImage(imageQuery);
    // TODO: test validations
  }
}
