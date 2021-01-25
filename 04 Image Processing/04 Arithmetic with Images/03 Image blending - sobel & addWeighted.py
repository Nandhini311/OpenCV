import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_with_matplotlib(color_img, title, pos):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB
    img_RGB = color_img[:, :, ::-1]

    ax = plt.subplot(1, 4, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')
    
image = cv2.imread('resources/lena_image.png')

#filter the image with guassianBlur
image_filtered = cv2.GaussianBlur(image, (3,3), 0)

gray_image = cv2.cvtColor(image_filtered, cv2.COLOR_BGR2GRAY)
#image blending = image addition with different weights, gives an impression of transperancy

#sobel - to get edges, uses two 3x3 kernel convolved with the original image
#to calculate the approx derivates, capturizing
#verticcl and horizontal changes

#CV_16S = one channel of 2-byte signed integers
#to avoid overflow
gradient_x = cv2.Sobel(gray_image, cv2.CV_16S, 1, 0, 3)
gradient_y = cv2.Sobel(gray_image, cv2.CV_16S, 0, 1, 3)

#conversion to unsigned 8-bit type
abs_gradient_x = cv2.convertScaleAbs(gradient_x)
abs_gradient_y = cv2.convertScaleAbs(gradient_y)

sobel_image = cv2.addWeighted(abs_gradient_x, 0.5, abs_gradient_y,0.5, 0)

show_with_matplotlib(image, "Image", 1)
show_with_matplotlib(cv2.cvtColor(abs_gradient_x, cv2.COLOR_GRAY2BGR), "Gradient x", 2)
show_with_matplotlib(cv2.cvtColor(abs_gradient_y, cv2.COLOR_GRAY2BGR), "Gradient y", 3)
show_with_matplotlib(cv2.cvtColor(sobel_image, cv2.COLOR_GRAY2BGR), "Sobel output", 4)

# Show the Figure:
plt.show()