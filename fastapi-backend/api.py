from fastapi import FastAPI

app = FastAPI()

asset = {
    'XY00001':{
        # "Id" : "XY00001",
        "Level" : 4,
        "Battery" : 100,
        "Signal" : 24,
        "Temp" : 24,
        "Humidity" : 24,
        "Pressure" : 24,
        "Altitude" : 24,
        "Data frequency" : 24,
    },
    'XY00002':{
        # "Id" : "XY00002",
        "Level" : 120,
        "Battery" : 19,
        "Signal" : 27,
        "Temp" : 25,
        "Humidity" : 44,
        "Pressure" : 34,
        "Altitude" : 64,
        "Data frequency" : 64,
    },
    'XY00003':{
        # "Id" : "XY00003",
        "Level" : 130,
        "Battery" : 38,
        "Signal" : 54,
        "Temp" : 64,
        "Humidity" : 34,
        "Pressure" : 74,
        "Altitude" : 94,
        "Data frequency" : 14,
    },
    'XY00004':{
        # "Id" : "XY00004",
        "Level" : 140,
        "Battery" : 48,
        "Signal" : 53,
        "Temp" : 94,
        "Humidity" : 38,
        "Pressure" : 58,
        "Altitude" : 22,
        "Data frequency" : 85,
    },
    'XY00005':{
        # "Id" : "XY00005",
        "Level" : 150,
        "Battery" : 58,
        "Signal" : 54,
        "Temp" : 33,
        "Humidity" : 38,
        "Pressure" : 45,
        "Altitude" : 91,
        "Data frequency" : 20,
    }
}

assetgraph = {
    'XY00001': [
        {"level": 40, "Timestamp": "4/18/2024 1:12 PM"},
        {"level": 40, "Timestamp": "4/18/2024 1:13 PM"},
        {"level": 40, "Timestamp": "4/18/2024 1:14 PM"},
        {"level": 40, "Timestamp": "4/18/2024 1:15 PM"},
        {"level": 40, "Timestamp": "4/18/2024 1:16 PM"},
        {"level": 40, "Timestamp": "4/18/2024 1:17 PM"},
        {"level": 40, "Timestamp": "4/18/2024 1:18 PM"},
        {"level": 40, "Timestamp": "4/18/2024 1:19 PM"},
        {"level": 40, "Timestamp": "4/18/2024 1:20 PM"},
        {"level": 40, "Timestamp": "4/18/2024 1:21 PM"},
        {"level": 40, "Timestamp": "4/18/2024 1:22 PM"},
        {"level": 40, "Timestamp": "4/18/2024 1:23 PM"},
        {"level": 40, "Timestamp": "4/18/2024 1:24 PM"},
        {"level": 40, "Timestamp": "4/18/2024 1:25 PM"},
        {"level": 40, "Timestamp": "4/18/2024 1:26 PM"},
        {"level": 40, "Timestamp": "4/18/2024 1:27 PM"},
        {"level": 40, "Timestamp": "4/18/2024 1:28 PM"},
        {"level": 40, "Timestamp": "4/18/2024 1:29 PM"},
        {"level": 40, "Timestamp": "4/18/2024 1:30 PM"},
        {"level": 40, "Timestamp": "4/18/2024 1:31 PM"},
        {"level": 40, "Timestamp": "4/18/2024 1:32 PM"}
    ],
}


@app.get("/user")
def user():
    return {
        "name" : "john doe"
    }
    
@app.get("/asset/{id}")
def get_asset(id: str):
    if id in asset:
        return asset[id]
    return {"error": "Asset not found"}, 404

@app.get("/graph/{id}")
def get_asset(id: str):
    if id in assetgraph:
        return assetgraph[id]
    return {"error": "Asset graph not found"}, 404