import cv2
import matplotlib.pyplot as plt
import numpy as np

def show_with_matplotlib(image, title,pos):
    img_RGB = image[:, :, ::-1]

    ax = plt.subplot(2,3 , pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')
    


# Create the dimensions of the figure and set title:
plt.figure(figsize=(12, 6))
plt.suptitle("Arithmetic with images", fontsize=14, fontweight='bold')

image = cv2.imread('resources/lena_image.png')

show_with_matplotlib(image, 'original image', 1)

M = np.ones(image.shape, dtype='uint8')*60
added_image = cv2.add(image, M)

show_with_matplotlib(added_image, 'added image', 2)

scalar = np.ones((1,3),dtype='float')*110
added_image1 = cv2.add(image, scalar)

show_with_matplotlib(added_image1, 'added image scalar', 3)

subtracted_image = cv2.subtract(image, M)

show_with_matplotlib(subtracted_image,'subtracted image',4)

subtracted_image_2 = cv2.subtract(image, scalar)
show_with_matplotlib(subtracted_image_2,'subtract image-scalar', 5)