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
import { OrgSagebionetworksRepoModelFileFileHandleResults } from './orgSagebionetworksRepoModelFileFileHandleResults';
import { OrgSagebionetworksRepoModelTableSelectColumn } from './orgSagebionetworksRepoModelTableSelectColumn';

/**
 * JSON schema for TableFileHandleResults.
 */
export interface OrgSagebionetworksRepoModelTableTableFileHandleResults {
  tableId?: string;
  /**
   * The list of ColumnModels ID that describes the rows of this set.
   */
  headers?: Array<OrgSagebionetworksRepoModelTableSelectColumn>;
  /**
   * For each row a list of file handles for each requested column
   */
  rows?: Array<OrgSagebionetworksRepoModelFileFileHandleResults>;
}