#include <Servo.h>

const int irSensorPin = 2;  // Replace with the appropriate pin number
const int servoPin = 9;     // Replace with the appropriate servo pin number

Servo myservo;
int sensorValue;

Servo servo1;
Servo servo2;
Servo servo3;

void setup() {
  myservo.attach(servoPin);
  pinMode(irSensorPin, INPUT);

   servo1.attach(10);
  servo2.attach(11);
  servo3.attach(13);
  Serial.begin(9600);
}

void loop() {
  sensorValue = digitalRead(irSensorPin);

  if (sensorValue == HIGH) {
    myservo.write(0);  // Rotate the servo to the middle position
    delay(1000);       // Wait for 1 second
  } else {
    myservo.write(90);   // Rotate the servo to the left position
    delay(4000);       // Wait for 1 second
  }

   if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    int servoPin = command.substring(0, command.indexOf(':')).toInt();
    int angle = command.substring(command.indexOf(':') + 1).toInt();

    if (servoPin == 10) {
      servo1.write(angle);
    } else if (servoPin == 11) {
      servo2.write(angle);
    } else if (servoPin == 13) {
      servo3.write(angle);
    }

    delay(15);
  }
}