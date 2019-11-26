#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2014 Roger Light <roger@atchoo.org>
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Distribution License v1.0
# which accompanies this distribution.
#
# The Eclipse Distribution License is available at
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    Roger Light - initial implementation

# This shows an example of using the publish.single helper function.
import sys
import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish
from gpiozero import Button
from time import sleep
from datetime import datetime

# adafruit i2c stuff imports
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# adafruit i2c stuff setup
# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)



auth = { 'username' : "ewarner77", 'password' : "my74bbug" } #setup for mqtt publishing and authentication
button = Button(25) #use gpio pin 25

def print_there(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()

def start_run():
    now=datetime.now()
    start_time=now.strftime("%H:%M:%S")
    print("run started @" + start_time)

while True:
    if button.is_pressed:
        publish.single("shop/cnc03/running", "1" , hostname="167.71.147.221", auth=auth)
        #print("Pressed")
    else:
        publish.single("shop/cnc03/running", "0" , hostname="167.71.147.221", auth=auth)
        #print("Released")

    print_there(10,20,("{:>5}\t{:>5.3f}".format(chan0.value, chan0.voltage)))
    print_there(12,20,("{:>5}\t{:>5.3f}".format(chan1.value, chan1.voltage)))
    
     
    button.when_pressed=start_run
    
    sleep(.25)

