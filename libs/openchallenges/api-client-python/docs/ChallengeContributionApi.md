# openchallenges_api_client_python.ChallengeContributionApi

All URIs are relative to *https://openchallenges.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_challenge_contribution**](ChallengeContributionApi.md#create_challenge_contribution) | **POST** /challenges/{challengeId}/contributions | Create a new contribution for a challenge
[**delete_challenge_contribution**](ChallengeContributionApi.md#delete_challenge_contribution) | **DELETE** /challenges/{challengeId}/contributions/{organizationId}/role/{role} | Delete a specific challenge contribution
[**get_challenge_contribution**](ChallengeContributionApi.md#get_challenge_contribution) | **GET** /challenges/{challengeId}/contributions/{organizationId}/role/{role} | Get a specific challenge contribution
[**list_challenge_contributions**](ChallengeContributionApi.md#list_challenge_contributions) | **GET** /challenges/{challengeId}/contributions | List challenge contributions


# **create_challenge_contribution**
> ChallengeContribution create_challenge_contribution(challenge_id, challenge_contribution_create_request)

Create a new contribution for a challenge

Creates a new contribution record associated with a challenge ID.


### Example

* Bearer (api_key) Authentication (apiBearerAuth):

```python
import openchallenges_api_client_python
from openchallenges_api_client_python.models.challenge_contribution import ChallengeContribution
from openchallenges_api_client_python.models.challenge_contribution_create_request import ChallengeContributionCreateRequest
from openchallenges_api_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://openchallenges.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openchallenges_api_client_python.Configuration(
    host = "https://openchallenges.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (api_key): apiBearerAuth
configuration = openchallenges_api_client_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openchallenges_api_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openchallenges_api_client_python.ChallengeContributionApi(api_client)
    challenge_id = 56 # int | The unique identifier of the challenge.
    challenge_contribution_create_request = openchallenges_api_client_python.ChallengeContributionCreateRequest() # ChallengeContributionCreateRequest | 

    try:
        # Create a new contribution for a challenge
        api_response = api_instance.create_challenge_contribution(challenge_id, challenge_contribution_create_request)
        print("The response of ChallengeContributionApi->create_challenge_contribution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChallengeContributionApi->create_challenge_contribution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **int**| The unique identifier of the challenge. | 
 **challenge_contribution_create_request** | [**ChallengeContributionCreateRequest**](ChallengeContributionCreateRequest.md)|  | 

### Return type

[**ChallengeContribution**](ChallengeContribution.md)

### Authorization

[apiBearerAuth](../README.md#apiBearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Contribution created successfully |  -  |
**401** | Unauthorized |  -  |
**403** | The user does not have the permission to perform this action |  -  |
**404** | The specified resource was not found |  -  |
**409** | The request conflicts with current state of the target resource |  -  |
**500** | The request cannot be fulfilled due to an unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_challenge_contribution**
> delete_challenge_contribution(challenge_id, organization_id, role)

Delete a specific challenge contribution

Delete a specific challenge contribution.

### Example

* Bearer (api_key) Authentication (apiBearerAuth):

```python
import openchallenges_api_client_python
from openchallenges_api_client_python.models.challenge_contribution_role import ChallengeContributionRole
from openchallenges_api_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://openchallenges.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openchallenges_api_client_python.Configuration(
    host = "https://openchallenges.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (api_key): apiBearerAuth
configuration = openchallenges_api_client_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openchallenges_api_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openchallenges_api_client_python.ChallengeContributionApi(api_client)
    challenge_id = 56 # int | The unique identifier of the challenge.
    organization_id = 56 # int | The unique identifier of the organization.
    role = openchallenges_api_client_python.ChallengeContributionRole() # ChallengeContributionRole | A challenge contribution role.

    try:
        # Delete a specific challenge contribution
        api_instance.delete_challenge_contribution(challenge_id, organization_id, role)
    except Exception as e:
        print("Exception when calling ChallengeContributionApi->delete_challenge_contribution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **int**| The unique identifier of the challenge. | 
 **organization_id** | **int**| The unique identifier of the organization. | 
 **role** | [**ChallengeContributionRole**](.md)| A challenge contribution role. | 

### Return type

void (empty response body)

### Authorization

[apiBearerAuth](../README.md#apiBearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Contribution deleted successfully |  -  |
**401** | Unauthorized |  -  |
**403** | The user does not have the permission to perform this action |  -  |
**404** | The specified resource was not found |  -  |
**500** | The request cannot be fulfilled due to an unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_challenge_contribution**
> ChallengeContribution get_challenge_contribution(challenge_id, organization_id, role)

Get a specific challenge contribution

Retrieves a specific contribution record for a challenge, identified by its ID.


### Example


```python
import openchallenges_api_client_python
from openchallenges_api_client_python.models.challenge_contribution import ChallengeContribution
from openchallenges_api_client_python.models.challenge_contribution_role import ChallengeContributionRole
from openchallenges_api_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://openchallenges.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openchallenges_api_client_python.Configuration(
    host = "https://openchallenges.io/api/v1"
)


# Enter a context with an instance of the API client
with openchallenges_api_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openchallenges_api_client_python.ChallengeContributionApi(api_client)
    challenge_id = 56 # int | The unique identifier of the challenge.
    organization_id = 56 # int | The unique identifier of the organization.
    role = openchallenges_api_client_python.ChallengeContributionRole() # ChallengeContributionRole | A challenge contribution role.

    try:
        # Get a specific challenge contribution
        api_response = api_instance.get_challenge_contribution(challenge_id, organization_id, role)
        print("The response of ChallengeContributionApi->get_challenge_contribution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChallengeContributionApi->get_challenge_contribution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **int**| The unique identifier of the challenge. | 
 **organization_id** | **int**| The unique identifier of the organization. | 
 **role** | [**ChallengeContributionRole**](.md)| A challenge contribution role. | 

### Return type

[**ChallengeContribution**](ChallengeContribution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Challenge contribution retrieved successfully |  -  |
**400** | Invalid request |  -  |
**404** | The specified resource was not found |  -  |
**500** | The request cannot be fulfilled due to an unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_challenge_contributions**
> ChallengeContributionsPage list_challenge_contributions(challenge_id)

List challenge contributions

List challenge contributions

### Example


```python
import openchallenges_api_client_python
from openchallenges_api_client_python.models.challenge_contributions_page import ChallengeContributionsPage
from openchallenges_api_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://openchallenges.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openchallenges_api_client_python.Configuration(
    host = "https://openchallenges.io/api/v1"
)


# Enter a context with an instance of the API client
with openchallenges_api_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openchallenges_api_client_python.ChallengeContributionApi(api_client)
    challenge_id = 56 # int | The unique identifier of the challenge.

    try:
        # List challenge contributions
        api_response = api_instance.list_challenge_contributions(challenge_id)
        print("The response of ChallengeContributionApi->list_challenge_contributions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChallengeContributionApi->list_challenge_contributions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **int**| The unique identifier of the challenge. | 

### Return type

[**ChallengeContributionsPage**](ChallengeContributionsPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**500** | The request cannot be fulfilled due to an unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

