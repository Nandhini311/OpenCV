import cv2
import matplotlib.pyplot as plt

'''Two key functions to perform geometric transformations
are cv2.warpAffine() and cv2.wrapPerspective()'''

def show_with_matplotlib(img, title):
    # Convert BGR image to RGB
    img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()
    
image = cv2.imread('resources/lena_image.png')
height, width = image.shape[:2]

#show loaded image
show_with_matplotlib(image, "Original image")

#Scaling or resizing-fx and fy are scaling factors
dst_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
#this will shrink the image by a factor of 2
#interpolation should be cv2.INTER_CUBIC inorder to enlarge the image
#cv2.INTER_LINEAR should be used to shrink the image

#getting the shape
print(dst_image.shape)

#making the image by size 
dst_image2 = cv2.resize(image,(width*2, height*2), interpolation=cv2.INTER_AREA)
print(dst_image2.shape)


show_with_matplotlib(dst_image, "Resized image")
show_with_matplotlib(dst_image2, "Resized image 2")


