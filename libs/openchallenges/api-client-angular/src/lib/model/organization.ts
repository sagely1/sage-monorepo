/**
 * OpenChallenges REST API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


/**
 * An organization
 */
export interface Organization { 
    name: string;
    /**
     * An email address.
     */
    email: string;
    /**
     * The login of an organization
     */
    login: string;
    description: string;
    avatarUrl: string | null;
    websiteUrl: string;
    challengeCount?: number;
    createdAt: string;
    updatedAt: string;
    acronym: string;
}

