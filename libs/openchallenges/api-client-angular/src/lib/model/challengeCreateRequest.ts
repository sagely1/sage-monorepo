/**
 * OpenChallenges API
 *
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { ChallengeStatus } from './challengeStatus';

/**
 * The information used to create a challenge
 */
export interface ChallengeCreateRequest {
  /**
   * The unique slug of the challenge.
   */
  slug: string;
  /**
   * The name of the challenge.
   */
  name: string;
  /**
   * The headline of the challenge.
   */
  headline?: string | null;
  /**
   * The description of the challenge.
   */
  description?: string;
  /**
   * The DOI of the challenge.
   */
  doi?: string | null;
  status: ChallengeStatus;
  /**
   * The unique identifier of a challenge platform.
   */
  platformId: number;
  /**
   * A URL to the website or image.
   */
  websiteUrl?: string | null;
  /**
   * A URL to the website or image.
   */
  avatarUrl?: string | null;
}
export namespace ChallengeCreateRequest {}
