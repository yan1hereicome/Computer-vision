import cv2

# Open default camera (0)
cap = cv2.VideoCapture(0)

# Video writer initialization
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None
recording = False
flip_mode = False
brightness = 50
contrast = 50

# Callback function for trackbars
def nothing(x):
    pass

# Create a control window
cv2.namedWindow("Controls")
cv2.createTrackbar("Brightness", "Controls", 50, 100, nothing)
cv2.createTrackbar("Contrast", "Controls", 50, 100, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Get brightness and contrast values from trackbars
    brightness = cv2.getTrackbarPos("Brightness", "Controls")
    contrast = cv2.getTrackbarPos("Contrast", "Controls")

    # Apply brightness/contrast
    frame = cv2.convertScaleAbs(frame, alpha=contrast / 50, beta=(brightness - 50) * 2)

    # Flip video if enabled
    if flip_mode:
        frame = cv2.flip(frame, 1)

    # If recording, draw a red circle on the frame
    if recording:
        cv2.circle(frame, (50, 50), 20, (0, 0, 255), -1)
        out.write(frame)

    # Show the frame
    cv2.imshow("Camera Feed", frame)

    # Key press handling
    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # ESC key to exit
        break
    elif key == 32:  # Space key to toggle recording
        recording = not recording
        if recording:
            out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame.shape[1], frame.shape[0]))
        else:
            out.release()
            out = None
    elif key == ord('f'):  # 'f' key to toggle flip mode
        flip_mode = not flip_mode

# Cleanup
cap.release()
if out:
    out.release()
cv2.destroyAllWindows()
