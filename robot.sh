#!/bin/bash
######################################################################################
filename="programme.py"
######################################################################################
function robotusage() {
    echo -e "Usage :\n   $0 start|stop|restart|status\n" >&2 ; exit 0
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
        else 
            echo "- Le robot n'a pas pu être démarré."
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
        echo "+ Mise à jour du robot disponible." ; return 0
    fi
    echo "+ Mise à jour du robot non disponsible." ; return 1
}
function cancelupdate() {
    sleep 1; echo "+ Suppression de la mise à jour.";
    # git reset --hard) > /dev/null
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

