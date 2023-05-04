from fastapi import FastAPI, Request, Response
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware
import redis
import requests
import json

app = FastAPI()

pool = redis.ConnectionPool(
    host='localhost', port=6379, db=0, decode_responses=True)
redis = redis.Redis(connection_pool=pool)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

busy_object = {"state": "busy"}
open_object = {"state": "open"}

@app.post("/startTest/")
async def runTest(data: Dict):
    print(getStmState())
    if getStmState() == "busy":
        return busy_object
    else:
        redis.set("stm32:state", "busy")
        print("before request")
        print(data)
        # Forward the request to the Django backend
        headers = {"Content-Type": "application/json"}
        resp = requests.post(f'http://localhost:8000/api/wrfram/',
                                   json=data,
                                   headers=headers)
        #print(resp.json())
        return resp.json()
        #req = requests.get(f'http://localhost:8000/api/wrfram')
        #print(req)
        #payload = req.json()
        #return payload


@app.get("/getStmState")
async def getState():
    req = requests.get('http://localhost:8000/api/getStmState')
    payload = req.json()
    return payload


@app.get("/getDevice")
async def getDevice():
    if getStmState() == "busy":
        data = [{
            'id': 123,
            'name': "stm32 hc",
            'ExternalMemory': "fram hc",
            'is_ctive': True,
        }]
        return data[0]
    else:
        print("sed request /getDevice")
        req = requests.get('http://localhost:8000/api/getDevice')
        payload = req.json()
        return payload[0]

def getStmState():
    print("in backend server getStmSate -- fetch from ")
    return redis.get("stm32:state")
  
@app.post("/testProgress/")
async def get_data(body: Dict):
    print("/testProgress")
    print(body["id"])
    data = redis.get("testOperation:"+str(body["id"])+":progress")
    print(data)
    return {"progress": data}
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return {"data": data}
