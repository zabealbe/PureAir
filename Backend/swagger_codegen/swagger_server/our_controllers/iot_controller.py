from pymongo import MongoClient
from datetime import datetime
import requests
import geopy.distance

client = MongoClient(   '192.168.1.102', # TODO: change this
                        username='root',
                        password='example',
                        authMechanism='SCRAM-SHA-256')

database = client["pureair_db"]
data_col = database["data"]
geo_col = database["geo"]


def get_pollution_info(body):
    ret = []
    for x in geo_col.find():
        data = x["geoinfo"]["location"]
        coords = (data["lat"], data["lng"])
        dst = geopy.distance.distance(coords, (body.lat, body.lng)).m

        if dst < body.range:
            lpo_time = data_col.find({"UUID": x["UUID"]})\
            .limit(1)\
            .sort({"$natural":"-1"})
            ret.append({
                "geoinfo": x["geoinfo"],
                "LPOTime": lpo_time
            })
    """
    coords_1 = (52.2296756, 21.0122287)
coords_2 = (52.406374, 16.9251681)

print geopy.distance.vincenty(coords_1, coords_2).km
"""
    return ret


def put_device_data(body, uuid):
    data_col.insert_one({
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

    geo_col.update(
        {"UUID": uuid},
        {"$set":
             {"geoinfo": pos}
         },
        True
    )

    return "Position updated"


def get_device_data(body, uuid):
    return None