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
from io.pharmatrace.api.scin.public.api.legal_tx_termss_api import LegalTxTermssApi  # noqa: E501
=======
from openapi_client.api.legal_tx_termss_api import LegalTxTermssApi  # noqa: E501
>>>>>>> 980b10d2a42689b772558c10c6ebd68e97faca50
from openapi_client.rest import ApiException


class TestLegalTxTermssApi(unittest.TestCase):
    """LegalTxTermssApi unit test stubs"""

    def setUp(self):
<<<<<<< HEAD
        self.api = io.pharmatrace.api.scin.public.api.legal_tx_termss_api.LegalTxTermssApi()  # noqa: E501
=======
        self.api = openapi_client.api.legal_tx_termss_api.LegalTxTermssApi()  # noqa: E501
>>>>>>> 980b10d2a42689b772558c10c6ebd68e97faca50

    def tearDown(self):
        pass

    def test_add_legal_tx_terms(self):
        """Test case for add_legal_tx_terms

        """
        pass

    def test_delete_legal_tx_terms(self):
        """Test case for delete_legal_tx_terms

        """
        pass

    def test_find_legal_tx_termss(self):
        """Test case for find_legal_tx_termss

        """
        pass

    def test_find_legaltxterms_by_id(self):
        """Test case for find_legaltxterms_by_id

        """
        pass


if __name__ == '__main__':
    unittest.main()
