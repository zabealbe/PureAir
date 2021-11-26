import connexion
import six

from swagger_server.models.date_range import DateRange  # noqa: E501
from swagger_server.models.get_pollution_info_data import GetPollutionInfoData  # noqa: E501
from swagger_server.models.pollution_info import PollutionInfo  # noqa: E501
from swagger_server.models.pollution_upload_data import PollutionUploadData  # noqa: E501
from swagger_server.models.wi_fi_list_inner import WiFiListInner  # noqa: E501
from swagger_server import util
from swagger_server.our_controllers import iot_controller

def get_device_data(body, uuid):  # noqa: E501
    """Get pollution info on your zone

     # noqa: E501

    :param body: Optional description in *Markdown*
    :type body: dict | bytes
    :param uuid: UUID of the device
    :type uuid: float

    :rtype: List[PollutionInfo]
    """
    if connexion.request.is_json:
        body = DateRange.from_dict(connexion.request.get_json())  # noqa: E501

    status, data = iot_controller.get_device_data(body, uuid)
    if status == 200:
        return data
    else:
        return [], 404


def get_pollution_info(body):  # noqa: E501
    """Get pollution info on your zone

     # noqa: E501

    :param body: Optional description in *Markdown*
    :type body: dict | bytes

    :rtype: List[PollutionInfo]
    """
    if connexion.request.is_json:
        body = GetPollutionInfoData.from_dict(connexion.request.get_json())  # noqa: E501
    data = iot_controller.get_pollution_info(body)
    return data


def update_device_position(body, uuid):  # noqa: E501
    """Update Pollution Info for a zone

     # noqa: E501

    :param body: Optional description in *Markdown*
    :type body: list | bytes
    :param uuid: UUID of the device
    :type uuid: float

    :rtype: List[PollutionInfo]
    """
    if connexion.request.is_json:
        body = [WiFiListInner.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return iot_controller.update_device_position(body, uuid)


def put_device_data(body, uuid):  # noqa: E501
    """Update Pollution Info for a zone

     # noqa: E501

    :param body: Optional description in *Markdown*
    :type body: dict | bytes
    :param uuid: UUID of the device
    :type uuid: float

    :rtype: List[PollutionInfo]
    """
    if connexion.request.is_json:
        body = PollutionUploadData.from_dict(connexion.request.get_json())  # noqa: E501
    return iot_controller.put_device_data(body, uuid)
