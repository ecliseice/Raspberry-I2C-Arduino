
#include <Wire.h>
#define Photo_pin A0     // Датчик DHT11 подключен к цифровому пину номер 4

int SLAVE_ADDRESS = 0x04;
int ledPin = 13;
int ledOn = 0;

void setup() {
  Serial.begin(9600);   // Скорость работы порта
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(processMessage);
  Wire.onRequest(sendAnalogReading);
}

void loop() {

}

void processMessage(int n) {
  int led_status = Wire.read();

  if (led_status > 0) {
    if (led_status == 1) ledOn = 1;
    else ledOn = 0;
    digitalWrite(ledPin, ledOn);
  }
}

void sendAnalogReading() {
  int value = analogRead(Photo_pin);
  float num = 0.09803922;
  int new_value = 100 - floor(value * num);

  //  byte output[] = {byte(new_value),byte(ledOn)};
  //Wire.write(output,2);
  byte output[] = {byte(new_value)};
  Wire.write(output, 1);
}
