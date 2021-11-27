from pymongo import MongoClient
from datetime import datetime
import requests
import geopy.distance

client = MongoClient(
    '192.168.1.102',
    username='root',
    password='example',
    authMechanism='SCRAM-SHA-256'
)

database = client["pureair_db"]
data_col = database["data"]
geo_col = database["geo"]


def get_pollution_info(body):
    ret = geo_col.find({
        "location": {
            "$near": {
                "$geometry": {
                    "type": "Point",
                    "coordinates": [body.lng, body.lat],
                },
                "$maxDistance": body.range,
            }
        }
    },
   {"_id": False})

    geojson = {
        "features": []
    }
    for r in list(ret):
        geojson["features"].append({
            "geometry": r["location"],
            "type": "Feature"
        })

    return geojson


def put_device_data(body, uuid):
    data_col.insert_one({
        "UUID": uuid,
        "sensors": {
            "co2": body.co2,
            "in_temp": body.in_temp,
            "out_temp": body.out_temp,
            "lpo_time": body.lpo_time,
        },
        "timestamp": datetime.now() #datetime.today().strftime("%Y-%m-%d %H:%M:%S")
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
             {"location": {
                 "type": "Point",
                 "coordinates": [
                    pos["location"]["lng"],
                    pos["location"]["lat"]
                 ]
             },
             "accuracy": pos["accuracy"]}
         },
        True
    )

    return "Position updated"


def get_device_data(body, uuid):
    """
    start = datetime.strptime(body.start_date, "%Y-%m-%d %H:%M:%S")
end = datetime.strptime(body.end_date, "%Y-%m-%d %H:%M:%S")
data_col.find({"UUID": uuid, "timestamp": {"$lt": end, "$gte": start}})
    """
    start = datetime.strptime(body.start_date, "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(body.end_date, "%Y-%m-%d %H:%M:%S")

    out = list(data_col.find({"UUID": uuid,
                              "timestamp": {
                                  "$lt": end,
                                  "$gte": start}
                              }, {"_id": False}))
    if len(out) == 0 and len(list(data_col.find({"UUID": uuid}))) == 0:
        return {"error": "device not found"}, 404
    else:
        return {"status": "success", "data": out}, 200

def get_home_assistant(uuid):
    ret = data_col.find({"UUID": uuid}, {"_id": False})\
        .sort("timestamp", -1).limit(1)
    return list(ret)[0]["sensors"]