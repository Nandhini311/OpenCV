import numpy as np
import cv2
from show_matplotlib import show_with_matplotlib, colors



#handling mouseevents

#cv2.setMouseCallback(windowName, onMouse, param=None)

#step 1:creating a callback function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("event: left button double click")
        cv2.circle(image, (x,y), 10, colors[magenta],-1)
        
    if event == cv2.EVENT_MOUSEMOVE:
        print("event: EVENT_MOUSEMOVE")
        
    if event == cv2.EVENT_LBUTTONUP:
        print("event: EVENT_LBUTTONUP")
   
    if event == cv2.EVENT_LBUTTONDOWN:
        print("event: EVENT_LBUTTONDOWN")
        
#step 2: creating a window
cv2.namedWindow('Image mouse')

#step 3: activate the mouse callbakc function to the fucntion we have created
cv2.setMouseCallback('Image mouse', draw_circle)