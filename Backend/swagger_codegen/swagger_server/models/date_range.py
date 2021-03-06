# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DateRange(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, start_date: str=None, end_date: str=None):  # noqa: E501
        """DateRange - a model defined in Swagger

        :param start_date: The start_date of this DateRange.  # noqa: E501
        :type start_date: str
        :param end_date: The end_date of this DateRange.  # noqa: E501
        :type end_date: str
        """
        self.swagger_types = {
            'start_date': str,
            'end_date': str
        }

        self.attribute_map = {
            'start_date': 'startDate',
            'end_date': 'endDate'
        }
        self._start_date = start_date
        self._end_date = end_date

    @classmethod
    def from_dict(cls, dikt) -> 'DateRange':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DateRange of this DateRange.  # noqa: E501
        :rtype: DateRange
        """
        return util.deserialize_model(dikt, cls)

    @property
    def start_date(self) -> str:
        """Gets the start_date of this DateRange.

        Start date  # noqa: E501

        :return: The start_date of this DateRange.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: str):
        """Sets the start_date of this DateRange.

        Start date  # noqa: E501

        :param start_date: The start_date of this DateRange.
        :type start_date: str
        """

        self._start_date = start_date

    @property
    def end_date(self) -> str:
        """Gets the end_date of this DateRange.

        End date  # noqa: E501

        :return: The end_date of this DateRange.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: str):
        """Sets the end_date of this DateRange.

        End date  # noqa: E501

        :param end_date: The end_date of this DateRange.
        :type end_date: str
        """

        self._end_date = end_date
