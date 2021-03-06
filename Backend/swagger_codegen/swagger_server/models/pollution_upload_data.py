# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PollutionUploadData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, in_temp: float=None, out_temp: float=None, lpo_time: float=None, co2: float=None):  # noqa: E501
        """PollutionUploadData - a model defined in Swagger

        :param in_temp: The in_temp of this PollutionUploadData.  # noqa: E501
        :type in_temp: float
        :param out_temp: The out_temp of this PollutionUploadData.  # noqa: E501
        :type out_temp: float
        :param lpo_time: The lpo_time of this PollutionUploadData.  # noqa: E501
        :type lpo_time: float
        :param co2: The co2 of this PollutionUploadData.  # noqa: E501
        :type co2: float
        """
        self.swagger_types = {
            'in_temp': float,
            'out_temp': float,
            'lpo_time': float,
            'co2': float
        }

        self.attribute_map = {
            'in_temp': 'inTemp',
            'out_temp': 'outTemp',
            'lpo_time': 'LPOTime',
            'co2': 'CO2'
        }
        self._in_temp = in_temp
        self._out_temp = out_temp
        self._lpo_time = lpo_time
        self._co2 = co2

    @classmethod
    def from_dict(cls, dikt) -> 'PollutionUploadData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PollutionUploadData of this PollutionUploadData.  # noqa: E501
        :rtype: PollutionUploadData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def in_temp(self) -> float:
        """Gets the in_temp of this PollutionUploadData.


        :return: The in_temp of this PollutionUploadData.
        :rtype: float
        """
        return self._in_temp

    @in_temp.setter
    def in_temp(self, in_temp: float):
        """Sets the in_temp of this PollutionUploadData.


        :param in_temp: The in_temp of this PollutionUploadData.
        :type in_temp: float
        """

        self._in_temp = in_temp

    @property
    def out_temp(self) -> float:
        """Gets the out_temp of this PollutionUploadData.


        :return: The out_temp of this PollutionUploadData.
        :rtype: float
        """
        return self._out_temp

    @out_temp.setter
    def out_temp(self, out_temp: float):
        """Sets the out_temp of this PollutionUploadData.


        :param out_temp: The out_temp of this PollutionUploadData.
        :type out_temp: float
        """

        self._out_temp = out_temp

    @property
    def lpo_time(self) -> float:
        """Gets the lpo_time of this PollutionUploadData.


        :return: The lpo_time of this PollutionUploadData.
        :rtype: float
        """
        return self._lpo_time

    @lpo_time.setter
    def lpo_time(self, lpo_time: float):
        """Sets the lpo_time of this PollutionUploadData.


        :param lpo_time: The lpo_time of this PollutionUploadData.
        :type lpo_time: float
        """

        self._lpo_time = lpo_time

    @property
    def co2(self) -> float:
        """Gets the co2 of this PollutionUploadData.


        :return: The co2 of this PollutionUploadData.
        :rtype: float
        """
        return self._co2

    @co2.setter
    def co2(self, co2: float):
        """Sets the co2 of this PollutionUploadData.


        :param co2: The co2 of this PollutionUploadData.
        :type co2: float
        """

        self._co2 = co2
