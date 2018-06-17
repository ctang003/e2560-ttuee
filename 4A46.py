import RPi.GPIO as IO
import time

IO.setwarnings(False)

b0=b1=b2=b3=b4=b5=b6=b7=0
IO.setmode(IO.BOARD)
IO.setup(7,IO.IN)
IO.setup(11,IO.IN)
IO.setup(13,IO.IN)
IO.setup(15,IO.IN)
IO.setup(29,IO.IN)
IO.setup(31,IO.IN)
IO.setup(33,IO.IN)
IO.setup(35,IO.IN)
IO.setup(40,IO.OUT)  #y1
IO.setup(38,IO.OUT)  #y2
IO.setup(37,IO.OUT)  #y3
IO.setup(23,IO.OUT)  #y4
IO.setup(36,IO.OUT)

seg = (12,16,18,22,24,26,32)   # a,b,c,d,e,


def zero(a):
        num = [12,16,18,22,24,26,32]
        IO.output(num,(IO.LOW,IO.LOW,IO.LOW,IO.LOW,IO.LOW,IO.LOW,IO.HIGH))
def one(a):
        num = [12,16,18,22,24,26,32]
        IO.output(num,(IO.HIGH,IO.LOW,IO.LOW,IO.HIGH,IO.HIGH,IO.HIGH,IO.HIGH))
def two(a):
        num = [12,16,18,22,24,26,32]
        IO.output(num,(IO.LOW,IO.LOW,IO.HIGH,IO.LOW,IO.LOW,IO.HIGH,IO.LOW))
def three(a):
        num = [12,16,18,22,24,26,32]
        IO.output(num,(IO.LOW,IO.LOW,IO.LOW,IO.LOW,IO.HIGH,IO.HIGH,IO.LOW))
def four(a):
        num = [12,16,18,22,24,26,32]
        IO.output(num,(IO.HIGH,IO.LOW,IO.LOW,IO.HIGH,IO.HIGH,IO.LOW,IO.LOW))
def five(a):
        num = [12,16,18,22,24,26,32]
        IO.output(num,(IO.LOW,IO.HIGH,IO.LOW,IO.LOW,IO.HIGH,IO.LOW,IO.LOW))
def six(a):
        num = [12,16,18,22,24,26,32]
        IO.output(num,(IO.LOW,IO.HIGH,IO.LOW,IO.LOW,IO.LOW,IO.LOW,IO.LOW))
def seven(a):
        num = [12,16,18,22,24,26,32]
        IO.output(num,(IO.LOW,IO.LOW,IO.LOW,IO.HIGH,IO.HIGH,IO.HIGH,IO.HIGH))

def eight(a):
	num = [12,16,18,22,24,26,32]
	IO.output(num,IO.LOW)
def nine(a):
        num = [12,16,18,22,24,26,32]
        IO.output(num,(IO.LOW,IO.LOW,IO.LOW,IO.LOW,IO.HIGH,IO.LOW,IO.LOW)) 

compare = {0:zero,1:one,2:two,3:three,4:four,5:five,6:six,7:seven,8:eight,9:nine}

for n in range(0,7):
	IO.setup(seg[n],IO.OUT)
#a=input("insert a number: ")
while 1:

	inputValue = IO.input(35)
	if inputValue==True:
		b0=1
	elif inputValue ==False:
		b0=0
        inputValue = IO.input(33)
        if inputValue==True:
                b1=1
        elif inputValue ==False:
                b1=0
        inputValue = IO.input(31)
        if inputValue==True:
                b2=1
        elif inputValue ==False:
                b2=0
        inputValue = IO.input(29)
        if inputValue==True:
                b3=1
        elif inputValue ==False:
                b3=0
        inputValue = IO.input(15)
        if inputValue==True:
                b4=1
        elif inputValue ==False:
                b4=0
        inputValue = IO.input(13)
        if inputValue==True:
                b5=1
        elif inputValue ==False:
                b5=0
        inputValue = IO.input(11)
        if inputValue==True:
                b6=1
        elif inputValue ==False:
                b6=0
        inputValue = IO.input(7)
        if inputValue==True:
                b7=1
        elif inputValue ==False:
                b7=0

	x=(1*b0)+(2*b1)
	x=x+(4*b2)+(8*b3)
	x=x+(16*b4)+(32*b5)
	x=x+(64*b6)+(128*b7)

	y=(x/255.0)*25
	a1=round(y,3)*1000
	a1=int(a1)
	a2=a1/1000.0
	print "The voltage value of battery: ",a2,"V"
	y1=a1/1000
	y2=(a1%1000)/100
	y3=(a1%100)/10
	y4=a1%10
	b0=b1=b2=b3=b4=b5=b6=b7=0

	IO.output(36,IO.LOW)
	time.sleep(0.008)
        IO.output(40,IO.HIGH)
        compare[y1](y1)
        time.sleep(0.008)
	IO.output(36,IO.HIGH)
        IO.output(40,IO.LOW)


        time.sleep(0.008)
        IO.output(38,IO.HIGH)
        compare[y2](y2)
        time.sleep(0.008)
        IO.output(38,IO.LOW)

        time.sleep(0.008)
        IO.output(37,IO.HIGH)
        compare[y3](y3)
        time.sleep(0.008)
        IO.output(37,IO.LOW)

        time.sleep(0.008)
        IO.output(23,IO.HIGH)
        compare[y4](y4)
        time.sleep(0.008)
        IO.output(23,IO.LOW)
