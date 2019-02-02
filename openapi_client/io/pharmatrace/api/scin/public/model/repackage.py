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


class Repackage(object):
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
        'timestamp': 'int',
        'tx_uid': 'str',
        'terms_id': 'str',
        'transaction_channel': 'str'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'tx_uid': 'tx_uid',
        'terms_id': 'terms_id',
        'transaction_channel': 'transaction_channel'
    }

    def __init__(self, timestamp=None, tx_uid=None, terms_id=None, transaction_channel=None):  # noqa: E501
        """Repackage - a model defined in OpenAPI"""  # noqa: E501

        self._timestamp = None
        self._tx_uid = None
        self._terms_id = None
        self._transaction_channel = None
        self.discriminator = None

        if timestamp is not None:
            self.timestamp = timestamp
        if tx_uid is not None:
            self.tx_uid = tx_uid
        if terms_id is not None:
            self.terms_id = terms_id
        if transaction_channel is not None:
            self.transaction_channel = transaction_channel

    @property
    def timestamp(self):
        """Gets the timestamp of this Repackage.  # noqa: E501

        GMT, Unix Epoch  # noqa: E501

        :return: The timestamp of this Repackage.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Repackage.

        GMT, Unix Epoch  # noqa: E501

        :param timestamp: The timestamp of this Repackage.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def tx_uid(self):
        """Gets the tx_uid of this Repackage.  # noqa: E501

        unique id hash of the transaction  # noqa: E501

        :return: The tx_uid of this Repackage.  # noqa: E501
        :rtype: str
        """
        return self._tx_uid

    @tx_uid.setter
    def tx_uid(self, tx_uid):
        """Sets the tx_uid of this Repackage.

        unique id hash of the transaction  # noqa: E501

        :param tx_uid: The tx_uid of this Repackage.  # noqa: E501
        :type: str
        """

        self._tx_uid = tx_uid

    @property
    def terms_id(self):
        """Gets the terms_id of this Repackage.  # noqa: E501

        id reference to the terms and conditions for this transaction  # noqa: E501

        :return: The terms_id of this Repackage.  # noqa: E501
        :rtype: str
        """
        return self._terms_id

    @terms_id.setter
    def terms_id(self, terms_id):
        """Sets the terms_id of this Repackage.

        id reference to the terms and conditions for this transaction  # noqa: E501

        :param terms_id: The terms_id of this Repackage.  # noqa: E501
        :type: str
        """

        self._terms_id = terms_id

    @property
    def transaction_channel(self):
        """Gets the transaction_channel of this Repackage.  # noqa: E501

        hyperledger channel the transaction has been executed in  # noqa: E501

        :return: The transaction_channel of this Repackage.  # noqa: E501
        :rtype: str
        """
        return self._transaction_channel

    @transaction_channel.setter
    def transaction_channel(self, transaction_channel):
        """Sets the transaction_channel of this Repackage.

        hyperledger channel the transaction has been executed in  # noqa: E501

        :param transaction_channel: The transaction_channel of this Repackage.  # noqa: E501
        :type: str
        """

        self._transaction_channel = transaction_channel

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
        if not isinstance(other, Repackage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
