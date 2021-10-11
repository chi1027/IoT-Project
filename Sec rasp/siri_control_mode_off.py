import RPi.GPIO as GPIO
import time
import mcs_upload_other

mcs_upload_other.post_to_mcs('mode', 0)