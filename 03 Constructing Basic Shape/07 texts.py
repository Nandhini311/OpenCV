#writing text
import cv2
import numpy as np
from show_matplotlib import show_with_matplotlib, colors

image = np.zeros((500,500,3),dtype='uint8')

#syntax: img, text, org (starting coordinates), fontFace, fomt scale, thickness, linetype, bottomLeft origin

cv2.putText(image, 'Mastering OpenCV4 with python',(10,30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors['red'],2,cv2.LINE_4)
cv2.putText(image,'I LOVE BANANA SHAKE', (10,70),
            cv2.FONT_HERSHEY_SIMPLEX,0.9,colors['yellow'],2,cv2.LINE_AA, True)
cv2.putText(image,'ANIMALS ARE LOVE',(10, 150),
            cv2.FONT_HERSHEY_SIMPLEX,0.9,colors['cyan'],2,cv2.LINE_8)

show_with_matplotlib(image,"Text Images")


'''available fonts
FONT_HERSHEY_SIMPLEX = 0
FONT_HERSHEY_PLAIN = 1
FONT_HERSHEY_DUPLEX = 2
FONT_HERSHEY_COMPLEX = 3
FONT_HERSHEY_TRIPLEX = 4
FONT_HERSHEY_COMPLEX_SMALL = 5
FONT_HERSHEY_SCRIPT_SIMPLEX = 6
FONT_HERSHEY_SCRIPT_COMPLEX = 7
'''