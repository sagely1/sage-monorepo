/**
 * OpenChallenges API
 *
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/**
 * A challenge platform update request.
 */
export interface ChallengePlatformUpdateRequest {
  /**
   * The slug of the challenge platform.
   */
  slug: string;
  /**
   * The display name of the challenge platform.
   */
  name: string;
  /**
   * The avatar key
   */
  avatarKey: string;
  /**
   * A URL to the website or image.
   */
  websiteUrl: string | null;
}
