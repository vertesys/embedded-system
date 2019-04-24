
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI


class detection():

    def __init__(self):
        self.pin1 = 1
        self.pin2 = 20
        self.pin3 = 4
        self.pin4 = 16
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin1, GPIO.IN)
        GPIO.setup(self.pin2, GPIO.IN)
        GPIO.setup(self.pin3, GPIO.IN)
        GPIO.setup(self.pin4, GPIO.IN)

    def obstacle(self) -> str:
        if GPIO.input(self.pin1) == 0:
            return "droite"
        elif GPIO.input(self.pin2) == 0:
            return "droite"
        elif GPIO.input(self.pin3) == 0:
            return "gauche"
        elif GPIO.input(self.pin4) == 0:
            return "gauche"
