#importer RPi.GPIO

import RPi.GPIO as GPIO

#numerotation des pins d'apres leur position physique

GPIO.setmode(GPIO.BCM)

#declarer pin11 comme pin du signal

GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)
#declarer un objet pwm en indiquant le pin et la frequence

pwm=GPIO.PWM(17,50)
# initialiser l'objet PWM avec un duty cycle de 2.5% (angle 0°)
pwm.start(2.5)
while True :

    #changer l'angle (0 à 90°) en modifiant le duty cycle à 12.5%
    DutyCycle = 1/18* (90) + 2
    pwm.ChangeDutyCycle(DutyCycle)
    DutyCycle = 1 / 18 * (10) + 2
    pwm.ChangeDutyCycle(DutyCycle)
# import RPi.GPIO as GPIO
# import time
#
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(17, GPIO.OUT)
# GPIO.setwarnings(False)
#
# ajoutAngle = 5
#
# # nbrTour = int(input("Entrez le nombre d'aller-retour que fera le Servo :\n"))
#
# pwm=GPIO.PWM(17,50)
# pwm.start(2.5)
# pwm.ChangeDutyCycle(2.5)
# time.sleep(1)
# pwm.ChangeDutyCycle(10)
# time.sleep(1)
# # angle1 = 0
# # duty1 = float(angle1)/10 + ajoutAngle
# #
# # angle2= 180
# # duty2= float(angle2)/10 + ajoutAngle
#
# i = 0
#
# # while i <= nbrTour:
# #     pwm.ChangeDutyCycle(5.0)
# #     time.sleep(1)
# #     pwm.ChangeDutyCycle(10.0)
# #     time.sleep(1)
# #     i = i+1
# # GPIO.cleanup()
#
#
# GPIO.cleanup()
GPIO.cleanup()