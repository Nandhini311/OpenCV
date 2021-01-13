import cv2

# to read an image
image = cv2.imread("resources/spongebob.png")
# To show the image: 
cv2.imshow('imagewindow',image)
# waits until a key is pressed to exit the window
cv2.waitKey(0) 
# destroy all windows
cv2.destroyAllWindows() 
# To convert into grayscale: 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# To write the image into disk: 
cv2.imwrite('resources',gray)




#To read from web camera: 
capture = cv2.VideoCapture(0) #reads frame from camera
#To read from secondary camera: 
capture = cv2.VideoCapture(1)
#To check if connection was established fine: 
capture.isOpened()
#To capture footage frame by frame: 
frame = capture.read() #also return True or False to show if it has been read correctly.
#Frame width: 
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
#Frame height: 
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
#Frame per second: 
fps = capture.get(cv2.CAP_PROP_FPS)
