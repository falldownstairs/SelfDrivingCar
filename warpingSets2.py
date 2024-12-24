import cv2
import numpy as np

WINDOW_WIDTH = 360
WINDOW_HEIGHT = 240
size = 15

def thresHold(image):
    image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lowerWhite = np.array([80, 0, 0])
    upperWhite = np.array([255, 160, 255])
    # this masks the white color area in the video
    maskWhite = cv2.inRange(image_HSV,lowerWhite, upperWhite)
    # to make sure if it works return masked version
    return maskWhite


def warpImage(image,points,width,height, inverse = False):
    pointOne = np.float32(points)
    pointTwo = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    if inverse:
       matrix = cv2.getPerspectiveTransform(pointTwo,pointOne)
    else:
        matrix = cv2.getPerspectiveTransform(pointOne,pointTwo)
        
    imageWarp = cv2.warpPerspective(image, matrix, (width, height))
    return imageWarp


def initializeTrackbars(intialTracbarVals,wT=480, hT=240):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 480, 240)
    cv2.createTrackbar("Width Top", "Trackbars", intialTracbarVals[0],wT//2, nothing)
    cv2.createTrackbar("Height Top", "Trackbars", intialTracbarVals[1], hT, nothing)
    cv2.createTrackbar("Width Bottom", "Trackbars", intialTracbarVals[2],wT//2, nothing)
    cv2.createTrackbar("Height Bottom", "Trackbars", intialTracbarVals[3], hT, nothing)
    
    
def valTrackbars(wT=480, hT=240):
    widthTop = cv2.getTrackbarPos("Width Top", "Trackbars")
    heightTop = cv2.getTrackbarPos("Height Top", "Trackbars")
    widthBottom = cv2.getTrackbarPos("Width Bottom", "Trackbars")
    heightBottom = cv2.getTrackbarPos("Height Bottom", "Trackbars")
    points = np.float32([(widthTop, heightTop), (wT-widthTop, heightTop),
                      (widthBottom , heightBottom ), (wT-widthBottom, heightBottom)])
    return points


def drawPoints(image, points):
    for x in range(4):
        cv2.circle(image, (int(points[x][0]), int(points[x][1])), size,(0, 0 ,255), cv2.FILLED)
    return image

def nothing(a):
    pass

if __name__ == '__main__':
    capture = cv2.VideoCapture(0)
    
    initialTrackBarValues = (100, 100, 100, 100)
    
    initializeTrackbars(initialTrackBarValues,480,240)
    
    while True:
        success, image = capture.read()
        heightWarp,widthWarp,channelWarp = image.shape
        
        imageCopy = image.copy()

        image = cv2.resize(image,(WINDOW_WIDTH,WINDOW_HEIGHT))
        
        points = valTrackbars()
        
        imageWarped = warpImage(image, points, widthWarp, heightWarp)
        
        imageWarpPoints = drawPoints(imageCopy, points)
        

        cv2.imshow('original video',imageWarpPoints)
        
        cv2.waitKey(1)
