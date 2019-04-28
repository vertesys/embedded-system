# Système embarqué
Déploiement d'un robot sur un système embarqué basé sur un Raspberry Pi.

## Mise en place du robot
*Mise en place du robot avec mise à jour automatique.*
```bash
Ansible/install-all.sh
```

## Système de monitoring
*Mise en place du monitoring du raspberry via le réseau.*
```bash
Ansible/install-all.sh
```

## Liste des tâches
- [x] Initialisation du structure du projet.
- [x] Prise en compte du mise à jour automatique du robot.
- [x] Configurer git pour faire du pulling sur ce repository privé.
- [ ] Mise en place d'un système de monitoring (envoi des métriques).
- [ ] \(Optionel) Ajout de l'utilisateur deploy (sudoers + clé SSH).


