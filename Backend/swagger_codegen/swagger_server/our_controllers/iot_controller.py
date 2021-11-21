from tinydb import TinyDB, Query
from datetime import datetime
import requests
import geopy.distance

db = TinyDB('/usr/src/app/db.json')
geo_db = TinyDB('/usr/src/app/location_db.json')
query = Query()

def get_pollution_info(body):
    res = db.search(query.UUID == 123)
    """
    coords_1 = (52.2296756, 21.0122287)
coords_2 = (52.406374, 16.9251681)

print geopy.distance.vincenty(coords_1, coords_2).km
"""
    return res


def put_device_data(body, uuid):
    db.insert({
        "UUID": uuid,
        "sensors": {
            "co2": body.co2,
            "in_temp": body.in_temp,
            "out_temp": body.out_temp,
            "lpo_time": body.lpo_time,
        },
        "timestamp": datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    })
    return "Data added"


def update_device_position(body, uuid):
    data_for_gmap_api = {
        "homeMobileCountryCode": 310,
        "homeMobileNetworkCode": 410,
        "radioType": "gsm",
        "carrier": "Vodafone",
        "considerIp": True,
        "cellTowers": [

        ],
        "wifiAccessPoints": [
            {
                "macAddress": "88:78:73:84:B9:C6",
                "signalStrength": -43,
                "signalToNoiseRatio": 0,
                "channel": 11,
                "age": 0
            }
        ]
    }
    endpoint = "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyC55fOO_Y6J7hmy-zfHqMCFRMBOZl5ZSJc"
    r = requests.post(endpoint, json=data_for_gmap_api)
    pos = r.json()

    geo_db.update({"geoinfo", pos}, query.UUID == uuid)

    print(geo_db.all())


def get_device_data(body, uuid):
    return None