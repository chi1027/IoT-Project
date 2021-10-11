import time
import RPi.GPIO as GPIO
import mcs_upload_other 
import mcs_get_other 
import Line_notifier as notifier

value1 = mcs_get_other.status('ldr_display')
value2 = mcs_get_other.status('soil_display')
value3 = mcs_get_other.status('celsius')
value4 = mcs_get_other.status('air_dis')
notifier.line_message("\nLdr(%)  :" + str(value1) + "\nSoil(%) :" + str(value2) + "\nTemp :" + str(value3) + "\nAir Quality(%) :" + str(value4))

