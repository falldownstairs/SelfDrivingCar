from PCA9685 import PCA9685
import time

pwm = PCA9685(0x40,debug=False)
pwm.setPWMFreq(50)

PWMA = 0 # motor-LEFT speed control
AIN1 = 1 # motor-LEFT direction control
AIN2 = 2 # motor-LEFT direction control

PWMB = 5 # motor-RIGHT speed control
BIN1 = 3 # motor-RIGHT direction control
BIN2 = 4 # motor-RIGHT direction control

STOP_LEVEL = 0
LOW_SPEED_LEVEL = 8  
MEDIUM_SPEED_LEVEL = 50
HIGH_SPEED_LEVEL = 75

def motorRightForward():
    pwm.setDutycycle(PWMB,LOW_SPEED_LEVEL)
    pwm.setLevel(BIN1,0)
    pwm.setLevel(BIN2,1)
    time.sleep(3)
    pwm.setDutycycle(PWMB,STOP_LEVEL)
    pwm.setLevel(BIN1,0)
    pwm.setLevel(BIN2,0)
    
    
def motorRightBackward():
    pwm.setDutycycle(PWMB,LOW_SPEED_LEVEL)
    pwm.setLevel(BIN1,1)
    pwm.setLevel(BIN2,0)
    time.sleep(3)
    pwm.setDutycycle(PWMB,STOP_LEVEL)
    pwm.setLevel(BIN1,0)
    pwm.setLevel(BIN2,0)
    
    
    
def motorLeftForward():
    pwm.setDutycycle(PWMA,LOW_SPEED_LEVEL)
    pwm.setLevel(AIN1,1)
    pwm.setLevel(AIN2,0)
    time.sleep(3)
    pwm.setDutycycle(PWMB,STOP_LEVEL)
    pwm.setLevel(AIN1,0)
    pwm.setLevel(AIN2,0)
    
    
def motorLeftBackward():
    pwm.setDutycycle(PWMA,LOW_SPEED_LEVEL)
    pwm.setLevel(AIN1,0)
    pwm.setLevel(AIN2,1)
    time.sleep(3)
    pwm.setDutycycle(PWMB,STOP_LEVEL)
    pwm.setLevel(AIN1,0)
    pwm.setLevel(AIN2,0)

def robotForward():
    pwm.setDutycycle(PWMB,LOW_SPEED_LEVEL)
    pwm.setDutycycle(PWMA,LOW_SPEED_LEVEL)
    pwm.setLevel(BIN1,0)
    pwm.setLevel(BIN2,1)
    pwm.setLevel(AIN1,1)
    pwm.setLevel(AIN2,0)
   
    
def robotBackward():
    pwm.setDutycycle(PWMB,MEDIUM_SPEED_LEVEL)
    pwm.setDutycycle(PWMA,MEDIUM_SPEED_LEVEL)
    pwm.setLevel(BIN1,1)
    pwm.setLevel(BIN2,0)
    pwm.setLevel(AIN1,0)
    pwm.setLevel(AIN2,1)
  



