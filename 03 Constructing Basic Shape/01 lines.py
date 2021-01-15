import cv2
import numpy as np
from matplotlib import pyplot as plt

colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

#drawing a canvas 400x400 pixels, 3 channels, uint8
image = np.zeros((400,400,3),dtype='uint8')


def show_with_matplotlib(img, title):
    img_RGB = img[:,:,::-1]
    
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()
    



cv2.line(image,(0,0),(400,400),colors['green'],3)
cv2.line(image,(0,400),(400,0),colors['blue'],10)
cv2.line(image,(200,0),(200,400),colors['blue'],3)
cv2.line(image,(0,200),(400,200),colors['yellow'],10)


show_with_matplotlib(image, "Drawing lines")