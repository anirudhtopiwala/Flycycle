/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/AnalogReadSerial
*/

// the setup routine runs once when you press reset:
int pin = A0;
int c=0;
long prevtime = 0;
float rpm =0.0;
long currtime =0;
long elpased =0 ;
float prevvoltage=0.0;
float voltdiff=0.0;
void setup() {
  // initialize serial communication at 9600 bits per second:
  analogReference(INTERNAL);
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  int sensorValue = analogRead(pin);
  float voltage = sensorValue * (5.0 / 1023.0);
//  Serial.println(voltage);
 //  Serial.println(sensorValue);
   long currtime = millis();  
   voltdiff= voltage-prevvoltage;
   if (voltdiff>2)
   {
     long elapsed = currtime - prevtime;        //  CALCULATE IDLE TIME
     rpm= 60*1000/elapsed;
     prevtime=currtime;    
     Serial.println(elapsed);
//     delay(1000);
   }
//    Serial.println(voltage);
}
////////////////////////////////////////////////////////////  END OF THE PROGRAM  ///////////////////////////////////////////////////////////////////////
