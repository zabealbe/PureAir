import requests
import json

rows=-1
url=f"https://public.opendatasoft.com/api/records/1.0/search/?dataset=worldwide-pollution&rows={rows}"

records=[]

r = requests.get(url)

for row in r.json()["records"]:
    row["type"] = "Feature"
    row["properties"] = {
        "lpoTime": row["fields"]["value_pm5"]
    }
    del row["fields"]
    del row["datasetid"]
    del row["recordid"]
    del row["record_timestamp"]
    records.append(row)

data = {
    "type": "FeatureCollection",
    "features": records
}

with open("dataset.json", "w+") as f:
    json.dump(data, f, indent=4)
