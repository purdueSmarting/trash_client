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

ser = serial.Serial('/dev/ttyACM1', 9600, timeout=2)
ser.open

total_height = 68.0
while True:
    print "loop start"
    current_time = str(datetime.datetime.now())
    current_height = int(ser.readline())

    #How much is trash can filled
    percentage = (total_height - float(current_height)) / total_height *100 

    payload = {'time':current_time,'current_height':current_height,'percentage':percentage}
    jsonString = json.dumps(payload)
    print (jsonString)    
    requests.post('http://192.168.2.136:1235/trash', data=payload)
    print "request posted"
    time.sleep(2)
