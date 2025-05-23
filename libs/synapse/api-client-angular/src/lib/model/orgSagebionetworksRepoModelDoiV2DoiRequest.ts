/**
 * Synapse REST API
 *
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { OrgSagebionetworksRepoModelDoiV2Doi } from './orgSagebionetworksRepoModelDoiV2Doi';

/**
 * An AsynchronousRequestBody to mint or modify DOIs.
 */
export interface OrgSagebionetworksRepoModelDoiV2DoiRequest {
  concreteType: OrgSagebionetworksRepoModelDoiV2DoiRequest.ConcreteTypeEnum;
  doi?: OrgSagebionetworksRepoModelDoiV2Doi;
}
export namespace OrgSagebionetworksRepoModelDoiV2DoiRequest {
  export type ConcreteTypeEnum = 'org.sagebionetworks.repo.model.doi.v2.DoiRequest';
  export const ConcreteTypeEnum = {
    OrgSagebionetworksRepoModelDoiV2DoiRequest:
      'org.sagebionetworks.repo.model.doi.v2.DoiRequest' as ConcreteTypeEnum,
  };
}
