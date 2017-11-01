import RPi.GPIO as gpio
import time
import datetime
from threading import Timer
import threading
import json
import urllib2
import httplib as http
import requests

gpio.setmode(gpio.BCM)
  
trig = 13
echo = 19
  
print "start"

gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)

def printit():
    gpio.output(trig, False)
    time.sleep(0.5)
 
    gpio.output(trig, True)
    time.sleep(0.00001)
    gpio.output(trig, False)

    pulse_start=0
    pulse_end=0
 
    while gpio.input(echo) == 0 :  
        pulse_start = time.time()
 	
    while gpio.input(echo) == 1 :
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17000
    distance = round(distance, 2)

    wtime = datetime.datetime.now()
    ret = "Time: " + str(wtime) + " Distance: " + str(distance) + " cm"
    return ret
    
while 1:
    data = json.loads(json.dumps(printit()))
    print data
    r = requests.post('http://13.59.174.162:7579/trash', json={'data':data})
    #print r.text
    #r.close()
    time.sleep(10)
