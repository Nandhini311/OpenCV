import numpy as np
from show_matplotlib import show_with_matplotlib
import cv2

#Rotation
#cv2.getRotationMatrix2D()
#positive value-counterclockwise rotation
#center and scale factor can be adjusted

image = cv2.imread('resources/lena_image.png')
height, width = image.shape[:2]
#step 1: build 2x3 transformation matrix
#center, rotation degree, scale
M = cv2.getRotationMatrix2D((width/2.0,height/2.0),180,1)
dst_image = cv2.warpAffine(image, M, (width, height))

#marking the circle
cv2.circle(dst_image, (round(width / 2.0), round(height / 2.0)), 5, (255, 0, 0), -1)
show_with_matplotlib(dst_image, 'Image rotated 180 degrees')

#rotating by 30 degree
M = cv2.getRotationMatrix2D((width/1.5,height/1.5),30,1)
dst_image = cv2.warpAffine(image, M, (width, height))

cv2.circle(dst_image, (round(width/1.5), round(height/1.5)),5,(255,0,0),-1)
show_with_matplotlib(dst_image,'Image rotated 30 degrees')