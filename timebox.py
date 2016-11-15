"""Sole author: Luke Hargraves"""

import time
import sys
import os
import datetime as dt

# def timebox(slots=[0, 0.25, 0.5, 0.75, 0.95, 1], phrases=[0,  "75 % Time Remaining", "50 % Time Remaining", "25 % Time Remaining", "5 % Time Remaining"]):
# 	"""Alerts user at useful intervals during work session, at customisable times"""
# 	print("Timebox Started at:", print_time)
# 	os.system('say "Timebox Initiated"')
# 	for i in range(len(slots)):
# 		if i <= (len(slots) -3):
# 			time.sleep(((slots[i+1]) - slots[i])*60*float(sys.argv[1]))
# 			n = (1-slots[i+1])
# 			print("Time Remaining: 		{:.0%}".format(100*n/100))
# 			os.system('say ' + phrases[i+1])
# 		else:
# 			time.sleep(((slots[i+1]) - slots[i])*60*float(sys.argv[1])) 
# 			print("Time is up.")
# 			os.system('say "Timebox Expired"')
# 			break
# 	return


# timebox()


def timebox(t = 60 * float(sys.argv[1]), ):
	os.system('say "Timebox Initiated"')
	print ("\tTimebox Started at: {:s}").format(time.strftime('%H:%M:%S', time.localtime()))
	print("\tTime Allocated: {:02.0f}:{:02.0f}\r".format(((t - t%60) / 60), (t%60)))
	while t >= 1:
		time.sleep(1)
		t -= 1
		if t%60 == 0 and t/60 > 1:
			print("\a{:10.0f}  Minutes Remaining        ").format(t/60)
		elif t%60 == 0 and t/60 == 1:
			print("\a{:10.0f}  Minute  Remaining        ").format(t/60)
		elif t == 1:
			sys.stdout.write("\tTime Remaining: 00:01\r")
			time.sleep(1)
			sys.stdout.flush()
			sys.stdout.write("\tTime Remaining: 00:00\r")
			sys.stdout.flush()
		else:
			sys.stdout.write("\tTime Remaining: {:02.0f}:{:02.0f}\r".format(((t - t%60) / 60), (t%60)))
			sys.stdout.flush()
	print("\n\tTime is up.                     ")
	os.system('say "Timebox Expired"')
	return

timebox()

