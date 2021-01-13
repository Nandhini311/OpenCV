"""
Example to introduce how to write a video file
"""

# Import required packages
import cv2


# Create a VideoCapture object and pass 0 as argument to read from the camera
capture = cv2.VideoCapture(0)

# Get some properties of VideoCapture (frame width, frame height and frames per second (fps)):
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

# Print these values:
print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(frame_width))
print("CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(frame_height))
print("CAP_PROP_FPS : '{}'".format(fps))

# FourCC is a 4-byte code used to specify the video codec and it is platform dependent!
# In this case, define the codec XVID
# This line also works:
# fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Create VideoWriter object. We use the same properties as the input camera.
# Last argument is False to write the video in grayscale. True otherwise (write the video in color)
out_gray = cv2.VideoWriter('output_video_path', fourcc, int(fps), (int(frame_width), int(frame_height)), False)

# Read until video is completed or 'q' is pressed
while capture.isOpened():
    # Read the frame from the camera
    ret, frame = capture.read()
    if ret is True:

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything:
capture.release()
out_gray.release()
cv2.destroyAllWindows()
