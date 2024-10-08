/**
 * Synapse REST API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/**
 * Used to request a two fa reset token to be sent by email, can be requested with a twoFaToken returned by an authentication attempt.
 */
export interface OrgSagebionetworksRepoModelAuthTwoFactorAuthResetRequest {
  userId?: number;
  twoFaResetEndpoint?: string;
  twoFaToken?: string;
  password?: string;
}
