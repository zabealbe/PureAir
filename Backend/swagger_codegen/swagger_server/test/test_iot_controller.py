# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.date_range import DateRange  # noqa: E501
from swagger_server.models.get_pollution_info_data import GetPollutionInfoData  # noqa: E501
from swagger_server.models.pollution_info import PollutionInfo  # noqa: E501
from swagger_server.models.pollution_upload_data import PollutionUploadData  # noqa: E501
from swagger_server.models.wi_fi_list_inner import WiFiListInner  # noqa: E501
from swagger_server.test import BaseTestCase


class TestIotController(BaseTestCase):
    """IotController integration test stubs"""

    def test_get_device_data(self):
        """Test case for get_device_data

        Get pollution info on your zone
        """
        body = DateRange()
        response = self.client.open(
            '/v1/iot/getDeviceData/{UUID}'.format(uuid=1.2),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_pollution_info(self):
        """Test case for get_pollution_info

        Get pollution info on your zone
        """
        body = GetPollutionInfoData()
        response = self.client.open(
            '/v1/iot/getPollutionInfo',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_device_position(self):
        """Test case for update_device_position

        Update Pollution Info for a zone
        """
        body = [WiFiListInner()]
        response = self.client.open(
            '/v1/iot/updateDevicePosition/{UUID}'.format(uuid=1.2),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_pollution_info(self):
        """Test case for update_pollution_info

        Update Pollution Info for a zone
        """
        body = PollutionUploadData()
        response = self.client.open(
            '/v1/iot/putDeviceData/{UUID}'.format(uuid=1.2),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
