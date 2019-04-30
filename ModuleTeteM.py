#importer RPi.GPIO
import time

import RPi.GPIO as GPIO

#numerotation des pins d'apres leur position physique

#GPIO.setmode(GPIO.BCM)

#declarer pin11 comme pin du signal


#while True :

    #changer l'angle (0 à 90°) en modifiant le duty cycle à 12.5%

# DutyCycle = 1 / 18 * (90) + 2
# pwm.ChangeDutyCycle(DutyCycle)
# time.sleep(0.5)

class Tmoteur():

    def __init__(self):
        GPIO.setup(17, GPIO.OUT)
        GPIO.setwarnings(False)
        # declarer un objet pwm en indiquant le pin et la frequence

        self.pwm = GPIO.PWM(17, 50)
        # initialiser l'objet PWM avec un duty cycle de 2.5% (angle 0°)
        self.pwm.start(2.5)

    def tmoteur(self,rotation):
        DutyCycle = 1 / 18 * (rotation) + 2
        self.pwm.ChangeDutyCycle(DutyCycle)
        time.sleep(0.5)
        GPIO.cleanup()
