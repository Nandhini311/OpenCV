#writing a video file

#counting frames per second

import cv2

capture = cv2.VideoCapture(0)

while capture.isOpened():
    ret, frame = capture.read()
    
    if ret is True:
        processing_start = time.time()
        
        cv2.imshow("frame window", frame)
        
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
        
        processing_end = time.time()
        #time per frame
        processing_time_frame = processing_end - processing_start
        print("fps:{}".format(1.0/processing_time_frame))
        
    else:
        break