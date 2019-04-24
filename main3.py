import ModuleLancement as deb
import ModuleMouvement as mouv
import ModuleDistance as dis


import ModulePresence as pres
import ModuleEcran as ecran

from time import sleep

# lancement = deb.Lancement()
# lancement.CheckRobot()
afecran = ecran.Ecran()
# mov = mouv.Mouvements()
objetDistance = dis.Distance()
# presence = pres.Presence()

while True:
    afecran.text('coucou mathieu')

