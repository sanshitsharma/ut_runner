# coding: utf-8

"""
    REST APIs for UT runner

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UnitTesterJobCreateResp(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'job_id': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'created_at': 'created_at'
    }

    def __init__(self, job_id=None, created_at=None):  # noqa: E501
        """UnitTesterJobCreateResp - a model defined in Swagger"""  # noqa: E501

        self._job_id = None
        self._created_at = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if created_at is not None:
            self.created_at = created_at

    @property
    def job_id(self):
        """Gets the job_id of this UnitTesterJobCreateResp.  # noqa: E501

        A unique ID to track the job created.  # noqa: E501

        :return: The job_id of this UnitTesterJobCreateResp.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this UnitTesterJobCreateResp.

        A unique ID to track the job created.  # noqa: E501

        :param job_id: The job_id of this UnitTesterJobCreateResp.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def created_at(self):
        """Gets the created_at of this UnitTesterJobCreateResp.  # noqa: E501

        Time at which job got created.  # noqa: E501

        :return: The created_at of this UnitTesterJobCreateResp.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UnitTesterJobCreateResp.

        Time at which job got created.  # noqa: E501

        :param created_at: The created_at of this UnitTesterJobCreateResp.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(UnitTesterJobCreateResp, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UnitTesterJobCreateResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other