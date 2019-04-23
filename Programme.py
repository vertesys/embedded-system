#!/usr/bin/env python3

# Import os, time and datetime modules.
import os, time, datetime
m..
while (True):
    file = open(os.path.expanduser("~/.robot/programme.txt"), "w")
    file.write(datetime.datetime.today().strftime("\tDATE : %d-%m-%Y\n"))
    file.write(datetime.datetime.now().strftime("\tHOUR : [%H:%M:%S]"))
    file.close()
    time.sleep(1)
