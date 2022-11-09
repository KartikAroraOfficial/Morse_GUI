# This Python file uses the following encoding: utf-8

from gpiozero import LED
import time
import morse


class led_controller(object):
    def __init__(self):
        self.led = LED(14)

    def blinkDit(self):
        self.led.on()
        time.sleep(morse.DOT_TIME)
        self.led.off()

    def blinkDah(self):
        self.led.on()
        time.sleep(morse.DASH_TIME)
        self.led.off()
