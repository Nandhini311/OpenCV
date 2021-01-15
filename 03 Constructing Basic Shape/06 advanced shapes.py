import cv2
import numpy as np
from matplotlib import pyplot as plt

colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}


def show_with_matplotlib(image, title):
    image_RGB = image[:,:,::-1]
    
    plt.imshow(image_RGB)
    plt.title(title)
    plt.show()
    
    
image = np.zeros((300,300,3),dtype='uint8')

cv2.line(image,(0,0),(300,300),colors['green'],4)
cv2.rectangle(image,(0,0),(100,100),colors['blue'],3)
ret, p1, p2 = cv2.clipLine((0,0,100,100),(0,0),(300,300))
#returns false if line is outside the rectangle
if ret:
    cv2.line(image,p1,p2,colors['yellow'],3)
    

#drawing arrows
#parameters- image, p1,p2, color, thickness, linetype, shift, tiplength
cv2.arrowedLine(image, (50,250),(150,250),colors['cyan'],4,cv2.LINE_AA,0,0.3)

show_with_matplotlib(image,"clipline")