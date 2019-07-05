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


class ActivityDefinition(object):
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
        'static_data': 'list[ActivitySpecItem]',
        'temporal_event': 'list[ActivitySpecItem]',
        'settings': 'list[ActivitySpecItem]'
    }

    attribute_map = {
        'static_data': 'static_data',
        'temporal_event': 'temporal_event',
        'settings': 'settings'
    }

    def __init__(self, static_data=None, temporal_event=None, settings=None):  # noqa: E501
        """ActivityDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._static_data = None
        self._temporal_event = None
        self._settings = None
        self.discriminator = None

        if static_data is not None:
            self.static_data = static_data
        if temporal_event is not None:
            self.temporal_event = temporal_event
        if settings is not None:
            self.settings = settings

    @property
    def static_data(self):
        """Gets the static_data of this ActivityDefinition.  # noqa: E501


        :return: The static_data of this ActivityDefinition.  # noqa: E501
        :rtype: list[ActivitySpecItem]
        """
        return self._static_data

    @static_data.setter
    def static_data(self, static_data):
        """Sets the static_data of this ActivityDefinition.


        :param static_data: The static_data of this ActivityDefinition.  # noqa: E501
        :type: list[ActivitySpecItem]
        """

        self._static_data = static_data

    @property
    def temporal_event(self):
        """Gets the temporal_event of this ActivityDefinition.  # noqa: E501


        :return: The temporal_event of this ActivityDefinition.  # noqa: E501
        :rtype: list[ActivitySpecItem]
        """
        return self._temporal_event

    @temporal_event.setter
    def temporal_event(self, temporal_event):
        """Sets the temporal_event of this ActivityDefinition.


        :param temporal_event: The temporal_event of this ActivityDefinition.  # noqa: E501
        :type: list[ActivitySpecItem]
        """

        self._temporal_event = temporal_event

    @property
    def settings(self):
        """Gets the settings of this ActivityDefinition.  # noqa: E501


        :return: The settings of this ActivityDefinition.  # noqa: E501
        :rtype: list[ActivitySpecItem]
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this ActivityDefinition.


        :param settings: The settings of this ActivityDefinition.  # noqa: E501
        :type: list[ActivitySpecItem]
        """

        self._settings = settings

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
        if not isinstance(other, ActivityDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
