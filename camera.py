import cv2
from picamera2 import Picamera2

piCam = Picamera2()
piCam.preview_configuration.main.size = (480,240)
piCam.preview_configuration.main.format = "RGB888"
#piCam.preview_configuration.align()
#config = piCam.preview_configuration(transform=libcamera.Transform(hflip=1, vflip=1))

piCam.configure("preview")
#piCam.start_preview(Preview.QTGL, transform=Transform(hflip=1))
#piCam.preview_configuration.transform =libcamera.Transform(hflip=1)
piCam.start()

def getImage(display = False):
    frame = piCam.capture_array()
    if display:
        cv2.imshow("piCam",frame)
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindow()
            
        return frame
        

if __name__ == '__main__':
    while True:
        image = getImage(True)

    
    


