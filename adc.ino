void setup() {
  Serial.begin(9600);
  pinMode(A0,INPUT);
  pinMode(1,OUTPUT);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
   pinMode(10,OUTPUT);
      
  

}

void loop() {
  int k = analogRead(A0);

      for(int i =1;i<=9;i++)
      {
        if(k==(i-1))
        digitalWrite(i,1);
        else
        digitalWrite(i,0);  
        
        }
        Serial.println(analogRead(A0)); 

}
//analog to digital
