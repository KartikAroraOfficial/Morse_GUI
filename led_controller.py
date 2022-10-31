# This Python file uses the following encoding: utf-8
from gpiozero import LED
import RPi.GPIO as GPIO
import time
from morse import DOT_TIME, DASH_TIME



class led_controller:

    led = LED(14)

    def __init__(self):
        GPIO.setmode(GPIO.BCM)


    def blinkDit(self):
        self.led.on()
        time.sleep(DOT_TIME)
        self.led.off()


    def blinkDah(self):
        self.led.on()
        time.sleep(DASH_TIME)
        self.led.off()