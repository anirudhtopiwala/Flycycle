
const int joypitch = 44 ;

void setup() {
  Serial.begin(9600);

  pinMode(joypitch , OUTPUT);

}

void loop() {

  digitalWrite(joypitch , HIGH);
  delayMicroseconds(1); // Approximately 10% duty cycle @ 1KHz
  digitalWrite(joypitch , LOW);
  delayMicroseconds(4 - 1);
 //analogWrite(joypitch, 125 );

 //delay(2);        // delay in between reads for stability
}
