import cv2
import numpy as np
from matplotlib import pyplot as plt
from show_matplotlib import show_with_matplotlib, colors


image = np.zeros((400,400,3),dtype='uint8')
#drawing ellipses
#parameters- image, center, axes(size of the ellipse corresponding to half the size of the axes ), 
#angle(rotate the ellipse), startAngle, endAngle, color, thickness=1, lineType=8, shift=0 
cv2.ellipse(image, (80,80),(40,40),0,0,360,colors['red'],-1)
cv2.ellipse(image, (200,200),(10,40),0,0,180,colors['yellow'],3)
cv2.ellipse(image, (200,100), (20,40), 45, 0, 360, colors['gray'],3)

#drawing polygons
#points define a triangle
pts = np.array([[250,150],[220,200],[280,200]], np.int32)
#reshape to shape(number_vertex, 1, 2)
pts = pts.reshape((-1,1,2))
cv2.polylines(image, [pts], True, colors['green'],3) #True-isClosed polygon

#pentagon
pts = np.array([[20, 180], [60, 150], [100, 180], [80, 220], [40, 220]], np.int32)
# Reshape to shape (number_vertex, 1, 2)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(image, [pts], True, colors['white'],3)
show_with_matplotlib(image,"advanced shapes")
