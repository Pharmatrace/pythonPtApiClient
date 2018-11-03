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
from io.pharmatrace.api.scin.public.api.container_api import ContainerApi  # noqa: E501
from openapi_client.rest import ApiException


class TestContainerApi(unittest.TestCase):
    """ContainerApi unit test stubs"""

    def setUp(self):
        self.api = io.pharmatrace.api.scin.public.api.container_api.ContainerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_location_history_get(self):
        """Test case for location_history_get

        Location History  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
