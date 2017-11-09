#!/usr/bin/python
# coding=utf8
import time
import datetime
from threading import Timer
import threading
import json
import urllib2
import httplib as http
import requests
import serial

ser = serial.Serial('/dev/ttyACM1', 9600)
ser.open

total_height = 68.0
while 1:
    current_height = ser.readline()
    current_time = datetime.datetime.now()

    #How much is trash can filled
    percentage = (total_height - float(current_height)) / total_height *100 
    
    data = "Time:"+ str(current_time) + "Distance from trash: " + str(current_height) + "Percentage: " + str(int(percentage)) + "%"
    data = json.loads(json.dumps(data))
    print data
    r = requests.post('http://192.168.2.136:7579/trash', json={'data':data})
    time.sleep(2)
