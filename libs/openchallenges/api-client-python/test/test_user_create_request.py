# coding: utf-8

"""
    OpenChallenges REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import openchallenges_client
from openchallenges_client.models.user_create_request import (
    UserCreateRequest,
)  # noqa: E501
from openchallenges_client.rest import ApiException


class TestUserCreateRequest(unittest.TestCase):
    """UserCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserCreateRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `UserCreateRequest`
        """
        model = openchallenges_client.models.user_create_request.UserCreateRequest()  # noqa: E501
        if include_optional :
            return UserCreateRequest(
                login = '', 
                email = 'john.smith@example.com', 
                password = '', 
                name = '', 
                avatar_url = 'https://example.com/awesome-avatar.png', 
                bio = ''
            )
        else :
            return UserCreateRequest(
                login = '',
                email = 'john.smith@example.com',
                password = '',
        )
        """

    def testUserCreateRequest(self):
        """Test UserCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
