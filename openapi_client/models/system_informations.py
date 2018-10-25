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


class SystemInformations(object):
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
        'offset': 'int',
        'limit': 'int',
        'count': 'int',
        'history': 'list[SystemInformation]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'count': 'count',
        'history': 'history'
    }

    def __init__(self, offset=None, limit=None, count=None, history=None):  # noqa: E501
        """SystemInformations - a model defined in OpenAPI"""  # noqa: E501

        self._offset = None
        self._limit = None
        self._count = None
        self._history = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if count is not None:
            self.count = count
        if history is not None:
            self.history = history

    @property
    def offset(self):
        """Gets the offset of this SystemInformations.  # noqa: E501

        Position in pagination.  # noqa: E501

        :return: The offset of this SystemInformations.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SystemInformations.

        Position in pagination.  # noqa: E501

        :param offset: The offset of this SystemInformations.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SystemInformations.  # noqa: E501

        Number of items to retrieve (100 max).  # noqa: E501

        :return: The limit of this SystemInformations.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SystemInformations.

        Number of items to retrieve (100 max).  # noqa: E501

        :param limit: The limit of this SystemInformations.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def count(self):
        """Gets the count of this SystemInformations.  # noqa: E501

        Total number of items available.  # noqa: E501

        :return: The count of this SystemInformations.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this SystemInformations.

        Total number of items available.  # noqa: E501

        :param count: The count of this SystemInformations.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def history(self):
        """Gets the history of this SystemInformations.  # noqa: E501


        :return: The history of this SystemInformations.  # noqa: E501
        :rtype: list[SystemInformation]
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this SystemInformations.


        :param history: The history of this SystemInformations.  # noqa: E501
        :type: list[SystemInformation]
        """

        self._history = history

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
        if not isinstance(other, SystemInformations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
