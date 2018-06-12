import RPi.GPIO as GPIO     #calling for header file which GPIO for pi
import time, datetime       #calling for time delay 
now = datetime.datetime.now()
GPIO.setmode(GPIO.BCM)      # 
GPIO.setwarnings(False)
 
segment8 =  (26,19,13,6,5,11,9) #a,b,c,d,e,f,g,p
ipt      =  (22,27,17,4,3,2,14,15,18) 

for segment in segment8:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)
    
for inpt in ipt:
    GPIO.setup(inpt , GPIO.IN)
    
 
    #D 1
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12,1) 
    #D 2
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, 1) 
    #D 3
    GPIO.setup(20, GPIO.OUT)
    GPIO.output(20, 1)
    #D 4
    GPIO.setup(21, GPIO.OUT)
    GPIO.output(21, 1) 
    #D 8
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24, 1) 
    #D 7
    GPIO.setup(25, GPIO.OUT)
    GPIO.output(25, 1) 
    #D 6
    GPIO.setup(8, GPIO.OUT)
    GPIO.output(8, 1) 
    #D 5
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, 1) 
    

zero = [1,1,1,1,1,1,0]
one = [0,1,1,0,0,0,0]
two = [1,1,0,1,1,0,1]
three = [1,1,1,1,0,0,1]
four = [0,1,1,0,0,1,1]
five = [1,0,1,1,0,1,1]
six = [1,0,1,1,1,1,1]
seven = [1,1,1,0,0,0,0]
eight = [1,1,1,1,1,1,1]
nine = [1,1,1,1,0,1,1]
def print_segment(charector):
    if charector == 1:
        for i in range(7):
            GPIO.output(segment8[i], one[i])
    if charector == 2:
        for i in range(7):
            GPIO.output(segment8[i], two[i])
    if charector == 3:
        for i in range(7):
            GPIO.output(segment8[i], three[i])
    if charector == 4:
        for i in range(7):
            GPIO.output(segment8[i], four[i])
    if charector == 5:
        for i in range(7):
            GPIO.output(segment8[i], five[i])
    if charector == 6:
        for i in range(7):
            GPIO.output(segment8[i], six[i])
    if charector == 7:
        for i in range(7):
            GPIO.output(segment8[i], seven[i])
    if charector == 8:
        for i in range(7):
            GPIO.output(segment8[i], eight[i])
    if charector == 9:
        for i in range(7):
            GPIO.output(segment8[i], nine[i])
    if charector == 0:
        for i in range(7):
            GPIO.output(segment8[i], zero[i])
                                       
    return;
while 1:
    for i in range(8):
        if GPIO.input(ipt[i]):
            a=i
    vo=(a*48)
    total=48*a
    
    c1_=total/1000
    c2_=total/100
    c3_=(total/10)%10
    c4_=total%10
    c1=int(c1_)
    c2=int(c2_)
    c3=int(c3_)
    c4=int(c4_)
    v1_=vo/1000
    v2_=vo/100
    v3_=(vo/10)%10
    v4_=vo%10
    v1=int(v1_)
    v2=int(v2_)
    v3=int(v3_)
    v4=int(v4_)
    
    
  
    delay_time = 0.001
   
    GPIO.output(12, 0) 
    print_segment (v1) 
    time.sleep(delay_time)
    GPIO.output(12, 1)
    GPIO.output(16, 0) 
    print_segment (v2) 
     
    time.sleep(delay_time)
    GPIO.output(16, 1)
    GPIO.output(20, 0) 
    
    print_segment (v3) 
    time.sleep(delay_time)
    GPIO.output(20, 1)
    GPIO.output(21, 0) 
    
    print_segment (v4) 
    time.sleep(delay_time)
    GPIO.output(21, 1)
    
    
    GPIO.output(24, 0) 
    
    print_segment (c1) 
    time.sleep(delay_time)
    GPIO.output(24, 1)
    GPIO.output(25, 0) 
    print_segment (c2)
    
    time.sleep(delay_time)
    GPIO.output(25, 1) 
    GPIO.output(8, 0) 
    
    print_segment (c3) 
    time.sleep(delay_time)
    GPIO.output(8, 1) 
    GPIO.output(7, 0) 
  
    print_segment (c4) 
    time.sleep(delay_time)
    GPIO.output(7, 1) 
 
    