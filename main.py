import ModuleLancement as deb
import ModuleMouvement as mouv
import ModuleDistance as dis
import ModulePresence as pres
import ModuleEcran as ecran
# import ModuleTeteM as rmoteur

from time import sleep
# rmot =rmoteur.Tmoteur()
afecran = ecran.Ecran()
mov = mouv.Mouvements()
objetDistance = dis.Distance()
presence = pres.Presence()
Vconteur = 3
Position = 0
conteur = 0
va = list
ecran = 1
state = "1"
while True:

    if state != "1":
        mov.stop()


    elif state == '1':
        if ecran == 1:
            afecran.text('fantastics... bizou.')
            # afecran.image('cat.jpg')
            ecran = 0
            # rmot.tmoteur(90)
        va = []

        # if objetDistance.distance() < 35:
        #     Vconteur = 3
        #     Position = 0
        #     conteur = 0
        # elif Position == 0:
        #
        #     if conteur == 0:
        #         mov.Ravancer(False, True, True, False, 0.8, 0.8)
        #         va.append(objetDistance.distance())
        #
        #     if objetDistance.distance() > min(va):
        #         conteur = 1
        #         Position = 1
        #         Vconteur = 0
        #         mov.Ravancer(False, False, False, False, 0, 0)
        #         sleep(1)
        #
        # elif Vconteur == 0:
        #     caldis = (objetDistance.distance())
        #     Vconteur = 1
        #
        # elif Vconteur == 1:
        #
        #     if objetDistance.distance() <= caldis:
        #         mov.Ravancer(False, False, False, False, 0, 0)
        #         Vconteur = 3
        #         Position = 0
        #         conteur = 0
        #         sleep(1)
        #     else:
        #         # mov.avancer()
        #         mov.Ravancer(True, False, True, False, 0.8, 0.8)
        #         sleep(2)
        #         mov.Ravancer(True, False, False, True, 0.8, 0.8)
        #         sleep(2)
        #         mov.Ravancer(False, True, True, False, 0.8, 0.8)
        #         sleep(4)
        #         mov.Ravancer(True, False, False, True, 0.8, 0.8)
        #         sleep(2)
        #         mov.Ravancer(True, False, True, False, 0.8, 0.8)
        #         sleep(1)
        #
        #         mov.Ravancer(True, False, False, True, 0.8, 0.8)
        #         sleep(4)
        #         # rmot.tmoteur(90)
        #         # rmot.tmoteur(45)
        #         # rmot.tmoteur(125)
        #
        #         mov.Ravancer(False, True, True, False, 0.8,0.8)
        #         sleep(2)
        #         mov.Ravancer(True, False, True, False, 0.8, 0.8)
        #         sleep(2)
        #         mov.Ravancer(False, True, False, True, 0.8, 0.8)
        #         sleep(2)
        #         mov.Ravancer(True, False, True, False, 0.8, 0.8)
        #         sleep(2)
        #         mov.Ravancer(False, True, True, False, 0.8, 0.8)
        #         sleep(3)



