import cv2
import matplotlib.pyplot as plt

def show_with_matplotlib(img, title, pos):
    # Convert BGR image to RGB
    img_RGB = img[:, :, ::-1]

    ax = plt.subplot(3, 4, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')
    

#step1: constructing the sketch of the image
def sketch_image(image):
    #converting to gray scale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #smoothening the image
    img_smooth = cv2.medianBlur(img_gray, 5)
    
    #detecting the image's edges
    edges = cv2.Laplacian(img_smooth,cv2.CV_8U,ksize=5)
    
    '''If pixel value is greater than a threshold value, 
    it is assigned one value (may be white), 
    else it is assigned another value (may be black).'''
    #70-threshold value, 255 maxval
    ret, threshold = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY_INV)
    
    return threshold

def cartonize_image(image, gray_mode = False):
    thresholded = sketch_image(image)
    
    #bilateral function
    filtered = cv2.bilateralFilter(image, 10, 250, 250)
    
    cartoonized = cv2.bitwise_and(filtered, filtered, mask=thresholded)
    
    if gray_mode:
        return cv2.cvtColor(cartoonized, cv2.COLOR_BGR2GRAY)

    return cartoonized


plt.figure(figsize=(14, 6))
plt.suptitle("Cartoonizing images", fontsize=14, fontweight='bold')

# Load image:
image = cv2.imread('resources/justin.jpg')
show_with_matplotlib(image, "image", 1)

# Call the created functions for sketching and cartoonizing images:
custom_sketch_image = sketch_image(image)
custom_cartonized_image = cartonize_image(image)
custom_cartonized_image_gray = cartonize_image(image, True)


show_with_matplotlib(custom_cartonized_image, "custom cartoonized", 2)
show_with_matplotlib(cv2.cvtColor(custom_cartonized_image_gray, cv2.COLOR_GRAY2BGR), "custom cartoonized gray", 3)
show_with_matplotlib(cv2.cvtColor(custom_sketch_image, cv2.COLOR_GRAY2BGR), "custom sketch", 4)

# Call the OpenCV functions to get a similar output:
sketch_gray, sketch_color = cv2.pencilSketch(image, sigma_s=30, sigma_r=0.1, shade_factor=0.1)
stylizated_image = cv2.stylization(image, sigma_s=60, sigma_r=0.07)

show_with_matplotlib(cv2.cvtColor(sketch_gray, cv2.COLOR_GRAY2BGR), "sketch gray cv2.pencilSketch()", 7)
show_with_matplotlib(sketch_color, "sketch color cv2.pencilSketch()", 6)
show_with_matplotlib(stylizated_image, "cartoonized cv2.stylization()", 5)


plt.show()
