import time

input("Press enter to start the timer.")
startTime = time.localtime()

input("Press enter to stop the timer.")
endTime = time.localtime()

diff = time.mktime(endTime) - time.mktime(startTime)

print(diff)
