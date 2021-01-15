import cv2
import numpy as np
from matplotlib import pyplot as plt


colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

def show_with_matplotlib(img, title):
    img_RGB = img[:,:,::-1]
    
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()
    
    
image = np.zeros((400,400,3), dtype='uint8')

cv2.line(image,(400,25),(0,25),colors['magenta'],3)
#to draw a rectangle, default shifg = 0
cv2.rectangle(image,(10,50),(60,300),colors['green'],3)
cv2.rectangle(image,(10,320),(300,370),colors['white'],3)
#to draw a circle
#cv2.circle(image, center, radius, color, thickness, linetype, shift)
cv2.circle(image,(100,70),20,colors['yellow'],-1)

show_with_matplotlib(image,"basic shapes")