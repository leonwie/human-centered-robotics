import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

import time
import math
import Adafruit_ADS1x15

import slider

from config import *


adc = Adafruit_ADS1x15.ADS1015()


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(5, GPIO.OUT) # Chip Enable
try:
    while 1:
            slider.initialise()
except KeyboardInterrupt:
    print("END")
    GPIO.cleanup()