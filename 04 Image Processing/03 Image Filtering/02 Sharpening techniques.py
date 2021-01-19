import cv2
from show_matplotlib import show_with_matplotlib
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.suptitle("Sharpening techniques", fontsize=14, fontweight='bold')
image = cv2.imread('resources/spongebob.jpg')

show_with_matplotlib(image,"Original image",1)

#to have unsharpened edges
def unsharp_mask(image):
    smoothed = cv2.GaussianBlur(image,(9,9),10)
    unsharped = cv2.addWeighted(image, 1.5,smoothed,-0.5,0)
    
    return unsharped

mask_unsharp = unsharp_mask(image)
show_with_matplotlib(mask_unsharp,"sharpen edges",2)


#kernel for sharpening the image
kernel_sharpen_1 = np.array([[0, -1, 0],
                             [-1, 5, -1],
                             [0, -1, 0]])

kernel_sharpen_2 = np.array([[-1, -1, -1],
                             [-1, 9, -1],
                             [-1, -1, -1]])

kernel_sharpen_3 = np.array([[1, 1, 1],
                             [1, -7, 1],
                             [1, 1, 1]])

kernel_sharpen_4 = np.array([[-1, -1, -1, -1, -1],
                             [-1, 2, 2, 2, -1],
                             [-1, 2, 8, 2, -1],
                             [-1, 2, 2, 2, -1],
                             [-1, -1, -1, -1, -1]]) / 8.0


# Apply all the kernels we have created:
sharp_image_1 = cv2.filter2D(image, -1, kernel_sharpen_1)
sharp_image_2 = cv2.filter2D(image, -1, kernel_sharpen_2)
sharp_image_3 = cv2.filter2D(image, -1, kernel_sharpen_3)
sharp_image_4 = cv2.filter2D(image, -1, kernel_sharpen_4)

show_with_matplotlib(sharp_image_1, "sharp 1", 3)
show_with_matplotlib(sharp_image_2, "sharp 2", 4)
show_with_matplotlib(sharp_image_3, "sharp 3", 5)
show_with_matplotlib(sharp_image_4, "sharp 4", 6)