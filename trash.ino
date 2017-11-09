#include <Servo.h>

Servo myservo;
int increase = 30;
int min_angle = 15;
int max_angle = 165;
int pos = min_angle;

int TrigPin = 12;
int EchoPin = 13;

void setup(){
  Serial.begin(9600);
  myservo.attach(6);
  pinMode(TrigPin, OUTPUT);
  pinMode(EchoPin, INPUT);
}

void loop(){
  Serial.println(distance());
  delay(2000);
  myservo.write(pos);
   
  pos += increase;
  if(pos <= min_angle || pos >=max_angle)
    increase *=-1;
  
}

unsigned long distance() {
   unsigned long d;
  
  digitalWrite(TrigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(TrigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(TrigPin, LOW);
  
  d = pulseIn(EchoPin, HIGH)/2*0.034; //cm
  
  return d;
}
  
  
  
