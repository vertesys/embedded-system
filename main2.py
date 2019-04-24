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
Vconteur = 0
Position = 0
conteur = 0
va = []
while True:

    afecran.text(presence.mouvement())

    if objetDistance.distance() < 10 :
        Vconteur = 3
        Position = 0

    if Position == 0:
        if conteur == 0:
            mov.Ravancer(False, True, True, False, 0.5, 0.5)
            va.append(objetDistance.distance())

        if objetDistance.distance() > min(va)+10 :
            conteur = 1
            Position = 1
            Vconteur = 0
            mov.Ravancer(False, False, False, False, 0, 0)

        # print(objetDistance.distance())
        # print('min',min(va))
        sleep(1)

    else:

        if Vconteur == 0 :
            caldis = (objetDistance.distance()/2)
            Vconteur = 1
        elif Vconteur == 1:

            if objetDistance.distance() <= caldis:
                mov.Ravancer(False,False,False,False,0,0)
            else:
                mov.avancer()


