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
import { SimilarGenesNetworkLink } from './similarGenesNetworkLink';
import { SimilarGenesNetworkNode } from './similarGenesNetworkNode';

/**
 * SimilarGenesNetwork
 */
export interface SimilarGenesNetwork {
  nodes: Array<SimilarGenesNetworkNode>;
  links: Array<SimilarGenesNetworkLink>;
  min: number;
  max: number;
}
