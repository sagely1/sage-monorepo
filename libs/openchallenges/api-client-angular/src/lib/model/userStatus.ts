/**
 * OpenChallenges REST API
 *
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/**
 * The account status of a user
 */
export type UserStatus = 'pending' | 'approved' | 'disabled' | 'blacklist';

export const UserStatus = {
  Pending: 'pending' as UserStatus,
  Approved: 'approved' as UserStatus,
  Disabled: 'disabled' as UserStatus,
  Blacklist: 'blacklist' as UserStatus,
};
