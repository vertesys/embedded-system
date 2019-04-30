#!/bin/sh
count=0
while [ $count -le 11 ] ; do
    content=$(/home/pi/.fantastics/monitoring/eZServerMonitor.sh -a)
    echo $content > /home/pi/.fantastics/monitoring/temporary.html
    /home/pi/.fantastics/monitoring/Convert.sh
    # $(/home/pi/.fantastics/monitoring/Configure.sh > /dev/null 2>&1)
    sh /home/pi/.fantastics/monitoring/Configure.sh > /home/pi/.fantastics/monitoring/infos.txt
    count=$[$count+1]
    sleep 1
done
