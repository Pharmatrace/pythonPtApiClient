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
from io.pharmatrace.api.scin.public.api.containers_api import ContainersApi  # noqa: E501
from openapi_client.rest import ApiException


class TestContainersApi(unittest.TestCase):
    """ContainersApi unit test stubs"""

    def setUp(self):
        self.api = io.pharmatrace.api.scin.public.api.containers_api.ContainersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_container(self):
        """Test case for add_container

        """
        pass

    def test_delete_container(self):
        """Test case for delete_container

        """
        pass

    def test_find_container_by_id(self):
        """Test case for find_container_by_id

        """
        pass

    def test_find_containers(self):
        """Test case for find_containers

        """
        pass


if __name__ == '__main__':
    unittest.main()