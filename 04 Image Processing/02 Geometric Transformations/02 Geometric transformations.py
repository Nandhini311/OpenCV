import cv2
import numpy as np
import matplotlib.pyplot as plt
from show_matplotlib import show_with_matplotlib
'''Two key functions to perform geometric transformations
are cv2.warpAffine() and cv2.wrapPerspective()'''
  
image = cv2.imread('resources/lena_image.png')
height, width = image.shape[:2]

#show loaded image
show_with_matplotlib(image, "Original image")

#Translation 
#Step 1: create 2x3 transformation matrix
#translation in the x direction: 200 pixels and a translation in the y direction: 30 pixels
M = np.float32([[1, 0, 200], [0, 1, 30]])

# Once this transformation Matrix is created, we can pass it to the function cv2.warpAffine():
dst_image = cv2.warpAffine(image, M, (width, height))

# Show the translated image:
show_with_matplotlib(dst_image, 'Translated image (positive values)')

N = np.float32([[1, 0, -200], [0, 1, -30]])

dst_image1 = cv2.warpAffine(image, N, (width, height))

show_with_matplotlib(dst_image1, 'Translated image (negative values)')
