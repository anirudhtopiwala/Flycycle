#include <Wire.h>
#include <Adafruit_MCP4725.h>


Adafruit_MCP4725 dac1(1);
Adafruit_MCP4725 dac2(2);

/*<<<<<<<<<<<<<<<<<<<<<<<<<
Limits for the FLcycle are:
Picth : 43 - 320 - 520
Roll: 190 - 300 - 400

Volatge for Dac: 0 - 2048 - 4097
**/
double pitch, roll, psig, rsig; 
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  dac1.begin(0x63);
  dac2.begin(0x63);
}

// the loop routine runs over and over again forever:
void loop() {
  int pitch = analogRead(A0);
  int roll= analogRead(A1);

  // Pitch
  if(pitch == 320 ){
    psig = 2048;
  }
  else if(pitch < 320 && pitch > 43){
    psig = 2048*(picth-43)/277;
    }
   else if (pitch < 520 && pitch > 320){
    psig = 2047 + 2048*(picth-320)/200;
   }

   // ROLL
  if(roll == 300 ){
    rsig = 2048;
  }
  else if(roll < 300 && roll > 190){
    rsig = 2048*(roll-190)/110;
    }
   else if (roll < 400 && roll > 300){
    rsig = 2047 + 2048*(roll-300)/100;
   }
   
dac1.setVoltage(psig, false);
dac2.setVoltage(rsig, false);
}
