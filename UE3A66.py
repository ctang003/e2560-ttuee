import spidev
import time
import os
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM)

segments = (23,24,25,12,16,20,21)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)

digits = (4,17,27,22,5,6,13,19)

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)

num = {' ':(0,0,0,0,0,0,0),
       '0':(1,1,1,1,1,1,0), 
       '1':(0,1,1,0,0,0,0),
       '2':(1,1,0,1,1,0,1),
       '3':(1,1,1,1,0,0,1),
       '4':(0,1,1,0,0,1,1),
       '5':(1,0,1,1,0,1,1),
       '6':(1,0,1,1,1,1,1),
       '7':(1,1,1,0,0,0,0),
       '8':(1,1,1,1,1,1,1),
       '9':(1,1,1,1,0,1,1)}

spi=spidev.SpiDev()
spi.open(0,0)

voltChannel=0
currChannel=1
sleeptime=2

def getReading(channel):
    if channel>7 or channel<0:
        return -1
    adc=spi.xfer2([1,(8+channel)<<4,0])
    data=((adc[1]&3)<<8)+adc[2]
    return data

def convertvolt(data,places):
    volt=(data*5)/float(1023)
    volt=round(volt,places)
    return volt

while True:
    voltData=getReading(voltChannel)
    currData=getReading(currChannel)
    voltss=convertvolt(voltData,3)
    currss=convertvolt(currData,3)

     
    s = str(voltss)+str(currss)
    for digit in range(8):
         for loop in range(0,7):
             GPIO.output(segments[loop], num[s[digit]][loop])
                
                
                    
    GPIO.output(digits[digit],0)
    time.sleep(0.001)
    GPIO.output(digits[digit],1)
            
        

    
    
