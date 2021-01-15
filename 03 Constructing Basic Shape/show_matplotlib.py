from matplotlib import pyplot as plt

def show_with_matplotlib(image,title):
    image_RGB = image[:,:,::-1]
    
    plt.imshow(image_RGB)
    plt.title(title)
    plt.show()
    
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125),'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}