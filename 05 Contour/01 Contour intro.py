import numpy as np
import cv2
import matplotlib.pyplot as plt
        
def draw_contour_outline(img, cnts, color, thickness=1):
    """Draws contours outlines of each contour"""

    for cnt in cnts:
        cv2.drawContours(img, [cnt], 0, color, thickness)
        
def build_image():
    img = np.ones((500, 500, 3), dtype="uint8") * 70
    cv2.rectangle(img, (100, 100), (300, 300), (255, 0, 255), -1)
    cv2.circle(img, (400, 400), 100, (255, 255, 0), -1)
    
    return img

               
def build_image_2():
    img = np.ones((500, 500, 3), dtype="uint8") * 70
    cv2.rectangle(img, (100, 100), (300, 300), (255, 0, 255), -1)
    cv2.rectangle(img, (150, 150), (250, 250), (70, 70, 70), -1)
    cv2.circle(img, (400, 400), 100, (255, 255, 0), -1)
    cv2.circle(img, (400, 400), 50, (70, 70, 70), -1)

    return img

def show_img_with_matplotlib(color_img, title, pos):
    """Shows an image using matplotlib capabilities"""

    img_RGB = color_img[:, :, ::-1]

    ax = plt.subplot(1, 4, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')


fig = plt.figure(figsize=(12, 5))
plt.suptitle("Contours introduction", fontsize=14, fontweight='bold')
fig.patch.set_facecolor('silver')


image = build_image()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary_image = cv2.threshold(gray_image, 70, 255, cv2.THRESH_BINARY)
contour, hierarchy = cv2.findContours(binary_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#ouptuts all the contours without any hierarchical relationship
contour1, hirerchy2 = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#outputs only the external the contours

contour_image = image.copy()
contour_image1 = image.copy()

draw_contour_outline(contour_image, contour, (0, 0, 255), 5)
draw_contour_outline(contour_image1, contour1, (255, 0, 0), 5)


show_img_with_matplotlib(image, "Original Imager", 1)
show_img_with_matplotlib(cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR), "threshold 100", 2)
show_img_with_matplotlib(contour_image, "RETR LIST", 3)
show_img_with_matplotlib(contour_image1, "RETR EXTERNAL", 4)

plt.show()