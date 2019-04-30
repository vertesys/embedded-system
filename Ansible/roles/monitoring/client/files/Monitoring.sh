#!/bin/bash
count=0
while [ $count -le 14 ] ; do
    content=$(/home/pi/.fantastics/monitoring/eZServerMonitor.sh -a)
    echo $content > /home/pi/.fantastics/monitoring/temporary.html
    /home/pi/.fantastics/monitoring/Convert.sh
    # $(/home/pi/.fantastics/monitoring/Configure.sh > /dev/null 2>&1)
    /home/pi/.fantastics/monitoring/Configure.sh
    count=$[$count+1]
done
