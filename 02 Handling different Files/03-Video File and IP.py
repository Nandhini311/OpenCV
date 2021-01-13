#reading a video file
import cv2


'''will have necessary information to parse 
the command-line arguments into data types'''

parser = argparse.ArgumentParser()

parser.add_argument("video_path", help="path to the video file")
args = parser.parse_args()
capture = cv2.VideoCapture(args.video_path)

#Reading from an IP camera
capture = cv2.VideoCapture('http://217.126.89.102:8010/axiscgi/mjpg/video.cgi')

while capture.isOpened():
    ret, frame = capture.read()
    
    if ret is True:
        #Dispaly the captured frame
        cv2.imshow("Frame", frame)
        
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break
