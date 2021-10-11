import RPi.GPIO as GPIO
import time
import mcs_upload_other

mcs_upload_other.post_to_mcs('mode', 1)
time.sleep(1)
mcs_upload_other.post_to_mcs('man_ctl', 1)