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
 * The permission a User has for a given Evaluation
 */
export interface OrgSagebionetworksEvaluationModelUserEvaluationPermissions {
  canChangePermissions?: boolean;
  canView?: boolean;
  canPublicRead?: boolean;
  canEdit?: boolean;
  canDelete?: boolean;
  canParticipate?: boolean;
  canSubmit?: boolean;
  canViewPrivateSubmissionStatusAnnotations?: boolean;
  canEditSubmissionStatuses?: boolean;
  canDeleteSubmissions?: boolean;
  ownerPrincipalId?: number;
}