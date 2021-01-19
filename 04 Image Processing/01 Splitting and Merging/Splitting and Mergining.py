#split and merging channels in OpenCV
'''We may want to work with specific channels on multichannel images, 
so it has to be split into several single-channel images. Once the processing
is done, one multi channel image from different single-channel images. It can be 
done using cv2.split() and cv2.merge()

(b,g,r) = cv2.split(image) #very time consuming operation
image_copy = cv2.merge((b,g,r))
#to access blue color of an image
blue = image[:,:,0]
'''

import cv2
import matplotlib.pyplot as plt

def show_with_matplotlib(color_img, title, pos):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB
    img_RGB = color_img[:, :, ::-1]

    ax = plt.subplot(3, 6, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')



#loading the original image
image = cv2.imread('resources/color_spaces.png') 

plt.figure(figsize=(13,5))
plt.suptitle("Splitting and merging",fontsize=14) 

show_with_matplotlib(image, "BGR-image",1)

#splitting the image into its three channels
(b,g,r) = cv2.split(image)


# Show all the channels from the BGR image:
show_with_matplotlib(cv2.cvtColor(b, cv2.COLOR_GRAY2BGR), "BGR - (B)",2)
show_with_matplotlib(cv2.cvtColor(g, cv2.COLOR_GRAY2BGR), "BGR - (G)",2 + 6)
show_with_matplotlib(cv2.cvtColor(r, cv2.COLOR_GRAY2BGR), "BGR - (R)",2 + 6 * 2)

#to show merge function
img_copy = cv2.merge((b,g,r))

show_with_matplotlib(img_copy,"BGR-image_copy",1+6)

#split() is a very time consuming function, therefore use it when its very necessary
#if not use numpy to access any specific channel
image_without_blue = image.copy()
image_without_green = image.copy()
image_without_red = image.copy()
#wihtout blue
image_without_blue[:,:,0] = 0

#without green
image_without_green[:,:,1]=0

#without red
image_without_red[:,:,2]=0

#displaying
show_with_matplotlib(image_without_blue, "BGR - (B)",3)
show_with_matplotlib(image_without_green, "BGR - (G)",3 + 6)
show_with_matplotlib(image_without_red, "BGR - (R)",3 + 6 * 2)


#splitting the image_without_blue into its three components
(b,g,r) = cv2.split(image_without_blue)

show_with_matplotlib(cv2.cvtColor(b,cv2.COLOR_GRAY2BGR),"BGR without blue -(B)", 4)
show_with_matplotlib(cv2.cvtColor(g,cv2.COLOR_GRAY2BGR),"BGR without blue -(G)", 4+6)
show_with_matplotlib(cv2.cvtColor(r,cv2.COLOR_GRAY2BGR),"BGR without blue -(R)", 4+6*2)

# Split the 'image_without_green' image into its three components (blue, green and red):
(b, g, r) = cv2.split(image_without_green)

# Show all the channels from the BGR image without the green:
show_with_matplotlib(cv2.cvtColor(b, cv2.COLOR_GRAY2BGR), "BGR without G (B)", 5)
show_with_matplotlib(cv2.cvtColor(g, cv2.COLOR_GRAY2BGR), "BGR without G (G)", 5 + 6)
show_with_matplotlib(cv2.cvtColor(r, cv2.COLOR_GRAY2BGR), "BGR without G (R)", 5 + 6 * 2)

# Split the 'image_without_red' image into its three components (blue, green and red):
(b, g, r) = cv2.split(image_without_red)

# Show all the channels from the BGR image without the red:
show_with_matplotlib(cv2.cvtColor(b, cv2.COLOR_GRAY2BGR), "BGR without R (B)", 6)
show_with_matplotlib(cv2.cvtColor(g, cv2.COLOR_GRAY2BGR), "BGR without R (G)", 6 + 6)
show_with_matplotlib(cv2.cvtColor(r, cv2.COLOR_GRAY2BGR), "BGR without R (R)", 6 + 6 * 2)

# Show the created image:
plt.show()
