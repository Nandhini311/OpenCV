import cv2
import numpy as np
from show_matplotlib import show_with_matplotlib, colors


image = np.zeros((1200,1200,3),dtype='uint8')
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2.5
thickness = 5
text = 'abcdefghijklmnopqrstuvwyz'
circle_radius = 10

#getting text size
ret, baseline = cv2.getTextSize(text, font, font_scale,thickness)

#text widht and hieight
text_width, text_height = ret

#centering the text in the image
text_x = int(round((image.shape[1] - text_width)/2))
text_y = int(round((image.shape[0] - text_height)/2))

#drawing this point for reference
cv2.circle(image,(text_x,text_y), circle_radius, colors['green'],-1)

#drawing rectangle (boudinig box of the text)
cv2.rectangle(image, (text_x, text_y+baseline),(text_x + text_width -
thickness, text_y - text_height),colors['blue'], thickness)

#drawing the baseline
cv2.line(image, (text_x, text_y + int(round(thickness/2))), (text_x + text_width -
thickness, text_y + int(round(thickness/2))), colors['yellow'], thickness)

#writing the text centered in the image
cv2.putText(image, text, (text_x, text_y), font, font_scale, colors['magenta'], thickness)


show_with_matplotlib(image,"Understanding other text funcitons")