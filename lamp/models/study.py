# coding: utf-8

"""
    LAMP Platform

    The LAMP Platform API.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from lamp.configuration import Configuration


class Study(object):
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
        'name': 'str',
        'activities': 'list[object]',
        'participants': 'list[object]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'activities': 'activities',
        'participants': 'participants'
    }

    def __init__(self, id=None, name=None, activities=None, participants=None, local_vars_configuration=None):  # noqa: E501
        """Study - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._activities = None
        self._participants = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if activities is not None:
            self.activities = activities
        if participants is not None:
            self.participants = participants

    @property
    def id(self):
        """Gets the id of this Study.  # noqa: E501

        A globally unique reference for objects.  # noqa: E501

        :return: The id of this Study.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Study.

        A globally unique reference for objects.  # noqa: E501

        :param id: The id of this Study.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Study.  # noqa: E501

        The name of the study.  # noqa: E501

        :return: The name of this Study.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Study.

        The name of the study.  # noqa: E501

        :param name: The name of this Study.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def activities(self):
        """Gets the activities of this Study.  # noqa: E501

        The set of all activities available in the study.  # noqa: E501

        :return: The activities of this Study.  # noqa: E501
        :rtype: list[object]
        """
        return self._activities

    @activities.setter
    def activities(self, activities):
        """Sets the activities of this Study.

        The set of all activities available in the study.  # noqa: E501

        :param activities: The activities of this Study.  # noqa: E501
        :type: list[object]
        """

        self._activities = activities

    @property
    def participants(self):
        """Gets the participants of this Study.  # noqa: E501

        The set of all enrolled participants in the study.  # noqa: E501

        :return: The participants of this Study.  # noqa: E501
        :rtype: list[object]
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """Sets the participants of this Study.

        The set of all enrolled participants in the study.  # noqa: E501

        :param participants: The participants of this Study.  # noqa: E501
        :type: list[object]
        """

        self._participants = participants

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
        if not isinstance(other, Study):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Study):
            return True

        return self.to_dict() != other.to_dict()
