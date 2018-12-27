/* Sense the Tilting action of an rotary potentiometer and
outputs the data on the Serial port (USB).
(c) Anthony Kelly, 2013 */
/*
A0 : X-Axis
A1 : Y-Axis
A2 : Z-Axis
*/

int pitchpin = A0,rollpin= A1;
int controllerpitch = A4;
int controllerroll = A5;
int pitchavg, rollavg;
int pitchtilt, rolltilt;
int l1 = 6; 
int l2 = 7;
int r1 = 9;
int r2 = 10;
int swpin = 0;
int l1button = 0;
int r1button = 0;
int trigger = 0;
int pitchvalue = 0 ; int rollvalue = 0;
void setup() {
  Serial.begin(9600);          // Fast Baud rate to reduce lag
//  pinMode(swpin, INPUT);
//  digitalWrite(swpin, HIGH);    // Enable Pullup on Switch Pin
// Calibrate the sensor for LEVEL position by taking the Average of 8 readings
pitchavg = average(pitchpin);
rollavg = average(rollpin);
 pinMode(l1, INPUT);
 pinMode(l2, INPUT);
 pinMode(r1, INPUT);
 pinMode(r2, INPUT); 
 digitalWrite(l1, HIGH);
 digitalWrite(l2, HIGH);
 digitalWrite(r1, HIGH);
 digitalWrite(r2, HIGH);
}

void loop() {
 pitchtilt = (analogRead(pitchpin)-pitchavg);
 rolltilt = (analogRead(rollpin)-rollavg);
 l1button = digitalRead(l1); 
 r1button = digitalRead(r1); 


// Send the Data as a Serial String as follows:
// "pitchtilt, rolltilt \n"
// This String will be read by Python with lines separated by '\n'
   Serial.print(pitchtilt, DEC);                                  
   Serial.print(",");
   Serial.print(rolltilt, DEC);
   Serial.print(",");
   Serial.print(digitalRead(l1), DEC);
   Serial.print(",");
   Serial.print(digitalRead(l2), DEC);
   Serial.print(",");
   Serial.print(digitalRead(r1), DEC);
   Serial.print(",");
   Serial.print(digitalRead(r2), DEC);
   Serial.println();
//   delay(100);
  
  
}

// Get the Average of 8 readings from 'pin'
int average(int pin) {
  int Ave = 0;
  for (int i=0; i<8; i++) {
    Ave = Ave + analogRead(pin);
  }
  return Ave/8;
}
