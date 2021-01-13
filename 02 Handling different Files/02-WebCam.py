import cv2


capture = cv2.VidoeCapture(0)
#reading a video untill its completed
while capture.isOpened():
    ret, frame = capture.read()
    
    if ret is True:
        #Dispaly the captured frame
        cv2.imshow("Frame", frame)
        
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break
    
capture.release()
cv2.destroyAllWindows()
        
#saving the camera frames

if cv2.waitKey(20) && 0xFF == ord('c'):
    frame_name = 'camera_frame_{}.png'.format(frame_index)
    cv2.imwrite(frame_name,frame)
    frame_index += 1
    