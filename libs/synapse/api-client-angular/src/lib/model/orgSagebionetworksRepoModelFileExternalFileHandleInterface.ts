/**
 * Synapse REST API
 *
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { OrgSagebionetworksRepoModelFileExternalFileHandle } from './orgSagebionetworksRepoModelFileExternalFileHandle';
import { OrgSagebionetworksRepoModelFileExternalObjectStoreFileHandle } from './orgSagebionetworksRepoModelFileExternalObjectStoreFileHandle';
import { OrgSagebionetworksRepoModelFileProxyFileHandle } from './orgSagebionetworksRepoModelFileProxyFileHandle';

/**
 * Defines FileHandles for files that are stored externally and can not be controlled by Synapse. All file access authentication and download/upload/delete operations are delegated the client.
 */
/**
 * @type OrgSagebionetworksRepoModelFileExternalFileHandleInterface
 * Defines FileHandles for files that are stored externally and can not be controlled by Synapse. All file access authentication and download/upload/delete operations are delegated the client.
 * @export
 */
export type OrgSagebionetworksRepoModelFileExternalFileHandleInterface =
  | OrgSagebionetworksRepoModelFileExternalFileHandle
  | OrgSagebionetworksRepoModelFileExternalObjectStoreFileHandle
  | OrgSagebionetworksRepoModelFileProxyFileHandle;
