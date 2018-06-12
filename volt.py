#!/usr/bin/env python
# author: kevin Hung
import time, RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#seven segment LEDs
segments = (35,23,12,13,21,33,10,11)
for segment in segments:
	GPIO.setup(segment, GPIO.OUT)
	GPIO.output(segment, 0)
#seven segment digits
#Digit 1
GPIO.setup(32, GPIO.OUT)
GPIO.output(32, 0) #Off initially
#Digit 2
GPIO.setup(31, GPIO.OUT)
GPIO.output(31, 0) #Off initially
#Digit 3
GPIO.setup(29, GPIO.OUT)
GPIO.output(29, 0) #Off initially
#Digit 4
GPIO.setup(8, GPIO.OUT)
GPIO.output(8, 0) #Off initially

null = [1,1,1,1,1,1,1]
zero = [0,0,0,0,0,0,1]
one = [1,0,0,1,1,1,1]
two = [0,0,1,0,0,1,0]
three = [0,0,0,0,1,1,0]
four = [1,0,0,1,1,0,0]
five = [0,1,0,0,1,0,0]
six = [0,1,0,0,0,0,0]
seven = [0,0,0,1,1,1,1]
eight = [0,0,0,0,0,0,0]
nine = [0,0,0,0,1,0,0]
def print_segment(charector):
    if charector == 1:
        for i in range(7):
            GPIO.output(segments[i], one[i])
    if charector == 2:
        for i in range(7):
            GPIO.output(segments[i], two[i])
    if charector == 3:
        for i in range(7):
            GPIO.output(segments[i], three[i])
    if charector == 4:
        for i in range(7):
            GPIO.output(segments[i], four[i])
    if charector == 5:
        for i in range(7):
            GPIO.output(segments[i], five[i])
    if charector == 6:
        for i in range(7):
            GPIO.output(segments[i], six[i])
    if charector == 7:
        for i in range(7):
            GPIO.output(segments[i], seven[i])
    if charector == 8:
        for i in range(7):
            GPIO.output(segments[i], eight[i])
    if charector == 9:
        for i in range(7):
            GPIO.output(segments[i], nine[i])
    if charector == 0:
        for i in range(7):
            GPIO.output(segments[i], zero[i])
    return;
#ADC0804
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.IN)
GPIO.setup(18,GPIO.IN)
GPIO.setup(22,GPIO.IN)
GPIO.setup(7,GPIO.IN)
GPIO.setup(3,GPIO.IN)
GPIO.setup(5,GPIO.IN)
GPIO.setup(24,GPIO.IN)
GPIO.setup(19,GPIO.IN)
GPIO.setup(26,GPIO.IN)
intr=GPIO.input(16)

try:
	while True:
		GPIO.output(15,GPIO.LOW)
		GPIO.output(15,GPIO.HIGH)
		a0 = GPIO.input(18)
		a1 = GPIO.input(22)
		a2 = GPIO.input(7)
		a3 = GPIO.input(3)
		a4 = GPIO.input(5)
		a5 = GPIO.input(24)
		a6 = GPIO.input(19)
		a7 = GPIO.input(26)
		total=a0+(a1*2)+(a2*4)+(a3*8)+(a4*16)+(a5*32)+(a6*64)+(a7*128)

		y=round(((total/255.0)*25)*1000,3)
		y1=int(y)
		print(y1)

		n1=y1/1000

		n2=(y1%1000)/100
		n3=(y1%100)/10
		n4=(y1%10)

		print "the voltage is","[",y1/1000.0,"]"

		delay_time = 0.0085 #delay to create virtual effect
		GPIO.output(32, 1) #Turn on Digit One
    		print_segment (n1) #Print h1 on segment
		GPIO.output(11, 0) #Display point On
    		time.sleep(delay_time)
		GPIO.output(11, 1) #Display point On
    		GPIO.output(32, 0) #Turn off Digit One

    		GPIO.output(31, 1) #Turn on Digit One
    		print_segment (n2) #Print h1 on segment
    		time.sleep(delay_time)
    		GPIO.output(31, 0) #Turn off Digit One

    		GPIO.output(29, 1) #Turn on Digit One
    		print_segment (n3) #Print h1 on segment
    		time.sleep(delay_time)
    		GPIO.output(29, 0) #Turn off Digit One

    		GPIO.output(8, 1) #Turn on Digit One
    		print_segment (n4) #Print h1 on segment
    		time.sleep(delay_time)
    		GPIO.output(8, 0) #Turn off Digit One

    		#time.sleep(1)
finally:
	GPIO.cleanup()
