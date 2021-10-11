import time
import RPi.GPIO as GPIO
import mcs_upload_other 
import Line_notifier as notifier
status = 0
RAIN = 1 
SUN = 0
pin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin ,GPIO.IN)
try :
	if GPIO.input(pin)==GPIO.LOW :
		notifier.line_message("It's raining.")
		status = RAIN 
		mcs_upload_other.post_to_mcs('rain',1)
		print("It's raining.")
			
	else :
		notifier.line_message("It's sunny.")
		status = SUN
		mcs_upload_other.post_to_mcs('rain',0)
		print("It's sunny.")

	while True :
		if GPIO.input(pin)==GPIO.LOW:
			if status == SUN :
				notifier.line_message("It's raining.")
				status = RAIN 
				mcs_upload_other.post_to_mcs('rain',1)
				print("It's raining.")
			
		else :
			if status == RAIN :
				notifier.line_message("It's sunny.")
				status = SUN
				mcs_upload_other.post_to_mcs('rain',0)
				print("It's sunny.")
		time.sleep(20)
except KeyboardInterrupt:
	print("close")  	 
