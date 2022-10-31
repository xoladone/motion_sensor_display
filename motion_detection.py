#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import os

SENSOR_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

def display_callback(channel):
    # print message for debugging
    # print('Motion detected.')
    os.system("xset -display :0.0 dpms force on")

try:
    GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=display_callback)
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    print "Finis."
GPIO.cleanup()
