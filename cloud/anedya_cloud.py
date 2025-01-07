import json
import requests
import time
import uuid
import streamlit as st
import pandas as pd
import pytz  # Add this import for time zone conversion


class Anedya:
    def __init__(self, API_KEY) -> None:
        if API_KEY == "":
            st.error("Please config a valid NODE ID and API key.")

        elif API_KEY == "":
            st.error("Please config a valid API key.")
        else:
             self.API_KEY = API_KEY
             self.http_session = requests.Session()
    
    def get_deviceStatus(self, nodeId: str) -> list:
        return anedya_getDeviceStatus(self.API_KEY, nodeId, self.http_session)
    
    def get_latestData(self, variable_identifier: str, nodeId: str) -> list:
        return get_latestData(variable_identifier, nodeId, self.API_KEY, self.http_session)
    
    def get_aggregatedData(self, variable_identifier: str, from_: int, to: int, aggregation_interval_in_minutes: float, nodeId: str) -> list:
        return anedya_getData(variable_identifier, from_, to, aggregation_interval_in_minutes, nodeId, self.API_KEY, self.http_session)
    
    

@st.cache_data(ttl=9, show_spinner=False)
def get_latestData(param_variable_identifier: str, nodeId: str, apiKey: str, http_session) -> list:

    url = "https://api.anedya.io/v1/data/latest"
    apiKey_in_formate = "Bearer " + apiKey

    payload = json.dumps({"nodes": [nodeId], "variable": param_variable_identifier})
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": apiKey_in_formate,
    }

    # response = requests.request("POST", url, headers=headers, data=payload)
    response=http_session.request("POST", url, headers=headers, data=payload)
    response_message = response.text
    if response.status_code==200:
        # print(response_message)
        data = json.loads(response_message).get("data")
        if data=={} or data==None:
            print(f"No Data found")
            return[None,None]
        else:
            data=data[nodeId].get("value")
            timestamp = json.loads(response_message).get("data")[nodeId].get("timestamp")
            # print(data, timestamp)
            return [data, timestamp]
    else:
        st.error("Get LatestData API failed")
        return [None,None]

def anedya_getData(
    param_variable_identifier: str,
    param_from: int,
    param_to: int,
    param_aggregation_interval_in_minutes: float,
    nodeId: str,
    apiKey: str,
    http_session,
) -> list:
    url = "https://api.anedya.io/v1/aggregates/variable/byTime"
    apiKey_in_formate = "Bearer " + apiKey

    payload = json.dumps(
        {
            "variable": param_variable_identifier,
            "from": param_from,
            "to": param_to,
            "config": {
                "aggregation": {"compute": "avg", "forEachNode": True},
                "interval": {
                    "measure": "minute",
                    "interval": param_aggregation_interval_in_minutes,
                },
                "responseOptions": {"timezone": "UTC"},
                "filter": {"nodes": [nodeId], "type": "include"},
            },
        }
    )
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": apiKey_in_formate,
    }

    response = http_session.request("POST", url, headers=headers, data=payload)
    response_message = response.text
    res_code = response.status_code
    return [response_message, res_code]


@st.cache_data(ttl=40, show_spinner=False)
def anedya_getDeviceStatus(apiKey, nodeId, http_session):
    url = "https://api.anedya.io/v1/health/status"
    apiKey_in_formate = "Bearer " + apiKey

    payload = json.dumps({"nodes": [nodeId], "lastContactThreshold": 120})
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": apiKey_in_formate,
    }

    response =http_session.request("POST", url, headers=headers, data=payload)
    responseMessage = response.text

    errorCode = json.loads(responseMessage).get("errcode")
    if errorCode == 0:
        device_status = json.loads(responseMessage).get("data")[nodeId].get("online")
        value = [device_status, 1]
    else:
        # print(responseMessage)
        # st.write("No previous value!!")
        value = [False, -1]

    return value

# def get_nodeList():
#     url = "https://api.anedya.io/v1/node/list"
#     apiKey_in_formate = "Bearer " + apiKey

#     headers = {
#         "Content-Type": "application/json",
#         "Accept": "application/json",
#         "Authorization": apiKey_in_formate,
#     }

#     payload = json.dumps({
#         "limit" : 100,
#         "offset":0,
#         "order":"asc"
#     })

#     response = http_session.request("POST", url, headers=headers, data=payload)
#     response_message = response.text
#     st.write(response_message)