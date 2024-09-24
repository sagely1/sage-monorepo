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
import { OrgSagebionetworksRepoModelDataaccessAccessorChange } from './orgSagebionetworksRepoModelDataaccessAccessorChange';

/**
 * A Request contains information required by an AccessRequirement.
 */
export interface OrgSagebionetworksRepoModelDataaccessRequest {
  id?: string;
  accessRequirementId?: string;
  researchProjectId?: string;
  createdOn?: string;
  modifiedOn?: string;
  createdBy?: string;
  modifiedBy?: string;
  ducFileHandleId?: string;
  irbFileHandleId?: string;
  /**
   * The set of file handle ID of attached files to this request.
   */
  attachments?: Array<string>;
  /**
   * List of user changes. A user can gain access, renew access or have access revoked.
   */
  accessorChanges?: Array<OrgSagebionetworksRepoModelDataaccessAccessorChange>;
  etag?: string;
  concreteType: OrgSagebionetworksRepoModelDataaccessRequest.ConcreteTypeEnum;
}
export namespace OrgSagebionetworksRepoModelDataaccessRequest {
  export type ConcreteTypeEnum = 'org.sagebionetworks.repo.model.dataaccess.Request';
  export const ConcreteTypeEnum = {
    OrgSagebionetworksRepoModelDataaccessRequest:
      'org.sagebionetworks.repo.model.dataaccess.Request' as ConcreteTypeEnum,
  };
}