from pymongo import MongoClient
import json
import time
import os
import random

os.getenv("MONGODB_URL")

client = MongoClient(os.getenv("MONGODB_URL"))

database = client["pureair_db"]
data_col = database["data"]
geo_col = database["geo"]

with open("dataset.json") as f:
    json_data = json.load(f)

uuid = 1
length = len(json_data["features"])

for feat in json_data["features"]:
    #coords = feat["geometry"]["coordinates"]
    data_col.insert_one({
        "UUID": uuid,
        "sensors": {
            "lpo_time": feat["properties"]["lpoTime"],
            "co2": random.randrange(400, 2000), # 400ppm typical outdoor, 1000 typical indoor, 2000 bad
            "in_temp": random.randrange(13, 28),
            "out_temp": random.randrange(0, 38)

        },
        "timestamp": int(time.time())
    })

    pos = {
            "UUID": uuid,
            "location": feat["geometry"],
            "accuracy": random.randrange(5000, 10000)
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

data_col.create_index([
    ("UUID", 1)
])
geo_col.create_index([
    ("UUID", 1),
])
geo_col.create_index([
    ("location", "2dsphere")
])