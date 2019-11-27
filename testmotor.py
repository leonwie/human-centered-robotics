import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

import time
import math
import Adafruit_ADS1x15

from threading import *

import slider

from config import *
import subprocess

subprocess.run(["rosrun", "turtlesim_cleaner", "rotate.py"])
adc = Adafruit_ADS1x15.ADS1015()


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(CHIP_EN, GPIO.OUT) # Chip Enable
GPIO.setup(5, GPIO.OUT) # IN1
GPIO.setup(MOTOR_LEFT, GPIO.OUT) # IN2

GAIN = 1

#print("Start pi program")

#makeNobs = slider.makeNobs()

#try:
   ## test = input("Enter your name: ")
   #makeNobs.end()
   # while 1:
   #     GPIO.output(CHIP_EN,1)
        #motor_left.ChangeDutyCycle(80)
        #GPIO.output(MOTOR_RIGHT,1)
#        print("exit")
#except KeyboardInterrupt:
#    print("END")
GPIO.cleanup()
