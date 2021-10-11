import RPi.GPIO as GPIO
import time
 
RED_LED_PIN = 13
BLUE_LED_PIN = 19
GREEN_LED_PIN = 26
PWM_FREQ = 200
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
 
red_pwm = GPIO.PWM(RED_LED_PIN, PWM_FREQ)
red_pwm.start(0)
blue_pwm = GPIO.PWM(BLUE_LED_PIN, PWM_FREQ)
blue_pwm.start(0)
green_pwm = GPIO.PWM(GREEN_LED_PIN, PWM_FREQ)
green_pwm.start(0)
 
def setColor(r=0, g=0, b=0):
    red_pwm.ChangeDutyCycle(100-int(r/255*100))
    blue_pwm.ChangeDutyCycle(100-int(b/255*100))
    green_pwm.ChangeDutyCycle(100-int(g/255*100))

def display(color):
    if color ==  1 :
        for i in range(0,30):
            setColor(255, 0, 0)
            time.sleep(1)
        #red
    elif color == 2 :
        for i in range(0,30):
            setColor(0, 0, 255)
            time.sleep(1)
        #blue
    elif color == 3 :
        for i in range(0,30):
            setColor(0, 255, 0)
            time.sleep(1)
        #green

#red_pwm.stop()
#blue_pwm.stop()
#green_pwm.stop()
#GPIO.cleanup()

"""
try:
    display(1)
    time.sleep(1)
    display(2)
    time.sleep(1)
    display(3)
    time.sleep(1)
except KeyboardInterrupt:
    print('OFF')
finally:
    red_pwm.stop()
    blue_pwm.stop()
    green_pwm.stop()
    GPIO.cleanup()
"""