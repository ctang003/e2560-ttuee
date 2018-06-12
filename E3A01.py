///////////////// E3A01


void setup() {
  Serial.begin(9600);   
  for(int i = 2;i <=11;i++){
    pinMode(i,OUTPUT);
  }
}

void loop() {

float value = analogRead(A0) * (5.0 / 1024.0) * 5.0;
int   val=(int(value*100));
  Serial.println(val);
  String string0 = String(val,BIN);
  Serial.println(string0);
  int   ssize=string0.length();// find the size of the string0
  Serial.println(ssize);
  //Serial.println(String.length(string0));
  for(int i=2 ; i<=11;i++){
    digitalWrite(i,LOW);// pin0 to  pin10 are low
  }
  for(int i=0;string0[i];i++){
      if(string0[i] == '1'){
          digitalWrite(12-ssize,HIGH);
          Serial.print(12-ssize);
          Serial.println(" high");
          ssize--;
      }
      if(string0[i] == '0'){
          digitalWrite(12-ssize,LOW);
          Serial.print(12-ssize);
          Serial.println(" low");   
          ssize--;  
      } 
    }
    delay(500);   // remember to delete it  
 }  




import RPi.GPIO as GPIO
import datetime
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

segments = (27,18,23,22,24,25,8)
for segment in segments:
    GPIO.setup(segment,GPIO.OUT)
    GPIO.output(segment,0)   # segment off

digits = (2,3,4,5)
for digit in digits:
    GPIO.setup(digit,GPIO.OUT)
    GPIO.output(digit,1) # digit off

num = {'0':(27,18,23,22,24,25),
       '1':(18,23),
       '2':(27,18,8,24,22),
       '3':(27,18,23,22,8),
       '4':(25,8,18,23),
       '5':(27,23,22,25,8),
       '6':(27,23,22,24,25,8),
       '7':(27,18,23),
       '8':(27,18,23,22,24,25,8),
       '9':(27,18,23,22,25,8)
       }



digits2 = (17,10,11,7)
for digit2 in digits2:
    GPIO.setup(digit2,GPIO.OUT)
    GPIO.output(digit2,1)
    

def print_display(ch):
    if ch == 0:
       
       for segment in num['0'] :
                GPIO.output(segment,1)  
    elif ch == 1:
       
       for segment in num['1'] :
                GPIO.output(segment,1)
    
    elif ch == 2:
        
        for segment in num['2']:
                GPIO.output(segment,1)
    elif ch==3:
        
        for segment in num['3']:
                GPIO.output(segment,1)
    elif ch==4:
        
        for segment in num['4']:
                GPIO.output(segment,1)
    elif ch==5:
        
        for segment in num['5']:
                GPIO.output(segment,1)
    elif ch==6:
        
        for segment in num['6']:
                GPIO.output(segment,1)
    elif ch==7:
        
        for segment in num['7']:
                GPIO.output(segment,1)
    elif ch==8:
        
        for segment in num['8']:
                GPIO.output(segment,1)
    if ch==9:
        for segment in num['9']:
                GPIO.output(segment,1)

    return;



GPIO.setup(6,GPIO.IN)
GPIO.setup(12,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(14,GPIO.IN)
GPIO.setup(15,GPIO.IN)
GPIO.setup(16,GPIO.IN)
GPIO.setup(19,GPIO.IN)
GPIO.setup(20,GPIO.IN)
GPIO.setup(21,GPIO.IN)
GPIO.setup(26,GPIO.IN)
   
x=[0,0,0,0,0,0,0,0,0,0]

    
while 1:
        x[0]=GPIO.input(6)
        x[1]=GPIO.input(12)
        x[2]=GPIO.input(13)
        x[3]=GPIO.input(14)
        x[4]=GPIO.input(15)
        x[5]=GPIO.input(16)
        x[6]=GPIO.input(19)
        x[7]=GPIO.input(20)
        x[8]=GPIO.input(21)
        x[9]=GPIO.input(26)
        #print(''.join(map(str,x)))
        b=9
        de=0
        for i in range(0,10):
            de=de+x[i]*2**(i+b)
            b=b-2
        #print(de)
        current=de/235*10
        
        
        GPIO.output(2,0)
        print_display(int(de/100))
        time.sleep(0.0001)
        GPIO.output(2,1)
        for segment in segments:
            GPIO.output(segment,0)
        GPIO.output(3,0)
        print_display(int(de/10)%10)
        time.sleep(0.0001)
        
        GPIO.output(3,1)
        for segment in segments:
            GPIO.output(segment,0) 

        GPIO.output(4,0)
        print_display(de%100)
        time.sleep(0.0001)
        GPIO.output(4,1)
        for segment in segments:
            GPIO.output(segment,0) 
 
        GPIO.output(5,0)
        print_display(0)
        time.sleep(0.0001)
        GPIO.output(5,1)
        for segment in segments:
            GPIO.output(segment,0)
    
    
        GPIO.output(17,0)
        print_display(0)
        time.sleep(0.0001)
        GPIO.output(17,1)
        for segment in segments:
            GPIO.output(segment,0)
            
        GPIO.output(10,0)
        print_display(0)
        time.sleep(0.0001)     
        GPIO.output(10,1)
        for segment in segments:
            GPIO.output(segment,0) 

        GPIO.output(11,0)
        print_display(int(current/10))
        time.sleep(0.0001)
        GPIO.output(11,1)
        for segment in segments:
            GPIO.output(segment,0)
            
        GPIO.output(7,0)
        print_display(int(current)%10)
        time.sleep(0.0001)
        GPIO.output(7,1)
        for segment in segments:
            GPIO.output(segment,0)
    

    
        
