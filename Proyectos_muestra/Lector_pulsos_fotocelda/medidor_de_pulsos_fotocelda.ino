int sensorPin = 34;
int sensorValue = 0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  sensorValue = analogRead(sensorPin);
  
  // Convertir a voltaje
  float voltage = (sensorValue / 4095.0) * 3.3;
  if(voltage < 0.20 && voltage > -0.20){
    Serial.println(voltage);
  }
  
  delay(10); // frecuencia de muestreo ~100 Hz
}
