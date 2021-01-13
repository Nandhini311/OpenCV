#reading a video file backward
import cv2


capture = cv2.VideoCapture("file path name")

if capture.isOpened() is Flase:
    print("Error playing this video")
    
# to get the index of the last frame
frame_index = capture.get(cv2.CAP_PROP_FRAME_COUNT)-1
print("starting in frame: '{}'".format(frame_index))
#set the current frame to read to this position
while capture.isOpened() and frame_index >=0:
    capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
    
    ret, frame = capture.read()
    
    if ret is True:
        cv2.imshow('original frame', frame)
        
        frame_index = frame_index+1
        
        if cv2.waitKey(25) &0xFF == ord('q'):
            break
        
    else:
        break
    
capture.release()
cv2.destroyAllWindows()


