import cv2
from show_matplotlib import show_with_matplotlib
import numpy as np


image = cv2.imread('resources/lena_image.png')
height, width = image.shape[:2]


#showing the points that are seen by perspective trans
image_points = image.copy()
cv2.circle(image_points, (450, 65), 5, (255, 0, 255), -1)
cv2.circle(image_points, (517, 65), 5, (255, 0, 255), -1)
cv2.circle(image_points, (431, 164), 5, (255, 0, 255), -1)
cv2.circle(image_points, (552, 164), 5, (255, 0, 255), -1)


show_with_matplotlib(image_points,"points to be transformed")

# cv2.getPerspectiveTransform() needs four pairs of points
# (coordinates of a quadrangle in both the source and output image)
pts_1 = np.float32([[450,65],[517,65],[431,164],[552,164]]) #source
pts_2 = np.float32([[0,0],[300,0],[0,300],[300,300]]) #output

M = cv2.getPerspectiveTransform(pts_1,pts_2)
dst_image = cv2.warpPerspective(image, M, (300, 300))


show_with_matplotlib(dst_image, 'perspective transformation')