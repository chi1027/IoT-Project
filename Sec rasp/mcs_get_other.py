import time
import http.client, urllib
import json
import RPi.GPIO as GPIO
import requests
import socket
import serial

deviceId = "DfgskicX" #109550172
deviceKey = "0WXK7SwuDx2Vp9Qc"
#deviceId = "D5Wu3e3g" 
#deviceKey = "DQ4P5W3mkcHIepq8"

host = "http://api.mediatek.com"
headers = {"Content-type": "application/json", "deviceKey": deviceKey}

def status(sensor):
    endpoint = "/mcs/v2/devices/" + deviceId + "/datachannels/" + sensor + "/datapoints"
    url = host + endpoint
    r = requests.get(url,headers=headers)
    value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
    return value

