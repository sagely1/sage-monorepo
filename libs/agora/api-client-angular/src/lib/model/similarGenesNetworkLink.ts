/**
 * Agora REST API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/**
 * SimilarGenesNetworkLink
 */
export interface SimilarGenesNetworkLink {
  source: string;
  target: string;
  source_hgnc_symbol: string;
  target_hgnc_symbol: string;
  brain_regions: Array<string>;
}
