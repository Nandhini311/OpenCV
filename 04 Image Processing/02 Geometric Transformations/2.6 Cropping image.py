import cv2
from show_matplotlib import show_with_matplotlib
import numpy as np


image = cv2.imread('resources/lena_image.png')
height, width = image.shape[:2]


#showing the points that are seen by perspective trans
image_points = image.copy()

# Show the points and lines connecting the points:
cv2.circle(image_points, (230, 80), 5, (0, 0, 255), -1)
cv2.circle(image_points, (330, 80), 5, (0, 0, 255), -1)
cv2.circle(image_points, (230, 200), 5, (0, 0, 255), -1)
cv2.circle(image_points, (330, 200), 5, (0, 0, 255), -1)
cv2.line(image_points, (230, 80), (330, 80), (0, 0, 255))
cv2.line(image_points, (230, 200), (330, 200), (0, 0, 255))
cv2.line(image_points, (230, 80), (230, 200), (0, 0, 255))
cv2.line(image_points, (330, 200), (330, 80), (0, 0, 255))

# Show the image with the points and lines:
show_with_matplotlib(image_points, 'to be cropped')

# For cropping, we make use of numpy slicing:
dst_image = image[80:200, 230:330]

# Show the image:
show_with_matplotlib(dst_image, 'Cropped image')