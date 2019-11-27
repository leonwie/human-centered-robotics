import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

import time
import math
import Adafruit_ADS1x15

from firebase_access import checkFirebaseValue, setFirebaseValue

from config import *

import slider

adc = Adafruit_ADS1x15.ADS1015()


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(BUTTONIN_NO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # IN1
GPIO.setup(BUTTONIN_SKIP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # IN2
GPIO.setup(BUTTONIN_YES, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # IN3
GPIO.setup(BUTTONLED_NO, GPIO.OUT) # IN1
GPIO.setup(BUTTONLED_SKIP, GPIO.OUT) # IN2
GPIO.setup(BUTTONLED_YES, GPIO.OUT) # IN2
GPIO.setup(CHIP_EN, GPIO.OUT) # Chip Enable
GPIO.setup(MOTOR_RIGHT, GPIO.OUT) # IN1
GPIO.setup(MOTOR_LEFT, GPIO.OUT) # IN2

GAIN = 1

class Configuration:
  def __init__(self, yes, no, skip, slider):
    self.yes = yes
    self.no = no
    self.skip = skip
    self.slider = slider

print("Start pi program")
try:
    while 1:
        try:
            makeKnobs.end()
        except:
            print("NO object makeKnobs")
        state = checkFirebaseValue("Current_Screen")
        print("state: ", state)
        if state == "Welcome":
            configuration = Configuration(True, False, False, False)
        elif state == "Privacy":
            configuration = Configuration(True, True, False, False)
        else:
            if returnType[state] == "buttons":
                configuration = Configuration(True, True, True, False)
            else:
                configuration = Configuration(True, False, False, True)
                slider.initialise()
                makeKnobs = slider.makeKnobs()
        while state == checkFirebaseValue("Current_Screen"):
            GPIO.output(BUTTONLED_YES,configuration.yes)
            GPIO.output(BUTTONLED_NO,configuration.no)
            GPIO.output(BUTTONLED_SKIP,not configuration.skip)
            if configuration.slider:
                setFirebaseValue("Current_Slider_Value", slider.getLevel())
            if GPIO.input(BUTTONIN_YES) == GPIO.HIGH and configuration.yes:
                if configuration.slider:
                    setFirebaseValue(state, slider.getLevel())
                    makeKnobs.end()
                    slider.reset()
                else:
                    setFirebaseValue(state,"Yes")
                    time.sleep(0.5)
            elif GPIO.input(BUTTONIN_NO) == GPIO.HIGH and configuration.no:
                setFirebaseValue(state,"No")
                time.sleep(0.5)
            elif GPIO.input(BUTTONIN_SKIP) == GPIO.HIGH and configuration.skip:
                setFirebaseValue(state,"Skip")
                time.sleep(0.5)

except KeyboardInterrupt:
    print("END")
    GPIO.cleanup()