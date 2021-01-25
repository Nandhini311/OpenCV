import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_with_matplotlib(color_img, title, pos):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB
    img_RGB = color_img[:, :, ::-1]

    ax = plt.subplot(3, 3, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')
    
plt.figure(figsize=(12, 6))
plt.suptitle("Bitwise operations (AND, OR, XOR, NOT)", fontsize=14, fontweight='bold')
    

img_1 = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(img_1, (10, 10), (110, 110), (255, 255, 255), -1)
cv2.circle(img_1, (200, 200), 50, (255, 255, 255), -1)

img_2 = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(img_2, (50, 50), (150, 150), (255, 255, 255), -1)
cv2.circle(img_2, (225, 200), 50, (255, 255, 255), -1)

bitwise_or = cv2.bitwise_or(img_1, img_2)
bitwise_and = cv2.bitwise_and(img_1, img_2)
bitwise_xor = cv2.bitwise_xor(img_1, img_2)
bitwise_not = cv2.bitwise_not(img_1)

# Display all the resulting images:
show_with_matplotlib(cv2.cvtColor(img_1, cv2.COLOR_GRAY2BGR), "image 1", 1)
show_with_matplotlib(cv2.cvtColor(img_2, cv2.COLOR_GRAY2BGR), "image 2", 2)
show_with_matplotlib(cv2.cvtColor(bitwise_or, cv2.COLOR_GRAY2BGR), "image 1 OR image 2", 3)
show_with_matplotlib(cv2.cvtColor(bitwise_and, cv2.COLOR_GRAY2BGR), "image 1 AND image 2", 4)
show_with_matplotlib(cv2.cvtColor(bitwise_xor, cv2.COLOR_GRAY2BGR), "image 1 XOR image 2", 5)
show_with_matplotlib(cv2.cvtColor(bitwise_not, cv2.COLOR_GRAY2BGR), "NOT (image 1)", 6)

image = cv2.imread('resources/cat.png')

img_3 = np.zeros((300, 300), dtype="uint8")
cv2.circle(img_3, (150, 150), 150, (255, 255, 255), -1)

#using and as mask
dog = cv2.bitwise_and(image, image, mask=img_3)


show_with_matplotlib(cv2.cvtColor(img_3, cv2.COLOR_GRAY2BGR), "image 3", 7)
show_with_matplotlib(dog, "image 3 AND a loaded image", 8)

# Show the Figure:
plt.show()



