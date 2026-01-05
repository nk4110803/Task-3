from fastapi import FastAPI
import json

app = FastAPI()
FILE_PATH = "data.json"

@app.post("/json_payloud")
async def json_payloud(payload: dict):
    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    data.append(payload)
    with open(FILE_PATH, "w") as file:
        json.dump(data, file)
    return {"message": "Payload saved successfully"}

@app.get("/get_json")
async def get_json():
    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data[-10:]
 