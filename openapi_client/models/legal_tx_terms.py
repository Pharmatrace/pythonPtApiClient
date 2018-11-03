# coding: utf-8

"""
    PharmaTrace Supply Chain Information Network API

    The PharmaTrace SCIN API provides network members a resource and process oriented access to the blockchain backed market and inventory information. It represents a layer of abstraction above the Hyperledger network to facilitate a business focused development of clients and integration systems without the need to directly connect to Hyperledger nodes.  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: api@pharmatrace.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class LegalTxTerms(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'timestamp_valid_from': 'int',
        'timestamp_valid_until': 'int',
        'validity_tolerance': 'int',
        'terms_id': 'str',
        'terms_version': 'str',
        'terms_id_previous_version': 'str',
        'terms_text': 'str',
        'language': 'str',
        'legislation': 'str'
    }

    attribute_map = {
        'timestamp_valid_from': 'timestamp_valid_from',
        'timestamp_valid_until': 'timestamp_valid_until',
        'validity_tolerance': 'validity_tolerance',
        'terms_id': 'terms_id',
        'terms_version': 'terms_version',
        'terms_id_previous_version': 'terms_id_previous_version',
        'terms_text': 'terms_text',
        'language': 'language',
        'legislation': 'legislation'
    }

    def __init__(self, timestamp_valid_from=None, timestamp_valid_until=None, validity_tolerance=None, terms_id=None, terms_version=None, terms_id_previous_version=None, terms_text=None, language=None, legislation=None):  # noqa: E501
        """LegalTxTerms - a model defined in OpenAPI"""  # noqa: E501

        self._timestamp_valid_from = None
        self._timestamp_valid_until = None
        self._validity_tolerance = None
        self._terms_id = None
        self._terms_version = None
        self._terms_id_previous_version = None
        self._terms_text = None
        self._language = None
        self._legislation = None
        self.discriminator = None

        if timestamp_valid_from is not None:
            self.timestamp_valid_from = timestamp_valid_from
        if timestamp_valid_until is not None:
            self.timestamp_valid_until = timestamp_valid_until
        if validity_tolerance is not None:
            self.validity_tolerance = validity_tolerance
        if terms_id is not None:
            self.terms_id = terms_id
        if terms_version is not None:
            self.terms_version = terms_version
        if terms_id_previous_version is not None:
            self.terms_id_previous_version = terms_id_previous_version
        if terms_text is not None:
            self.terms_text = terms_text
        if language is not None:
            self.language = language
        if legislation is not None:
            self.legislation = legislation

    @property
    def timestamp_valid_from(self):
        """Gets the timestamp_valid_from of this LegalTxTerms.  # noqa: E501

        GMT, Unix Epoch  # noqa: E501

        :return: The timestamp_valid_from of this LegalTxTerms.  # noqa: E501
        :rtype: int
        """
        return self._timestamp_valid_from

    @timestamp_valid_from.setter
    def timestamp_valid_from(self, timestamp_valid_from):
        """Sets the timestamp_valid_from of this LegalTxTerms.

        GMT, Unix Epoch  # noqa: E501

        :param timestamp_valid_from: The timestamp_valid_from of this LegalTxTerms.  # noqa: E501
        :type: int
        """

        self._timestamp_valid_from = timestamp_valid_from

    @property
    def timestamp_valid_until(self):
        """Gets the timestamp_valid_until of this LegalTxTerms.  # noqa: E501

        GMT, Unix Epoch  # noqa: E501

        :return: The timestamp_valid_until of this LegalTxTerms.  # noqa: E501
        :rtype: int
        """
        return self._timestamp_valid_until

    @timestamp_valid_until.setter
    def timestamp_valid_until(self, timestamp_valid_until):
        """Sets the timestamp_valid_until of this LegalTxTerms.

        GMT, Unix Epoch  # noqa: E501

        :param timestamp_valid_until: The timestamp_valid_until of this LegalTxTerms.  # noqa: E501
        :type: int
        """

        self._timestamp_valid_until = timestamp_valid_until

    @property
    def validity_tolerance(self):
        """Gets the validity_tolerance of this LegalTxTerms.  # noqa: E501

        tolerance window for transactions that begin but do not finish under the governance of these terms (in ms)  # noqa: E501

        :return: The validity_tolerance of this LegalTxTerms.  # noqa: E501
        :rtype: int
        """
        return self._validity_tolerance

    @validity_tolerance.setter
    def validity_tolerance(self, validity_tolerance):
        """Sets the validity_tolerance of this LegalTxTerms.

        tolerance window for transactions that begin but do not finish under the governance of these terms (in ms)  # noqa: E501

        :param validity_tolerance: The validity_tolerance of this LegalTxTerms.  # noqa: E501
        :type: int
        """

        self._validity_tolerance = validity_tolerance

    @property
    def terms_id(self):
        """Gets the terms_id of this LegalTxTerms.  # noqa: E501

        unique id hash of the transaction terms and conditions  # noqa: E501

        :return: The terms_id of this LegalTxTerms.  # noqa: E501
        :rtype: str
        """
        return self._terms_id

    @terms_id.setter
    def terms_id(self, terms_id):
        """Sets the terms_id of this LegalTxTerms.

        unique id hash of the transaction terms and conditions  # noqa: E501

        :param terms_id: The terms_id of this LegalTxTerms.  # noqa: E501
        :type: str
        """

        self._terms_id = terms_id

    @property
    def terms_version(self):
        """Gets the terms_version of this LegalTxTerms.  # noqa: E501

        optional version mark of the terms  # noqa: E501

        :return: The terms_version of this LegalTxTerms.  # noqa: E501
        :rtype: str
        """
        return self._terms_version

    @terms_version.setter
    def terms_version(self, terms_version):
        """Sets the terms_version of this LegalTxTerms.

        optional version mark of the terms  # noqa: E501

        :param terms_version: The terms_version of this LegalTxTerms.  # noqa: E501
        :type: str
        """

        self._terms_version = terms_version

    @property
    def terms_id_previous_version(self):
        """Gets the terms_id_previous_version of this LegalTxTerms.  # noqa: E501

        optional link to the previous version of these terms  # noqa: E501

        :return: The terms_id_previous_version of this LegalTxTerms.  # noqa: E501
        :rtype: str
        """
        return self._terms_id_previous_version

    @terms_id_previous_version.setter
    def terms_id_previous_version(self, terms_id_previous_version):
        """Sets the terms_id_previous_version of this LegalTxTerms.

        optional link to the previous version of these terms  # noqa: E501

        :param terms_id_previous_version: The terms_id_previous_version of this LegalTxTerms.  # noqa: E501
        :type: str
        """

        self._terms_id_previous_version = terms_id_previous_version

    @property
    def terms_text(self):
        """Gets the terms_text of this LegalTxTerms.  # noqa: E501

        text of the terms and conditions  # noqa: E501

        :return: The terms_text of this LegalTxTerms.  # noqa: E501
        :rtype: str
        """
        return self._terms_text

    @terms_text.setter
    def terms_text(self, terms_text):
        """Sets the terms_text of this LegalTxTerms.

        text of the terms and conditions  # noqa: E501

        :param terms_text: The terms_text of this LegalTxTerms.  # noqa: E501
        :type: str
        """

        self._terms_text = terms_text

    @property
    def language(self):
        """Gets the language of this LegalTxTerms.  # noqa: E501

        ISO language code, e.g. en_us  # noqa: E501

        :return: The language of this LegalTxTerms.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this LegalTxTerms.

        ISO language code, e.g. en_us  # noqa: E501

        :param language: The language of this LegalTxTerms.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def legislation(self):
        """Gets the legislation of this LegalTxTerms.  # noqa: E501

        legislation enforcing these terms  # noqa: E501

        :return: The legislation of this LegalTxTerms.  # noqa: E501
        :rtype: str
        """
        return self._legislation

    @legislation.setter
    def legislation(self, legislation):
        """Sets the legislation of this LegalTxTerms.

        legislation enforcing these terms  # noqa: E501

        :param legislation: The legislation of this LegalTxTerms.  # noqa: E501
        :type: str
        """

        self._legislation = legislation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LegalTxTerms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other