# Import time for sleep.
import time, datetime

# While loop
while (True):
    file = open("Time.txt", "w")
    file.write(datetime.datetime.now().strftime(" %H:%M:%S").join("\n"))
    file.close()
    time.sleep(1)

# Change de code
