/**
 * Synapse REST API
 *
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { OrgSagebionetworksRepoModelSchemaValidationException } from './orgSagebionetworksRepoModelSchemaValidationException';

/**
 * Results of validating an object against a schema
 */
export interface OrgSagebionetworksRepoModelSchemaValidationResults {
  objectId?: string;
  objectType?: string;
  objectEtag?: string;
  schema$id?: string;
  isValid?: boolean;
  validatedOn?: string;
  validationErrorMessage?: string;
  /**
   * If the object is not valid according to the schema, a the flat list of error messages will be provided with one error message per sub-schema.
   */
  allValidationMessages?: Array<string>;
  validationException?: OrgSagebionetworksRepoModelSchemaValidationException;
}
