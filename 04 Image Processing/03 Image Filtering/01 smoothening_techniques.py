import cv2
from show_matplotlib import show_with_matplotlib
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.suptitle("Smoothing techniques", fontsize=14, fontweight='bold')

kernel_averaging_5x5 = np.array([[0.04,0.04,0.04,0.04,0.04],[0.04,0.04,0.04,0.04,0.04]
                                 ,[0.04,0.04,0.04,0.04,0.04],[0.04,0.04,0.04,0.04,0.04]
                                 ,[0.04,0.04,0.04,0.04,0.04]])

kernerl_averaging_10x10 = np.ones((10,10), np.float32)/100
#kernel- describes how the pixels involved in the computation 
#are combined in order to obtain the desired result
image = cv2.imread('resources/spongebob.jpg')


#The function cv2.filter2D() applies an arbitrary linear filter to the provided image:
smooth_image_f2D_5 = cv2.filter2D(image, -1, kernel_averaging_5x5)
smooth_image_f2D_10 = cv2.filter2D(image, -1, kernerl_averaging_10x10)

show_with_matplotlib(image,"Original Image", 1)
show_with_matplotlib(smooth_image_f2D_5,"kernel 5x5",2)
show_with_matplotlib(smooth_image_f2D_10,"kernel 10x10",3)

''' 1.cv2.blur() and cv2.boxFilter() to perform an averaging by
convolving the image with a kernel  
    2.They simply take the average of all the pixels under the
kernel area and replace the central element with this average. 
    3. When the normalize parameter (by default True) of cv2.boxFilter() is equal to True, both functions perform the
same operation.'''


smooth_image_blur = cv2.blur(image, (10,10))
smooth_image_bfi = cv2.boxFilter(image,-1,(10,10),normalize=True)
#if normalize = False, then boxFilter unnormalize
show_with_matplotlib(smooth_image_blur,"Blur",4)
show_with_matplotlib(smooth_image_bfi,"boxFilter",5)


#filter functions
#GaussianBlur-gaussian kernel 
smooth_image_gb = cv2.GaussianBlur(image, (9,9),0)
#ksize = (9,9), sigmaX and sigmaY - standard deviation in the X and Y direction

#median filer - reduce the noise of salt and peper - channels are operated independently
smooth_image_mb = cv2.medianBlur(image, 9)

#bilateral filter - reduce the noise while keeping the edges sharp
smooth_image_bf_s = cv2.bilateralFilter(image, 5, 10, 10)
smooth_image_bf_l = cv2.bilateralFilter(image, 9, 200, 200)

show_with_matplotlib(smooth_image_gb,"Gaussian Blur",6)
show_with_matplotlib(smooth_image_mb,"Median Blur",7)
show_with_matplotlib(smooth_image_bf_s,"Bilateral blur small k value",8)
show_with_matplotlib(smooth_image_bf_l,"Bilateral blur large k value",9)