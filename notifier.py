import datetime
import time
import win10toast

def toast():
	toaster=win10toast.ToastNotifier()
	toaster.show_toast('Python', "Hey! How bout some water huh?")

while True:
	curr= datetime.datetime.now()
	hour=curr.hour
	if curr.hour == hour:
		toast()
		hour = hour+2
		time.sleep((2*60*60)
