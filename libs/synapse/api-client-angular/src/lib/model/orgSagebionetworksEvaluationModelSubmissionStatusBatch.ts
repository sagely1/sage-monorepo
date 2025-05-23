/**
 * Synapse REST API
 *
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { OrgSagebionetworksEvaluationModelSubmissionStatus } from './orgSagebionetworksEvaluationModelSubmissionStatus';

/**
 * A batch of status objects, to be updated en masse.
 */
export interface OrgSagebionetworksEvaluationModelSubmissionStatusBatch {
  /**
   * A collection of Submission Statuses
   */
  statuses?: Array<OrgSagebionetworksEvaluationModelSubmissionStatus>;
  batchToken?: string;
  isFirstBatch?: boolean;
  isLastBatch?: boolean;
}
