/**
 * Synapse REST API
 *
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/**
 * Contains the name and type of the column to be filtered, and the facet values to filter on.
 */
export interface OrgSagebionetworksRepoModelTableFacetColumnValuesRequest {
  concreteType: OrgSagebionetworksRepoModelTableFacetColumnValuesRequest.ConcreteTypeEnum;
  columnName?: string;
  jsonPath?: string;
  /**
   * The set of facet values that were selected
   */
  facetValues?: Set<string>;
}
export namespace OrgSagebionetworksRepoModelTableFacetColumnValuesRequest {
  export type ConcreteTypeEnum = 'org.sagebionetworks.repo.model.table.FacetColumnValuesRequest';
  export const ConcreteTypeEnum = {
    OrgSagebionetworksRepoModelTableFacetColumnValuesRequest:
      'org.sagebionetworks.repo.model.table.FacetColumnValuesRequest' as ConcreteTypeEnum,
  };
}
