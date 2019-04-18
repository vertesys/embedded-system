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
######################################################################################
case "$1" in
      stop) robotstop ;;
     start) robotstart ;;
    status) robotstatus ;;
         *) robotusage ;;
esac
######################################################################################

