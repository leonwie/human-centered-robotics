import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

import time
import math
import Adafruit_ADS1x15

from config import *


adc = Adafruit_ADS1x15.ADS1015()


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(CHIP_EN, GPIO.OUT) # Chip Enable
GPIO.setup(MOTOR_RIGHT, GPIO.OUT) # IN1
GPIO.setup(MOTOR_LEFT, GPIO.OUT) # IN2

GAIN = 1

GPIO.output(CHIP_EN, 1)
motor_right = GPIO.PWM(MOTOR_RIGHT, 100)
motor_right.start(0)
motor_left = GPIO.PWM(MOTOR_LEFT, 100)
motor_left.start(0)
#GPIO.output(17, 0)
print("Start pi program")
try:
    while 1:
        values = adc.read_adc(0, gain=GAIN)
        values = math.floor(values/1.6)
        for i in range(1,5):
            if i==2:
                print(values)
            j = i*200
            if values > j-60 and values < j+60:
                print("inside")
                if values > j+10:
                    print("left")
                    motor_right.ChangeDutyCycle(0)
                    motor_left.ChangeDutyCycle(50)
                    time.sleep(0.0001)
                elif values < j -10:
                    print("right")
                    motor_right.ChangeDutyCycle(50)
                    motor_left.ChangeDutyCycle(0)
                    time.sleep(0.0001)
                else:
                    motor_right.ChangeDutyCycle(0)
                    motor_left.ChangeDutyCycle(0)
            else:
                motor_right.ChangeDutyCycle(0)
                motor_left.ChangeDutyCycle(0)

except KeyboardInterrupt:
    print("END")
    GPIO.cleanup()
