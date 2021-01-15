from matplotlib import pyplot as plt
import cv2
import numpy as np


def show_with_matplotlib(image,title):
    image_RGB = image[:,:,::-1]
    
    plt.imshow(image_RGB)
    plt.title(title)
    plt.show()
    
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125),'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

images = np.zeros((300,300,3),dtype='uint8')

cv2.line(images,(0,0),(300,300),colors['green'],3)
cv2.rectangle(images,(0,0),(100,100),colors['blue'],3)
ret, p1,p2 = cv2.clipLine((0,0,100,100),(0,0),(300,300))
if ret:
    cv2.line(images,p1,p2,colors['yellow'],3)
    
show_with_matplotlib(images,"Clip line")