
from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep
import detecproxi

class Mouvements(detecproxi.detection):
    def __init__(self):
        super().__init__()
        # ///////////////// Define Motor Driver GPIO Pins /////////////////
        # Motor A, Left Side GPIO CONSTANTS
        PWM_DRIVE_LEFT = 21		# ENA - H-Bridge enable pin
        FORWARD_LEFT_PIN = 26	# IN1 - Forward Drive
        REVERSE_LEFT_PIN = 19	# IN2 - Reverse Drive
        # Motor B, Right Side GPIO CONSTANTS
        PWM_DRIVE_RIGHT = 5		# ENB - H-Bridge enable pin
        FORWARD_RIGHT_PIN = 13	# IN1 - Forward Drive
        REVERSE_RIGHT_PIN = 6	# IN2 - Reverse Drive

        # Initialise objects for H-Bridge GPIO PWM pins
        # Set initial duty cycle to 0 and frequency to 1000
        self.driveLeft = PWMOutputDevice(PWM_DRIVE_LEFT, True, 0, 1000)
        self.driveRight = PWMOutputDevice(PWM_DRIVE_RIGHT, True, 0, 1000)

        # Initialise objects for H-Bridge digital GPIO pins
        self.forwardLeft = PWMOutputDevice(FORWARD_LEFT_PIN)
        self.reverseLeft = PWMOutputDevice(REVERSE_LEFT_PIN)
        self.forwardRight = PWMOutputDevice(FORWARD_RIGHT_PIN)
        self.reverseRight = PWMOutputDevice(REVERSE_RIGHT_PIN)

        self.val = ""


    def Ravancer(self, forwardG:bool, reverseG:bool, forwardD, reversedD, VG, VD):
        self.forwardLeft.value = forwardG
        self.reverseLeft.value = reverseG
        self.forwardRight.value = forwardD
        self.reverseRight.value = reversedD
        self.driveLeft.value = VG
        self.driveRight.value = VD

    def avancer(self):

        self.val = self.obstacle()

        # self.forwardLeft.value = self.forwardgauche
        # self.reverseLeft.value = self.reversegauche
        # self.forwardRight.value = self.forwarddroite
        # self.reverseRight.value = self.reversedroite
        # self.driveLeft.value = self.Vgauche
        # self.driveRight.value = self.Vdroite

        if self.val == "droite":
            self.forwardLeft.value = False
            self.reverseLeft.value = True
            self.forwardRight.value = False
            self.reverseRight.value = True
            self.driveLeft.value = 1
            self.driveRight.value = 0.2


        elif self.val == "gauche":
            self.forwardLeft.value = False
            self.reverseLeft.value = True
            self.forwardRight.value = False
            self.reverseRight.value = True
            self.driveLeft.value = 0.2
            self.driveRight.value = 1

        elif self.val == "centre":
            self.forwardLeft.value = True
            self.reverseLeft.value = False
            self.forwardRight.value = True
            self.reverseRight.value = False
            self.driveLeft.value = 1
            self.driveRight.value = 1
        else:
            self.forwardLeft.value = False
            self.reverseLeft.value = True
            self.forwardRight.value = False
            self.reverseRight.value = True
            self.driveLeft.value = 1
            self.driveRight.value = 1









