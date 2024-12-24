import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
servo_bcm_pin = 13
FREQUENCY = 50
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_bcm_pin,GPIO.OUT)
pwm = GPIO.PWM(servo_bcm_pin,FREQUENCY)
pwm.start(7.5)

def setLimitAngle(angle,min_a=0,min_s=2.5, max_a=180,max_s = 12.5):
    result =(angle - min_a) *(max_s - min_s) / (max_a - min_a) + min_s
    return max(min(12.5, result),2.5)
    
    
    
    
    
def setAngle(angle):
    signal = setLimitAngle(angle)
    pwm.ChangeDutyCycle(signal)
    sleep(0.04)
    
"""
for i in range(5):
    for ang in range(40,140):
        setAngle(ang)
""" 


    


    
