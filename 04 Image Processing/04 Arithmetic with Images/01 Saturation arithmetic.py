import cv2
import numpy as np

x = np.uint8([250])
y = np.uint8([50])

#saturated operation
#opencv - values are clipped so that it won't fall out of range
# 250+50 = 300 => 255:
result_opencv = cv2.add(x,y)
print("cv2.add(x:'{}',y:'{}'='{}'".format(x,y,result_opencv))
#modulo operation
#numpy-valyes are wrapped around
# 250+50 = 300 % 256 = 44:
result_numpy = x+y
print("x:'{}',y:'{}'='{}'".format(x,y,result_numpy))