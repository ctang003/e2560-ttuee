import RPi.GPIO as IO        # calling for header file which helps us use GPIO’s of PI
import RPi.GPIO as GPIO
import time                          # calling for time to provide delays in program3
IO.setwarnings(False)         # do not show any warnings
x=1
b0 =0                                    # integers for storing 8 bits
x1=0
x2=0
x3=0
x4=0
b1 =0
b2 =0
b3 =0
b4 =0
b5 =0
b6 =0
b7 =0
IO.setmode (IO.BCM)            # programming the GPIO by BCM pin numbers. (like PIN29 as‘GPIO5’)
IO.setup(4,IO.IN)                    # initialize GPIO Pins as input
IO.setup(17,IO.IN)
IO.setup(27,IO.IN)
IO.setup(22,IO.IN)
IO.setup(5,IO.IN)
IO.setup(6,IO.IN)
IO.setup(13,IO.IN)
IO.setup(19,IO.IN)

IO.setup(8,IO.OUT)
IO.setup(21,IO.OUT)
IO.setup(20,IO.OUT)
IO.setup(16,IO.OUT)
IO.setup(12,IO.OUT)
IO.setup(7,IO.OUT)
IO.setup(25,IO.OUT)
IO.setup(15,IO.OUT)
IO.setup(14,IO.OUT)
IO.setup(23,IO.OUT)
IO.setup(18,IO.OUT)
IO.setup(24,IO.OUT)


while 1:                                               # execute loop forever
    if IO.input(19) == True:
        time.sleep(0.001)
        if IO.input(19) == True:
            b7=1                                       # if pin19 is high bit7 is true
    if IO.input(13) == True:
        time.sleep(0.001)
        if IO.input(13) == True:
            b6=1                                      # if pin13 is high bit6 is true
    if IO.input(6) == True:
        time.sleep(0.001)
        if IO.input(6) == True:
            b5=1                                      # if pin6 is high bit5 is true
    if IO.input(5) == True:
        time.sleep(0.001)
        if IO.input(5) == True:
            b4=1                                     # if pin5 is high bit4 is true
    if IO.input(22) == True:
        time.sleep(0.001)
        if IO.input(22) == True:
            b3=1                                     # if pin22 is high bit3 is true
    if IO.input(27) == True:
        time.sleep(0.001)
        if IO.input(27) == True:
            b2=1                                    # if pin27 is high bit2 is true
    if IO.input(17) == True:
       time.sleep(0.001)
       if IO.input(17) == True:
            b1=1                                    # if pin17 is high bit1 is true
    if IO.input(4) == True:
        time.sleep(0.001)
        if IO.input(4) == True:
            b0=1 # if pin4 is high bit0 is true
    
    x = (1*b0)+(2*b1)
    x = x+(4*b2)+(8*b3)
    x = x+(16*b4)+(32*b5)
    x = x+(64*b6)+(128*b7)                    # representing the bit values from LSB to MSB
    print ( x*0.0931213873)# print the ADC value
    #print (((x*16.83/0.1986) -(x*16.83/0.1986 % 1000))/1000)
    x1 = ((x*93.1213873) -(x*93.1213873 % 1000))/1000
    time.sleep(0.001) 
    if x1 == 0:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,False)
            IO.output(15,False)
            IO.output(14,False)
            IO.output(23,False)
            IO.output(18,False)
            IO.output(24,True)
            IO.output(21,True)
            IO.output(7,False)
            IO.output(12,False)
            IO.output(25,False)
    if x1 == 1:

            IO.output(8,False)
            IO.output(20,True)
            IO.output(16,True)
            IO.output(15,True)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,False)
            IO.output(24,True)
            IO.output(21,True)
            IO.output(7,False)
            IO.output(12,False)
            IO.output(25,False)
    if x1 == 2:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,True)
            IO.output(15,False)
            IO.output(14,False)
            IO.output(23,True)
            IO.output(18,False)
            IO.output(24,False)
            IO.output(21,True)
            IO.output(7,False)
            IO.output(12,False)
            IO.output(25,False)
    if x1 == 3:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,True)
            IO.output(15,False)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,False)
            IO.output(24,False)
            IO.output(21,True)
            IO.output(7,False)
            IO.output(12,False)
            IO.output(25,False)
    if x1 == 4:

            IO.output(8,False)
            IO.output(20,True)
            IO.output(16,False)
            IO.output(15,True)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,False)
            IO.output(24,False)
            IO.output(21,True)
            IO.output(7,False)
            IO.output(12,False)
            IO.output(25,False)
    if x1 == 5:

            IO.output(8,True)
            IO.output(20,False)
            IO.output(16,False)
            IO.output(15,False)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,False)
            IO.output(24,False)
            IO.output(21,True)
            IO.output(7,False)
            IO.output(12,False)
            IO.output(25,False)
    if x1 == 6:

            IO.output(8,True)
            IO.output(20,False)
            IO.output(16,False)
            IO.output(15,False)
            IO.output(14,False)
            IO.output(23,False)
            IO.output(18,False)
            IO.output(24,False)
            IO.output(21,True)
            IO.output(7,False)
            IO.output(12,False)
            IO.output(25,False)
    if x1 == 7:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,True)
            IO.output(15,True)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,False)
            IO.output(24,True)
            IO.output(21,True)
            IO.output(7,False)
            IO.output(12,False)
            IO.output(25,False)
    if x1 == 8:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,False)
            IO.output(15,False)
            IO.output(14,False)
            IO.output(23,False)
            IO.output(18,False)
            IO.output(24,False)
            IO.output(21,True)
            IO.output(7,False)
            IO.output(12,False)
            IO.output(25,False)
    if x1 == 9:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,False)
            IO.output(15,False)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,False)
            IO.output(24,False)
            IO.output(21,True)
            IO.output(7,False)
            IO.output(12,False)
            IO.output(25,False)

    x1 = ((x*93.1213873% 1000) -(x*93.1213873 % 100))/100
    #print (((x*16.83/0.1986% 1000) -(x*16.83/0.1986 % 100))/100)
    time.sleep(0.001) 
    if x1 == 0:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,False)
            IO.output(15,False)
            IO.output(14,False)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,True)
            IO.output(7,True)
            IO.output(21,False)
            IO.output(12,False)
            IO.output(25,False)
    if x1 == 1:

            IO.output(8,False)
            IO.output(20,True)
            IO.output(16,True)
            IO.output(15,True)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,True)
            IO.output(7,True)
            IO.output(21,False)
            IO.output(12,False)
            IO.output(25,False)
    if x1 == 2:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,True)
            IO.output(15,False)
            IO.output(14,False)
            IO.output(23,True)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(7,True)
            IO.output(21,False)
            IO.output(12,False)
            IO.output(25,False)
    if x1 == 3:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,True)
            IO.output(15,False)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(7,True)
            IO.output(21,False)
            IO.output(12,False)
            IO.output(25,False)
    if x1 == 4:

            IO.output(8,False)
            IO.output(20,True)
            IO.output(16,False)
            IO.output(15,True)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(7,True)
            IO.output(21,False)
            IO.output(12,False)
            IO.output(25,False)
    if x1 == 5:

            IO.output(8,True)
            IO.output(20,False)
            IO.output(16,False)
            IO.output(15,False)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(7,True)
            IO.output(21,False)
            IO.output(12,False)
            IO.output(25,False)
    if x1 == 6:

            IO.output(8,True)
            IO.output(20,False)
            IO.output(16,False)
            IO.output(15,False)
            IO.output(14,False)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(7,True)
            IO.output(21,False)
            IO.output(12,False)
            IO.output(25,False)
    if x1 == 7:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,True)
            IO.output(15,True)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,True)
            IO.output(7,True)
            IO.output(21,False)
            IO.output(12,False)
            IO.output(25,False)
    if x1 == 8:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,False)
            IO.output(15,False)
            IO.output(14,False)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(7,True)
            IO.output(21,False)
            IO.output(12,False)
            IO.output(25,False)
    if x1 == 9:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,False)
            IO.output(15,False)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(7,True)
            IO.output(21,False)
            IO.output(12,False)
            IO.output(25,False)

    x1 = ((x*93.1213873% 100) -(x*93.1213873% 10))/10
    time.sleep(0.001) 
    if x1 == 0:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,False)
            IO.output(15,False)
            IO.output(14,False)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,True)
            IO.output(12,True)
            IO.output(7,False)
            IO.output(21,False)
            IO.output(25,False)
    if x1 == 1:

            IO.output(8,False)
            IO.output(20,True)
            IO.output(16,True)
            IO.output(15,True)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,True)
            IO.output(12,True)
            IO.output(7,False)
            IO.output(21,False)
            IO.output(25,False)
    if x1 == 2:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,True)
            IO.output(15,False)
            IO.output(14,False)
            IO.output(23,True)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(12,True)
            IO.output(7,False)
            IO.output(21,False)
            IO.output(25,False)
    if x1 == 3:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,True)
            IO.output(15,False)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(12,True)
            IO.output(7,False)
            IO.output(21,False)
            IO.output(25,False)
    if x1 == 4:

            IO.output(8,False)
            IO.output(20,True)
            IO.output(16,False)
            IO.output(15,True)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(12,True)
            IO.output(7,False)
            IO.output(21,False)
            IO.output(25,False)
    if x1 == 5:

            IO.output(8,True)
            IO.output(20,False)
            IO.output(16,False)
            IO.output(15,False)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(12,True)
            IO.output(7,False)
            IO.output(21,False)
            IO.output(25,False)
    if x1 == 6:

            IO.output(8,True)
            IO.output(20,False)
            IO.output(16,False)
            IO.output(15,False)
            IO.output(14,False)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(12,True)
            IO.output(7,False)
            IO.output(21,False)
            IO.output(25,False)
    if x1 == 7:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,True)
            IO.output(15,True)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,True)
            IO.output(12,True)
            IO.output(7,False)
            IO.output(21,False)
            IO.output(25,False)
    if x1 == 8:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,False)
            IO.output(15,False)
            IO.output(14,False)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(12,True)
            IO.output(7,False)
            IO.output(21,False)
            IO.output(25,False)
    if x1 == 9:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,False)
            IO.output(15,False)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(12,True)
            IO.output(7,False)
            IO.output(21,False)
            IO.output(25,False)

    x1 = ((x*93.1213873% 10) -(x*93.1213873 % 1))
    
    time.sleep(0.001) 
    if x1 == 0:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,False)
            IO.output(15,False)
            IO.output(14,False)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,True)
            IO.output(25,True)
            IO.output(7,False)
            IO.output(12,False)
            IO.output(21,False)
    if x1 == 1:

            IO.output(8,False)
            IO.output(20,True)
            IO.output(16,True)
            IO.output(15,True)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,True)
            IO.output(25,True)
            IO.output(7,False)
            IO.output(12,False)
            IO.output(21,False)
    if x1 == 2:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,True)
            IO.output(15,False)
            IO.output(14,False)
            IO.output(23,True)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(25,True)
            IO.output(7,False)
            IO.output(12,False)
            IO.output(21,False)
    if x1 == 3:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,True)
            IO.output(15,False)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(25,True)
            IO.output(7,False)
            IO.output(12,False)
            IO.output(21,False)
    if x1 == 4:

            IO.output(8,False)
            IO.output(20,True)
            IO.output(16,False)
            IO.output(15,True)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(25,True)
            IO.output(7,False)
            IO.output(12,False)
            IO.output(21,False)
    if x1 == 5:

            IO.output(8,True)
            IO.output(20,False)
            IO.output(16,False)
            IO.output(15,False)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(25,True)
            IO.output(7,False)
            IO.output(12,False)
            IO.output(21,False)
    if x1 == 6:

            IO.output(8,True)
            IO.output(20,False)
            IO.output(16,False)
            IO.output(15,False)
            IO.output(14,False)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(25,True)
            IO.output(7,False)
            IO.output(12,False)
            IO.output(21,False)
    if x1 == 7:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,True)
            IO.output(15,True)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,True)
            IO.output(25,True)
            IO.output(7,False)
            IO.output(12,False)
            IO.output(21,False)
    if x1 == 8:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,False)
            IO.output(15,False)
            IO.output(14,False)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(25,True)
            IO.output(7,False)
            IO.output(12,False)
            IO.output(21,False)
    if x1 == 9:

            IO.output(8,False)
            IO.output(20,False)
            IO.output(16,False)
            IO.output(15,False)
            IO.output(14,True)
            IO.output(23,False)
            IO.output(18,True)
            IO.output(24,False)
            IO.output(25,True)
            IO.output(7,False)
            IO.output(12,False)
            IO.output(21,False)

    b0=b1=b2=b3=b4=b5=b6=b7=0        # reset values
    time.sleep(0.01)                                   # wait for 10ms