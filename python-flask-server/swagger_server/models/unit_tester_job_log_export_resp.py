# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UnitTesterJobLogExportResp(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, export: str=None):  # noqa: E501
        """UnitTesterJobLogExportResp - a model defined in Swagger

        :param export: The export of this UnitTesterJobLogExportResp.  # noqa: E501
        :type export: str
        """
        self.swagger_types = {
            'export': str
        }

        self.attribute_map = {
            'export': 'export'
        }

        self._export = export

    @classmethod
    def from_dict(cls, dikt) -> 'UnitTesterJobLogExportResp':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The unit_testerJobLogExportResp of this UnitTesterJobLogExportResp.  # noqa: E501
        :rtype: UnitTesterJobLogExportResp
        """
        return util.deserialize_model(dikt, cls)

    @property
    def export(self) -> str:
        """Gets the export of this UnitTesterJobLogExportResp.

        Base64 encoded string representing the exported gunzip arhieve  # noqa: E501

        :return: The export of this UnitTesterJobLogExportResp.
        :rtype: str
        """
        return self._export

    @export.setter
    def export(self, export: str):
        """Sets the export of this UnitTesterJobLogExportResp.

        Base64 encoded string representing the exported gunzip arhieve  # noqa: E501

        :param export: The export of this UnitTesterJobLogExportResp.
        :type export: str
        """

        self._export = export
