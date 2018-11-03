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
<<<<<<< HEAD
from io.pharmatrace.api.scin.public.api.locations_api import LocationsApi  # noqa: E501
=======
from openapi_client.api.locations_api import LocationsApi  # noqa: E501
>>>>>>> 980b10d2a42689b772558c10c6ebd68e97faca50
from openapi_client.rest import ApiException


class TestLocationsApi(unittest.TestCase):
    """LocationsApi unit test stubs"""

    def setUp(self):
<<<<<<< HEAD
        self.api = io.pharmatrace.api.scin.public.api.locations_api.LocationsApi()  # noqa: E501
=======
        self.api = openapi_client.api.locations_api.LocationsApi()  # noqa: E501
>>>>>>> 980b10d2a42689b772558c10c6ebd68e97faca50

    def tearDown(self):
        pass

    def test_add_location(self):
        """Test case for add_location

        """
        pass

    def test_delete_location(self):
        """Test case for delete_location

        """
        pass

    def test_find_location_by_id(self):
        """Test case for find_location_by_id

        """
        pass

    def test_find_locations(self):
        """Test case for find_locations

        """
        pass


if __name__ == '__main__':
    unittest.main()
