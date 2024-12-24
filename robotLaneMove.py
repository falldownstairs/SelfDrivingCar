import webcamPi
import laneDetection
import cv2
from servoControl import setAngle
from motorControl import robotForward
from PCA9685 import PCA9685
import time
def main():
    image = webcamPi.getImage()
    curveVal = laneDetection.getLaneCurve(image, 1)
    sensitivity = 0.8
    curveVal = curveVal * sensitivity
    if curveVal<40:curveVal=40
    if curveVal>140:curveVal=140
    robotForward()
    setAngle(curveVal)
    cv2.waitKey(1)
if __name__ =='__main__':
    while True:
        main()
