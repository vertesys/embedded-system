import ModuleLancement as deb
import ModuleMouvement as mouv
import ModuleDistance as dis
import ModulePresence as pres
import ModuleEcran as ecran

from time import sleep

lancement = deb.Lancement()
lancement.CheckRobot()
afecran = ecran.Ecran()
mov = mouv.Mouvements()
objetDistance = dis.Distance()
presence = pres.Presence()
Vconteur = 3
Position = 0
conteur = 0
va = list
ecran = 1
while True:

    state = lancement.states_run()
    if state != "1":
        lancement.Restartd()

    elif state == '1':
        if ecran == 1:
            afecran.text('coucou adj3')
            # afecran.image('cat.jpg')
            ecran = 0

        va = []
        if objetDistance.distance() < 10:
            mov.Ravancer(True, False, True, False, 0.6, 0.6)
            Vconteur = 3
            Position = 0
            conteur = 0
            sleep(1)

        elif Position == 0:

            if conteur == 0:
                mov.Ravancer(False, True, True, False, 0.5, 0.5)
                va.append(objetDistance.distance())

            if objetDistance.distance() > min(va) + 10:
                conteur = 1
                Position = 1
                Vconteur = 0
                mov.Ravancer(False, False, False, False, 0, 0)

        elif Vconteur == 0:
            caldis = (objetDistance.distance() / 2)
            Vconteur = 1

        elif Vconteur == 1:

            if objetDistance.distance() <= caldis:
                mov.Ravancer(False, False, False, False, 0, 0)
                Vconteur = 3
                Position = 0
                conteur = 0
            else:
                mov.avancer()


