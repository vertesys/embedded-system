#!/bin/bash
count=0
while [ $count -le 11 ] ; do
    # chmod +x /home/pi/.fantastics/monitoring/eZServerMonitor.sh
    /home/pi/.fantastics/monitoring/eZServerMonitor.sh -a > /home/pi/.fantastics/monitoring/temporary.html
    # chmod +x /home/pi/.fantastics/monitoring/Convert.sh
    sleep 2
    /home/pi/.fantastics/monitoring/Convert.sh
    # chmod +x /home/pi/.fantastics/monitoring/Configure.sh
    /home/pi/.fantastics/monitoring/Configure.sh
    count=$[$count+1]
done
