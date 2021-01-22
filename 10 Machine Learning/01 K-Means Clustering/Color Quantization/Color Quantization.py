import numpy as np
import cv2
from matplotlib import pyplot as plt
import collections

#Color quantization using k means clustering
#process of reducing the number of colors in an image.
#very important when certain devices can only display a limited number of colors
#therefore trade off btwn the similarity and the reduction in number is necessary

img = cv2.imread('landscape_3.jpg')

def show_img_with_matplotlib(color_img, title, pos):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB
    img_RGB = color_img[:, :, ::-1]

    ax = plt.subplot(2, 3, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')

def color_quantization(image, k):
    #key step
    data = np.float32(image).reshape((-1,3))
    #algorithm termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    
    #applying K-means algorithm
    ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    center = np.uint8(center)
    #replacing pixel value with their center value
    result = center[label.flatten()] #flatten - copy of any array as 1D array
    result = result.reshape(image.shape)
   
    #number of pixels assigned to each center value
    counter = collections.Counter(label.flatten()) #key - value pair - center : number of pixels
    print(counter)
    
    #getting total number of pixels
    total = image.shape[0]*image.shape[1]
    
    #assigning width and height to the color distribution image
    desired_width = image.shape[1]
    #difference btwn them will be the seperation between the image
    desired_height = 70
    desired_height_colors = 50
    
    #initialize the color distribution image
    color_distribution = np.ones((desired_height, desired_width,3), dtype='uint8')*255
    
    #initialize start
    start = 0
    
    for key, value in counter.items():
        #calculate the normalized value
        value_normalized = value/total * desired_width
        
        #move end to the right
        end = start+value_normalized
        
        cv2.rectangle(color_distribution, (int(start),0), (int(end), desired_height_colors)
                      , center[key].tolist(), -1)
        start = end
        
        
    return np.vstack((color_distribution,result))

color_3 = color_quantization(img,3)
color_5 = color_quantization(img,5)
color_10 = color_quantization(img,10)
color_20 = color_quantization(img,20)
color_40 = color_quantization(img,40)

fig = plt.figure(figsize=(16, 8))
plt.suptitle("Color quantization using K-means clustering algorithm", fontsize=14, fontweight='bold')
fig.patch.set_facecolor('silver')

show_img_with_matplotlib(img, "Original image", 1)
show_img_with_matplotlib(color_3, "Color quantization - 3 colors", 2)
show_img_with_matplotlib(color_5, "Color quantization - 5 colors", 3)
show_img_with_matplotlib(color_10, "Color quantization - 10 colors", 4)
show_img_with_matplotlib(color_20, "Color quantization - 20 colors", 5)
show_img_with_matplotlib(color_40, "Color quantization - 50 colors", 6)

plt.show()
