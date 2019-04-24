import serial
import RPi.GPIO as GPIO


class Distance():

    def __init__(self):
        #GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.Dist_Total = 200
        self.ser = serial.Serial('/dev/ttyAMA0', 115200, timeout=1)

        # ser.write(0x42)
        self.ser.write(bytes(b'B'))

        # ser.write(0x57)
        self.ser.write(bytes(b'W'))

        # ser.write(0x02)
        self.ser.write(bytes(2))

        # ser.write(0x00)
        self.ser.write(bytes(0))

        # ser.write(0x00)
        self.ser.write(bytes(0))

        # ser.write(0x00)
        self.ser.write(bytes(0))

        # ser.write(0x01)
        self.ser.write(bytes(1))

        # ser.write(0x06)
        self.ser.write(bytes(6))
        Dist_Total = 200

    def distance(self) -> float:
        if ((b'Y' == self.ser.read()) and (b'Y' == self.ser.read())):

            Dist_L = self.ser.read()
            Dist_H = self.ser.read()
            self.Dist_Total = (ord(Dist_H) * 256) + (ord(Dist_L))
            for i in range(0, 5):
                self.ser.read()
            self.Dist_Total = (self.Dist_Total)

        return self.Dist_Total
