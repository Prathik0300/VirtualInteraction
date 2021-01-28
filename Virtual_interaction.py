import cv2 as cv
import numpy as np
from caliberation import caliberation
import pyautogui as gui

def rescale(frame,scale=1.25):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_CUBIC)

    
gui.FAILSAFE = False
Lower,Upper = caliberation()
video = cv.VideoCapture(0)
isTrue=1
x0,y0=0,0

point_color = (0,0,255)
select_color = (0,255,0)
#cv.namedWindow('frame', cv.WINDOW_NORMAL)
#cv.setWindowProperty('frame', cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
count=1
while isTrue==1:
    isTrue,frame = video.read()
    if count==1:
        blank = np.zeros(frame.shape[:2],dtype='uint8')
        count+=1
    frame = cv.flip(frame,1)
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv,np.array(Lower),np.array(Upper))
    erode = cv.erode(mask,(5,5),iterations=2)
    contour,hierarchy = cv.findContours(erode,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    if contour:
        c = max(contour,key=cv.contourArea)
        x,y,w,h = cv.boundingRect(c)
        cv.rectangle(erode,(x,y),(x+w,y+h),(255,255,255),thickness=2)
        #cv.line(erode,((x+w//2),(y+h//2)),(0,0),(255,0,0),4)

        x0,y0=(x+w//2)*5,(y+h//2)*4
        gui.moveTo(x0,y0,duration=1.5)
        show = cv.bitwise_or(blank,erode)
        cv.imshow("frame",show)
        if cv.waitKey(1) & 0xFF==ord('s'):
            print(x0,y0)
            gui.doubleClick(x0,y0)
    else:
        x0,y0=0,0
    if cv.waitKey(1) & 0xFF==ord('a'):
        break    
video.release()
cv.destroyAllWindows()