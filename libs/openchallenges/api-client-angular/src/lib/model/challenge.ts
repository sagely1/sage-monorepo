/**
 * OpenChallenges API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { SimpleChallengePlatform } from './simpleChallengePlatform';
import { SimpleChallengeInputDataType } from './simpleChallengeInputDataType';
import { ChallengeDifficulty } from './challengeDifficulty';
import { ChallengeStatus } from './challengeStatus';
import { ChallengeIncentive } from './challengeIncentive';
import { ChallengeSubmissionType } from './challengeSubmissionType';


/**
 * A challenge
 */
export interface Challenge { 
    /**
     * The unique identifier of a challenge.
     */
    id: number;
    /**
     * The name of the a challenge
     */
    name: string;
    /**
     * The headline of the challenge.
     */
    headline?: string;
    /**
     * The description of the challenge.
     */
    description: string;
    status: ChallengeStatus;
    difficulty: ChallengeDifficulty;
    platform: SimpleChallengePlatform;
    websiteUrl?: string;
    avatarUrl?: string;
    incentives: Array<ChallengeIncentive>;
    submissionTypes: Array<ChallengeSubmissionType>;
    inputDataTypes?: Array<SimpleChallengeInputDataType>;
    /**
     * The start date of the challenge.
     */
    startDate?: string | null;
    /**
     * The end date of the challenge.
     */
    endDate?: string | null;
    /**
     * The number of times the challenge has been starred by users.
     */
    starredCount: number;
    createdAt: string;
    updatedAt: string;
}

