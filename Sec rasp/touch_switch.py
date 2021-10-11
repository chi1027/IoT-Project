import RPi.GPIO as GPIO
import time
import mcs_upload_other

O1_PIN = 22
O2_PIN = 27
O3_PIN = 17
O4_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(O1_PIN, GPIO.IN)
GPIO.setup(O2_PIN, GPIO.IN)
GPIO.setup(O3_PIN, GPIO.IN)
GPIO.setup(O4_PIN, GPIO.IN)
global count = 0

while True :
    try:
        if GPIO.input(O1_PIN)==GPIO.HIGH :
            if(count == 1) : continue
            count = 1
            mcs_upload_other.post_to_mcs('mode', 1)
            print("manual mode")
        elif GPIO.input(O2_PIN)==GPIO.HIGH :
            if(count == 2) : continue
            count = 2
            mcs_upload_other.post_to_mcs('mode', 0)
            print("auto mode")
        elif GPIO.input(O3_PIN)==GPIO.HIGH :
            if(count == 3) : continue
            count = 3
            mcs_upload_other.post_to_mcs('man_ctl', 1)
            print("manual on")
        elif GPIO.input(O4_PIN)==GPIO.HIGH :
            if(count == 4) : continue
            count = 4
            mcs_upload_other.post_to_mcs('man_ctl', 0)
            print("manual off")  
        time.sleep(1)
    except KeyboardInterrupt:
        print("end")

def solve():
    if count == 1:
        return 1
    if count == 2:
        return 2
    if count == 3:
        return 3
    if count == 4:
        return 4
