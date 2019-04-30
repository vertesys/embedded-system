#! /usr/bin/python3
# -*- coding: utf-8 -*-
import time
import sys
import serial
import codecs

PORT_SERIE = "/dev/ttyAMA0"

# Initialisation du port sÃ©rie
ser = serial.Serial(
    port = PORT_SERIE,
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 3
)

# Gestion du CTRL C
def signal_handler(signal, frame):
        print ("Sortie du programme par Ctrl+C!")
        sys.exit(0)


# Lire le fichier de donnÃ©es Hexa
with open("data", "rb") as f:
    # Lire le premier octet
    byte = f.read(1)
    # Boucler tant qu'on n'est pas Ã  la fin du fichier
    while byte != b"":
        # Lecture de l'octet suivant + Ã©ventuelle modif
        byte = f.read(1)
        print (byte)
        # Envoyer sur le port sÃ©rie
        ser.write(byte)






