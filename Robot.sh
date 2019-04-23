#!/bin/bash
######################################################################################
function oneinstance() {
    pids=$(ps aux | grep -i bash.*$(basename "$0") | grep -v grep | awk '{print $2}')
    for pid in $pids ; do 
        if [ $$ -ne $pid ] ; then kill -9 $pid > /dev/null 2>&1 ; fi
    done
} ; oneinstance
function variables() {
    directory="." ; script_py="Programme.py" ; mkdir ~/.robot/ > /dev/null 2>&1
    sha_1_robot_works=~/.robot/sha-1-robot-works ; touch $sha_1_robot_works
    sha_1_robot_error=~/.robot/sha-1-robot-error ; touch $sha_1_robot_error
    file_informations=~/.robot/informations ; > $file_informations
}
######################################################################################
function robotusage() {
    echo -e "Usage :\n   $0 auto|start|stop|restart|status\n" >&2 ; exit 0
}
function robotstatus() {
    if (ps aux | grep -i "python.*$script_py" | grep -v grep) > /dev/null ; then
        echo "- Le robot est en fonctionnement." ; return 0
    else
        echo "- Le robot n'est pas en fonctionnement." ; return 1
    fi
}
######################################################################################
function robotstart() {
    if ! robotstatus > /dev/null ; then
        ($directory/$script_py &) ; sleep 1
        if robotstatus > /dev/null ; then
            echo "- Le robot a été démarré."
            echo $(git -C $directory rev-parse HEAD) > $sha_1_robot_works
        else 
            echo "- Le robot n'a pas pu démarré."
            echo $(git -C $directory rev-parse HEAD) > $sha_1_robot_error
        fi
    else
        sleep 1 ; echo "- Le robot a été déjà démarré."
    fi
}
function robotstop() {
    if robotstatus > /dev/null ; then
        pids=$(ps aux | grep -i python.*$script_py | grep -v grep | awk '{print $2}')
        (echo $pids | xargs kill -9 $1) > /dev/null 2>&1 ; sleep 1
        echo "- Le robot a été arrêté."
    else
        sleep 1 ; echo "- Le robot a été déjà arrêté."
    fi
}
######################################################################################
function checkupdate() {
    url_remote=$(git -C $directory config --get remote.origin.url)
    sha_1_last_commit_online=$(git -C $directory ls-remote $url_remote HEAD | cut -f1)
    if [ "$sha_1_last_commit_online" != "$(git -C $directory rev-parse HEAD)" ] ; then
        #if [ "$sha_1_last_commit_online" != head -n 1 $sha_1_robot_error ] ; then
            echo "+ Mise à jour du robot disponible." ; return 0
        #fi
    fi
    echo "+ Mise à jour du robot non disponsible." ; return 1
}
function cancelupdate() {
    sleep 1; echo "+ Suppression de la mise à jour.";
    git -C $directory reset --hard $(cat $sha_1_robot_works) > /dev/null 2>&1
}
function applyupdate() {
    sleep 1; echo "- Application de la mise à jour.";
    git -C $directory pull > /dev/null 2>&1
}
######################################################################################
function autoupdate() {
    variables ; sleep 1 ; (robotstatus | tr - +) > $file_informations ; sleep 1
    if checkupdate ; then
        echo -n "  " ; robotstop
        echo -n "  " ; applyupdate
        echo -n "  " ; robotstart ; sleep 1
        if ! robotstatus > /dev/null 2>&1 ; then
            echo -n "  " ; cancelupdate 
            echo -n "    " ; robotstart
        fi
    else
        if ! robotstatus > /dev/null 2>&1 ; then
            echo -n "  " ; robotstart ; sleep 1
            if ! robotstatus > /dev/null 2>&1 ; then
                echo -n "  " ; cancelupdate 
                echo -n "    " ; robotstart
            fi
        fi
    fi
} >> /home/deploy/.robot/informations
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
