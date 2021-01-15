import numpy as np
import cv2
from matplotlib import pyplot as plt


#dictionary that contains some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}


def show_with_matplotlib(img, title):
    img_RGB = img[:,:,::-1]
    
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()
    


seperation = 40
#creating a canvas 500x500p pixels and having three channels
image = np.zeros((500,500,3),dtype="uint8")

for key in colors:
    #drawing a line using the function cv2.line()
    #cv2.line(image, start coordinate, end coordinate, color, thickness)
    cv2.line(image,(0,seperation), (500,seperation), colors[key], 10)
    seperation += 40
    
show_with_matplotlib(image,'Dictionary with predefined colors')