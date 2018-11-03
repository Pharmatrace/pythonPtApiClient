# coding: utf-8

"""
    PharmaTrace Supply Chain Information Network API

    The PharmaTrace SCIN API provides network members a resource and process oriented access to the blockchain backed market and inventory information. It represents a layer of abstraction above the Hyperledger network to facilitate a business focused development of clients and integration systems without the need to directly connect to Hyperledger nodes.  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: api@pharmatrace.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from io.pharmatrace.api.scin.public.api.profiles_api import ProfilesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestProfilesApi(unittest.TestCase):
    """ProfilesApi unit test stubs"""

    def setUp(self):
        self.api = io.pharmatrace.api.scin.public.api.profiles_api.ProfilesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_profile(self):
        """Test case for add_profile

        """
        pass

    def test_delete_profile(self):
        """Test case for delete_profile

        """
        pass

    def test_find_profile_by_id(self):
        """Test case for find_profile_by_id

        """
        pass

    def test_find_profiles(self):
        """Test case for find_profiles

        """
        pass


if __name__ == '__main__':
    unittest.main()