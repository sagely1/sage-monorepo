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
 * The FileHandleSnapshot captures all of the fields that are common to all FileHandle implementations.
 */
export interface OrgSagebionetworksRepoModelAuditFileHandleSnapshot {
  id?: string;
  createdBy?: string;
  createdOn?: string;
  modifiedOn?: string;
  concreteType: OrgSagebionetworksRepoModelAuditFileHandleSnapshot.ConcreteTypeEnum;
  contentMd5?: string;
  contentType?: string;
  fileName?: string;
  storageLocationId?: number;
  contentSize?: number;
  key?: string;
  bucket?: string;
  previewId?: string;
  isPreview?: boolean;
  status?: string;
}
export namespace OrgSagebionetworksRepoModelAuditFileHandleSnapshot {
  export type ConcreteTypeEnum = 'org.sagebionetworks.repo.model.audit.FileHandleSnapshot';
  export const ConcreteTypeEnum = {
    OrgSagebionetworksRepoModelAuditFileHandleSnapshot:
      'org.sagebionetworks.repo.model.audit.FileHandleSnapshot' as ConcreteTypeEnum,
  };
}