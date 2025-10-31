#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

#define MIN_PULSE_WIDTH 650
#define MAX_PULSE_WIDTH 2350
#define FREQUENCY 50

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

int potMuñeca = A3;
int potCodo = A2;
int potHombro = A1;
int potBase = A0;

int mano = 11;
int muñeca = 12;
int codo = 13;
int hombro = 14;
int base = 15;

void setup()
{
  pwm.begin();
  pwm.setPWMFreq(FREQUENCY);
  Serial.begin(9600);
  Serial.println("Control de brazo robótico iniciado");
}

void moverMotor(int controlIn, int motorOut)
{
  int pulse_wide, pulse_width, potVal;

  potVal = analogRead(controlIn);

  pulse_wide = map(potVal, 800, 240, MIN_PULSE_WIDTH, MAX_PULSE_WIDTH);
  pulse_width = int(float(pulse_wide) / 1000000 * FREQUENCY * 4096);

  pwm.setPWM(motorOut, 0, pulse_width);
}

void loop()
{
  moveMotor(potMuñeca, muñeca);
  moveMotor(potCodo, codo);
  moveMotor(potHombro, hombro);
  moveMotor(potBase, base);
}

