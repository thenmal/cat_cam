// Sweep
// by BARRAGAN <http://barraganstudio.com> 
// This example code is in the public domain.


#include <Servo.h> 
 
Servo myservo;  // create servo object to control a servo 
                // a maximum of eight servo objects can be created 
 
int pos = 0;    // variable to store the servo position 
int i = 0;    // number of times the servo will loop per signal
 
String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete 
 
void setup() 
{ 
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object 
}     

void loop() {
  // print the string when a newline arrives:
  if (stringComplete) {
    
        for(i = 0; i < 5; i += 1) { 
          for(pos = 0; pos < 180; pos += 1)  // goes from 0 degrees to 180 degrees 
              {                                  // in steps of 1 degree 
                myservo.write(pos);              // tell servo to go to position in variable 'pos' 
                delay(15);                       // waits 15ms for the servo to reach the position 
              } 
              for(pos = 180; pos>=1; pos-=1)     // goes from 180 degrees to 0 degrees 
              {                                
                myservo.write(pos);              // tell servo to go to position in variable 'pos' 
                delay(15);                       // waits 15ms for the servo to reach the position 
              } 
        } 
    
    // clear the string:
    inputString = "";
    
    
    
    stringComplete = false;
  }
} 
 


void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read(); 
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    } 
  }
}
