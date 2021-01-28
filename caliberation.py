import cv2 as cv
import numpy as np

def empty(x):
    pass
def caliberation():
    Lower=[]
    Upper=[]
    video = cv.VideoCapture(0)
    cv.namedWindow("caliberation")
    cv.createTrackbar('L_HUE','caliberation',0,179,empty)
    cv.createTrackbar('L_SAT','caliberation',0,255,empty)
    cv.createTrackbar('L_VAL','caliberation',0,255,empty)
    cv.createTrackbar('U_HUE','caliberation',0,179,empty)
    cv.createTrackbar('U_SAT','caliberation',0,255,empty)
    cv.createTrackbar('U_VAL','caliberation',0,255,empty)
    cv.setTrackbarPos('U_HUE','caliberation',179)
    cv.setTrackbarPos('U_SAT','caliberation',255)
    cv.setTrackbarPos('U_VAL','caliberation',255)

    while cv.waitKey(1)==-1:
        isTrue,frame = video.read()
        frame = cv.flip(frame,1)
        cv.imshow("FRAME",frame)
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        L_HUE=cv.getTrackbarPos('L_HUE','caliberation')
        L_SAT=cv.getTrackbarPos('L_SAT','caliberation')
        L_VAL=cv.getTrackbarPos('L_VAL','caliberation')
        U_HUE=cv.getTrackbarPos('U_HUE','caliberation')
        U_SAT=cv.getTrackbarPos('U_SAT','caliberation')
        U_VAL=cv.getTrackbarPos('U_VAL','caliberation')

        Lower = [L_HUE,L_SAT,L_VAL]
        Upper = [U_HUE,U_SAT,U_VAL]

        mask = cv.inRange(hsv,np.array(Lower),np.array(Upper))
        cv.imshow("Mask",mask)
    video.release()
    cv.destroyAllWindows()
    return Lower,Upper
if __name__ == '__main__':
    print(caliberation())
    