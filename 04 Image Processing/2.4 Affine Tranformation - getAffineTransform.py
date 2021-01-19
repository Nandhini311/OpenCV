import cv2
from show_matplotlib import show_with_matplotlib
import numpy as np


image = cv2.imread('resources/lena_image.png')
height, width = image.shape[:2]

#4.Affine Transformation - preserves lines and parallelism, not necessarily distances and angles
#cv2.getAffineTransform() to build 2x3 matrix

image_copy = image.copy()
cv2.circle(image_copy, (135, 45), 5, (0, 0, 0), -1)
cv2.circle(image_copy, (385, 45), 5, (0, 0, 0), -1)
cv2.circle(image_copy, (135, 230), 5, (0, 0, 0), -1)

show_with_matplotlib(image_copy, "Points to be tranformed")

#creating a vector with before mentioned points
pts_1 = np.float32([[135, 45], [385, 45], [135, 230]])
pts_2 = np.float32([[135, 45], [385, 45], [150, 230]])


M = cv2.getAffineTransform(pts_1, pts_2)
dst_image = cv2.warpAffine(image_copy, M, (width, height))


#showing the image
show_with_matplotlib(dst_image,"Affine Transformation")