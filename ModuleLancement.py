#!/usr/bin/python3
#-*- coding : UTF-8 -*-
import os
import sys


class Lancement():

    def Restartd(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    # Lecture du fichier init.txt pour connaitre son etat
    def states_run(self)-> str:
        f = open("init.txt")
        state = f.readline()
        f.close()
        return (state)

    # Demarrage du programme principal du robot
    def CheckRobot(self):
        fic = open("init.txt", "w")
        fic.writelines("1")
        fic.close()
        state = "1"



