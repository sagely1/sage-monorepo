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
 * Request for a list of FormData matching the provided filters.
 */
export interface OrgSagebionetworksRepoModelFormListRequest {
  /**
   * Only return results with a state that matches elements from this set.  Required. Must include at least one element.
   */
  filterByState?: Set<string>;
  groupId?: string;
  nextPageToken?: string;
}