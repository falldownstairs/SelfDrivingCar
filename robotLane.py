import webcamPi
import laneDetection
import cv2
sensitivity = 1.1
def main():
    image = webcamPi.getImage()
    curveVal = laneDetection.getLaneCurve(image, 2)
    curveVal = curveVal * sensitivity
    print("angle is",curveVal)
    cv2.waitKey(1)
if __name__ =='__main__':
    while True:
        main()
