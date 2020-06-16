#!/usr/bin/env python3.8
import time

input("Press enter to start the timer.")
startTime = time.localtime()
print(f"Timer started at {time.strftime('%X', startTime)}")

input("Press enter to stop the timer.")
endTime = time.localtime()
print(f"Timer stopped at {time.strftime('%X', endTime)}")

diff = time.mktime(endTime) - time.mktime(startTime)
print(f"The difference was {diff} seconds")