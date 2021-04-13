import numpy
import cv2

# The video capture device (webcam)
input_device = cv2.VideoCapture(0)

if not input_device.isOpened():
    print('Cannot open camera')
    exit()


while True:

    # Capture the frame
    ret, frame = input_device.read()

    if not ret:
        print('Unable to read further into stream. Exiting.')
        break

    # Our operations on the frame come from here
    # Ignore this step if you do not care about editing
    # Or changing the image. The line as is converts it to
    # Black and white.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame in an OpenCV window
    cv2.imshow('Frame', frame)
    cv2

    if cv2.waitKey(1) == ord('q'):
        break


input_device.release()
cv2.destroyAllWindows()
