import RPi.GPIO as GPIO

class Presence():


    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.capteur = 14
        GPIO.setup(self.capteur, GPIO.IN)
        self.text = ""

    def mouvement(self):
        if GPIO.input(self.capteur):
            self.text = "Mouvement détecté"

        else:
            self.text = "il n'y a aucune présence"
        return self.text
