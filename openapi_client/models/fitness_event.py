# coding: utf-8

"""
    LAMP Platform

    The LAMP Platform API.  # noqa: E501

    OpenAPI spec version: 0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class FitnessEvent(object):
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
        'id': 'str',
        'attachments': 'dict(str, object)',
        'timestamp': 'int',
        'record': 'list[FitnessSample]'
    }

    attribute_map = {
        'id': 'id',
        'attachments': 'attachments',
        'timestamp': 'timestamp',
        'record': 'record'
    }

    def __init__(self, id=None, attachments=None, timestamp=None, record=None):  # noqa: E501
        """FitnessEvent - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._attachments = None
        self._timestamp = None
        self._record = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if attachments is not None:
            self.attachments = attachments
        if timestamp is not None:
            self.timestamp = timestamp
        if record is not None:
            self.record = record

    @property
    def id(self):
        """Gets the id of this FitnessEvent.  # noqa: E501

        A globally unique reference for objects within the LAMP platform.  # noqa: E501

        :return: The id of this FitnessEvent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FitnessEvent.

        A globally unique reference for objects within the LAMP platform.  # noqa: E501

        :param id: The id of this FitnessEvent.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def attachments(self):
        """Gets the attachments of this FitnessEvent.  # noqa: E501


        :return: The attachments of this FitnessEvent.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this FitnessEvent.


        :param attachments: The attachments of this FitnessEvent.  # noqa: E501
        :type: dict(str, object)
        """

        self._attachments = attachments

    @property
    def timestamp(self):
        """Gets the timestamp of this FitnessEvent.  # noqa: E501


        :return: The timestamp of this FitnessEvent.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this FitnessEvent.


        :param timestamp: The timestamp of this FitnessEvent.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def record(self):
        """Gets the record of this FitnessEvent.  # noqa: E501

        The set of all sub-samples within the event.  # noqa: E501

        :return: The record of this FitnessEvent.  # noqa: E501
        :rtype: list[FitnessSample]
        """
        return self._record

    @record.setter
    def record(self, record):
        """Sets the record of this FitnessEvent.

        The set of all sub-samples within the event.  # noqa: E501

        :param record: The record of this FitnessEvent.  # noqa: E501
        :type: list[FitnessSample]
        """

        self._record = record

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
        if not isinstance(other, FitnessEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
