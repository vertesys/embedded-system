#!/bin/bash
count=0
while [ $count -lt 10 ] ; do
    chmod +x /home/pi/.fantastics/monitoring/eZServerMonitor.sh
    /home/pi/.fantastics/monitoring/eZServerMonitor.sh -a > /home/pi/.fantastics/monitoring/temporary.html
    chmod +x /home/pi/.fantastics/monitoring/Convert.sh
    /home/pi/.fantastics/monitoring/Convert.sh
    chmod +x /home/pi/.fantastics/monitoring/Configure.sh
    /home/pi/.fantastics/monitoring/Configure.sh
    count=$[$count+1]
    sleep 5
done
