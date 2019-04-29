import RPi.GPIO as GPIO

class Presence():

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.capteur = 7
        GPIO.setup(self.capteur, GPIO.IN)
        self.text = ""

    def mouvement(self):
        if GPIO.input(self.capteur):
            self.text = "1"
        else:
            self.text = "0"
        return self.text
