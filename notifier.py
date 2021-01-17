import datetime
import time
import win10toast

def toast():
	toaster=win10toast.ToastNotifier()
	toaster.show_toast('Python', "Hey! How bout some waters huh?")

while True:
	curr= datetime.datetime.now()
	minit=curr.minute
	if curr.minute == minit:
		toast()
		minitmd = minit+2
		time.sleep(7200)