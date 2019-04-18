#!/bin/bash
######################################################################################
sha_1_commit_ok=~/.sha-1-commit-ok ; touch $sha_1_commit_ok
sha_1_commit_no=~/.sha-1-commit-no ; touch $sha_1_commit_no
filename="programme.py"
######################################################################################
function robotusage() {
    echo -e "Usage :\n   $0 auto|start|stop|restart|status\n" >&2 ; exit 0
} 
######################################################################################
function robotstatus() {
    if (pgrep -f "$filename") > /dev/null ; then
        echo "- Le robot est en fonctionnement." ; return 0
    else
        echo "- Le robot n'est pas en fonctionnement." ; return 1
    fi
}
######################################################################################
function robotstart() {
    if ! robotstatus > /dev/null ; then
        $(nohup python $filename > /dev/null 2>&1 &) ; sleep 1
        if robotstatus > /dev/null ; then
            echo "- Le robot a été démarré."
            echo $(git rev-parse HEAD) > $sha_1_commit_ok
        else 
            echo "- Le robot n'a pas pu être démarré."
            echo $(git rev-parse HEAD) > $sha_1_commit_no
        fi
    else
        sleep 1 ; echo "- Le robot a été déjà démarré."
    fi
}
function robotstop() {
    if robotstatus > /dev/null ; then 
        pkill -f "$filename" > /dev/null 2>&1 ; sleep 1
        echo "- Le robot a été arrêté."
    else
        sleep 1 ; echo "- Le robot a été déjà arrêté."
    fi
}
######################################################################################
function checkupdate() {
    git fetch origin > /dev/null 2>&1
    reslog=$(git log HEAD..origin/master --oneline) > /dev/null
    if [ "${reslog}" != "" ] ; then
        if [ "$(git rev-parse HEAD)" != "$(cat $sha_1_commit_no)" ] ; then
            echo "+ Mise à jour du robot disponible." ; return 0
        fi
    fi
    echo "+ Mise à jour du robot non disponsible." ; return 1
}
function cancelupdate() {
    sleep 1; echo "+ Suppression de la mise à jour.";
    (cat $sha_1_commit_ok | git reset --hard) > /dev/null
}
function applyupdate() {
    sleep 1; echo "- Mise à jour en cours...";
    git merge origin/master > /dev/null 2>&1
}
######################################################################################
function autoupdate() {
    if robotstatus > /dev/null ; then 
        robotstop > /dev/null; robotstart; 
    fi
    while true ; do
        if checkupdate ; then
            echo -n "  "; robotstop 
            echo -n "  "; applyupdate
            echo -n "  "; robotstart
            sleep 1;
            if ! robotstatus > /dev/null ; then
                echo -n "  "; cancelupdate
                echo -n "    "; robotstart
            fi
        fi
        sleep 3
    done   
}
######################################################################################
case "$1" in
       stop) robotstop ;;
       auto) autoupdate ;;
      start) robotstart ;;
     status) robotstatus ;;
    restart) robotstop; robotstart ;;
          *) robotusage ;;
esac
######################################################################################
