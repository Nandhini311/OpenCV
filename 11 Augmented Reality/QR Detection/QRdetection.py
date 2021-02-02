import numpy as np
import matplotlib.pyplot as plt
import cv2



img = cv2.imread("IDCard-Satya.png")
qrDetector = cv2.QRCodeDetector()

decoded, points, output = qrDetector.detectAndDecode(img)

if decoded is None:
    print("QR code not detected")
else:
    print(decoded)
  
n = len(points)
print(n)

for i in range(n):
    cv2.line(img, tuple(points[i][0]), tuple(points[(i+1)%n][0]),(255,0,255),3)
    

print("QR Code Detected !")
print(decoded)

resultImagePath = "QR-output.png"
cv2.imwrite(resultImagePath, img)
plt.imshow(img[:,:,::-1])
