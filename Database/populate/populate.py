from pymongo import MongoClient
import json
import requests
from datetime import datetime

client = MongoClient(   '192.168.1.102', # TODO: change this
                        username='root',
                        password='example',
                        authMechanism='SCRAM-SHA-256')

database = client["pureair_db"]
data_col = database["data"]
geo_col = database["geo"]

with open("Database/populate/dataset.json") as f:
    json_data = json.load(f)

uuid = 1
length = len(json_data["features"])

for feat in json_data["features"]:
    lpo = feat["properties"]["lpoTime"]
    #coords = feat["geometry"]["coordinates"]
    data_col.insert_one({
        "UUID": uuid,
        "sensors": {
            "LPOTime": lpo
        },
        "timestamp": datetime.now()
    })

    pos = {
            "UUID": uuid,
            "location": feat["geometry"],
            "accuracy": 10000
        }
    #geo_col.update(
    #    {"UUID": uuid},
    #    {"$set": 
    #        {"geoinfo": pos}
    #    }
    #)
    geo_col.insert_one(pos)

    print(int(100*uuid/length) ,uuid, "/", length)
    uuid += 1
