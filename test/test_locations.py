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
from openapi_client.io.pharmatrace.api.scin.public.model.locations import Locations  # noqa: E501
=======
from openapi_client.models.locations import Locations  # noqa: E501
>>>>>>> 980b10d2a42689b772558c10c6ebd68e97faca50
from openapi_client.rest import ApiException


class TestLocations(unittest.TestCase):
    """Locations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLocations(self):
        """Test Locations"""
        # FIXME: construct object with mandatory attributes with example values
        # model = openapi_client.models.locations.Locations()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
