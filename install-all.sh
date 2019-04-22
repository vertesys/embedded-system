#!/bin/bash
private_key=~/.ssh/id_rsa.robot
if [ ! -f $private_key ]; then
    yes y | ssh-keygen -f $private_key -q -N "" > /dev/null
    ansible-playbook --user pi -k -b -i inventory.inv playbooks/install-user.yml
fi
ansible-playbook -u deploy -b --private-key $private_key -i inventory.inv playbook.yml
