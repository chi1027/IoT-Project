import RPi.GPIO as GPIO
import time
import Line_notifier as notifier
import mcs_get_other
import RGB_LED


                           
while True:
    now_hour=int(time.strftime("%H"))
    now_min=int(time.strftime("%M")) 
    now_sec=int(time.strftime("%S")) 

    if(now_hour == 8 and now_min== 0 and now_sec < 5):
        value1 = mcs_get_other.status('celsius')
        value2 = mcs_get_other.status('air_dis')
        notifier.line_message("\nTemp  :" + str(value1) + "\nAir Quality(%)  :" + str(value2))

    value = mcs_get_other.status('soil_led')
    RGB_LED.display(int(value))
    time.sleep(1)