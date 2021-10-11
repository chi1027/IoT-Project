import time
import http.client, urllib
import json
import requests
import socket
import serial
#import i2c_lcd
#import mcs_ldr
#deviceId = "DweNqI3l" #109550172
#deviceKey = "aNyIGaL6GdsJZxco"
#deviceId = "DfgskicX" 
#deviceKey = "0WXK7SwuDx2Vp9Qc"
deviceId = "D5Wu3e3g" 
deviceKey = "DQ4P5W3mkcHIepq8"

# Set MediaTek Cloud Sand box (MCS) Connection
def post_to_mcs(mode, data):
    payload= {"datapoints":[{"dataChnId": mode,"values":{"value":str(data)}}]}
    headers = {"Content-type": "application/json", "deviceKey": deviceKey}
    not_connected = 1
    while (not_connected):
        try:
            conn = http.client.HTTPConnection("api.mediatek.com:80")
            conn.connect()
            not_connected = 0
        except (http.client.HTTPException, socket.error) as ex:
            print ("Error: %s" % ex)
        time.sleep(1) # sleep 10 seconds
        conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints", json.dumps(payload), headers)
        response = conn.getresponse()
        print( response.status, response.reason,# json.dumps(payload), 
        time.strftime("%c"))
        data = response.read()
        conn.close()


    
    