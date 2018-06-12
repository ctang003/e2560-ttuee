import RPi.GPIO as GPIO     #calling for header file which GPIO for pi
import time, datetime       #calling for time delay 
now = datetime.datetime.now()
GPIO.setmode(GPIO.BCM)      # 
GPIO.setwarnings(False)
 
segment8 =  (26,19,13,6,5,11,9,10) #a,b,c,d,e,f,g,p
seg      =  (2,3,4,17,27,22,21,12) #d1(hour1),d2(hour2),d3(minute1),d4(minute2),d5(second1),d6(second2),d7(microsecond1),d8(microsecond2)

for segment in segment8:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)
    
for se in seg:
    GPIO.setup(se , GPIO.OUT)
    GPIO.output(se , 1)
 
    #D 1
    GPIO.setup(20, GPIO.OUT)
    GPIO.output(20, 0) 
    #D 2
    GPIO.setup(8, GPIO.OUT)
    GPIO.output(8, 0) 
    #D 3
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, 0)
    #D 4
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24, 0) 
    #D 8
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, 0) 
    #D 7
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, 0) 
    #D 6
    GPIO.setup(15, GPIO.OUT)
    GPIO.output(15, 0) 
    #D 5
    GPIO.setup(14, GPIO.OUT)
    GPIO.output(14, 0) 
    

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
                       
def print_se(charector):
    if charector == 1:
        for i in range(7):
            GPIO.output(seg[i], one[i])
    if charector == 2:
        for i in range(7):
            GPIO.output(seg[i], two[i])
    if charector == 3:
        for i in range(7):
            GPIO.output(seg[i], three[i])
    if charector == 4:
        for i in range(7):
            GPIO.output(seg[i], four[i])
    if charector == 5:
        for i in range(7):
            GPIO.output(seg[i], five[i])
    if charector == 6:
        for i in range(7):
            GPIO.output(seg[i], six[i])
    if charector == 7:
        for i in range(7):
            GPIO.output(seg[i], seven[i])
    if charector == 8:
        for i in range(7):
            GPIO.output(seg[i], eight[i])
    if charector == 9:
        for i in range(7):
            GPIO.output(seg[i], nine[i])
    if charector == 0:
        for i in range(7):
            GPIO.output(seg[i], zero[i])   
            
    return;
while 1:
    now = datetime.datetime.now()
    h = now.hour
    m = now.minute
    s= now.second
    ms=now.microsecond
    
    h1_ = h / 10
    h1=int(h1_)
    h2 = h % 10
    m1_ = m / 10
    m1=int(m1_)
    m2 = m % 10
    s1_ = s / 10
    s1=int(s1_)
    s2_ = s % 10
    s2=int(s2_)
    
    ms1=ms/10
    ms2=ms%10
  
    delay_time = 0.001
   
    GPIO.output(20, 1) 
    GPIO.output(10, 1)
    print_segment (h1) 
    time.sleep(delay_time)
    GPIO.output(20, 0)
    GPIO.output(8, 1) 
    print_segment (h2) 
    GPIO.output(10, 0) 
    time.sleep(delay_time)
    GPIO.output(8, 0)
    GPIO.output(16, 1) 
    GPIO.output(10, 1)
    print_segment (m1) 
    time.sleep(delay_time)
    GPIO.output(16, 0)
    GPIO.output(24, 1) 
    GPIO.output(10, 1)
    print_segment (m2) 
    time.sleep(delay_time)
    GPIO.output(24, 0)
    
    
    GPIO.output(23, 1) 
    GPIO.output(12, 1)
    print_se (s1) 
    time.sleep(delay_time)
    GPIO.output(23, 0)
    GPIO.output(18, 1) 
    print_se (s2)
    GPIO.output(12, 0) 
    time.sleep(delay_time)
    GPIO.output(18, 0) 
    GPIO.output(15, 1) 
    GPIO.output(12, 1)
    print_se (ms1) 
    time.sleep(delay_time)
    GPIO.output(15, 0) 
    GPIO.output(14, 1) 
    GPIO.output(12, 1)
    print_se (ms2) 
    time.sleep(delay_time)
    GPIO.output(14, 0) 
 
    