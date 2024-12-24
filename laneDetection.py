import cv2
import numpy as np
import functions

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 240

curveList = []
averageValue = 10

def getLaneCurve(image, display=2):
    
    imageCopy = image.copy()
    imgResult = image.copy()
    # STEP-1 --> THRESHOLDING
    imageThresholded = functions.thresHold(image)
    
    # STEP-2 --> WARPING
    heightWarp,widthWarp,channelWarp = image.shape
    intialTracbarVals = [80,120,0,480]
    functions.initializeTrackbars(intialTracbarVals)

    points = functions.valTrackbars()
    imageWarped = functions.warpImage(imageThresholded, points, widthWarp, heightWarp)
    imageWarpPoints = functions.drawPoints(imageCopy, points)
    
    # STEP-3 --> WARPING
    middlePoint, imageHist = functions.getHistogram(imageWarped, display=True, minPer = 0.5, region=4)
    curveAveragePoint, imageHist = functions.getHistogram(imageWarped, display=True, minPer = 0.9)
    curveRaw = curveAveragePoint - middlePoint
    
    #STEP-4 --> AVERAGING
    curveList.append(curveRaw)
    if len(curveList) > averageValue:
        curveList.pop(0)
    curve = int(sum(curveList)/len(curveList))
    # convert the angle value 40 -140
    #STEP-5 --> DISPLAY
    if display != 0:
       imgInvWarp = functions.warpImage(imageWarped, points, widthWarp, heightWarp,inverse = True)
       imgInvWarp = cv2.cvtColor(imgInvWarp,cv2.COLOR_GRAY2BGR)
       imgInvWarp[0:heightWarp//3,0:widthWarp] = 0,0,0
       imgLaneColor = np.zeros_like(image)
       imgLaneColor[:] = 0, 255, 0
       imgLaneColor = cv2.bitwise_and(imgInvWarp, imgLaneColor)
       imgResult = cv2.addWeighted(imgResult,1,imgLaneColor,1,0)
       midY = 450
       cv2.putText(imgResult,str(curve),(widthWarp//2-80,85),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),3)
       cv2.line(imgResult,(widthWarp//2,midY),(widthWarp//2+(curve*3),midY),(255,0,255),5)
       cv2.line(imgResult, ((widthWarp // 2 + (curve * 3)), midY-25), (widthWarp // 2 + (curve * 3), midY+25), (0, 255, 0), 5)
       for x in range(-30, 30):
           w = widthWarp // 20
           cv2.line(imgResult, (w * x + int(curve//50 ), midY-10),
                    (w * x + int(curve//50 ), midY+10), (0, 0, 255), 2)
       #fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
       #cv2.putText(imgResult, 'FPS '+str(int(fps)), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (230,50,50), 3);
    if display == 2:
       imgStacked = functions.stackImages(0.7,([image,imageWarpPoints,imageWarped],
                                         [imageHist,imgLaneColor,imgResult]))
       cv2.imshow('ImageStack',imgStacked)
    elif display == 1:
       cv2.imshow('Resutlt',imgResult)
    
    # NORMALIZATION
    #curve = curve/100
    #if curve > 1: curve = 1
    #if curve < -1: curve = -1
    #cv2.imshow('thresholding',imageThresholded)
    #cv2.imshow('warping',imageWarped)
    #cv2.imshow('warping with points',imageWarpPoints)
    #cv2.imshow('histogram',imageHist)
    #THIS CODE CONVERTS THE RANGE
    #curve = int((5 / 9) * curve + 90)
    #if curve<0:curve=90+curve
    #if curve>0:curve=90
    curve = curve + 90
    print("curve is",curve)
    return curve
    



if __name__ == '__main__':
    #capture = cv2.VideoCapture('example.mp4')
    capture = cv2.VideoCapture(0)

    
    initialTrackBarValues = (102, 80, 20, 214)
    functions.initializeTrackbars(initialTrackBarValues)
        
    while True:
        success, image = capture.read()
        image = cv2.resize(image,(WINDOW_WIDTH,WINDOW_HEIGHT))
        
        # show masked video
        curve = getLaneCurve(image,display = 1)
        
        # show original video
        cv2.imshow('original video',image)
        cv2.waitKey(1)
        
