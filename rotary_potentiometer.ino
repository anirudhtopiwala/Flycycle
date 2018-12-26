/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/AnalogReadSerial
*/

// the setup routine runs once when you press reset:
int newvalue;
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int pitch = analogRead(A0);
  int roll= analogRead(A1);
//  int joystickvalue=analogRead(A4);
  // print out the value you read:
  Serial.println(pitch);
  Serial.println(roll);
  int sensorvalue  = pitch;
  if(sensorvalue < 350)
  {
//    int diffright= (350 -sensorvalue);
//    int newvalue= abs(200 - round((diffright)*3.125));
    int newvalue = 5;
    Serial.println("Going Left");
    analogWrite(A4, newvalue);

  }
  else if(sensorvalue > 495)
  {
//     int diffleft= (490 -sensorvalue);
//     int newvalue= abs(668 - round((diffleft)*2.97));
     int newvalue = 660;
//     Serial.println("Going Right");
//     analogWrite(A4, newvalue);
  }
  else
  {
    Serial.println("Center"); 
      int newvalue= 380;
     analogWrite(A4, newvalue);
//      Serial.println(newvalue);

  }
//  int finalvalue= analogRead(A4);
//  Serial.println(finalvalue);
// 
  
//  Serial.println(sensorvalue);

  delay(100);        // delay in between reads for stability
}
