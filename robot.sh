#!/bin/bash
######################################################################################
filename="robot.py"
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
case "$1" in
    status) robotstatus ;;
         *) robotusage ;;
esac
######################################################################################

