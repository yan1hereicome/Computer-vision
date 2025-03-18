# Computer-vision
Adjustable Brightness & Contrast
Use trackbars (cv2.createTrackbar) to let users modify brightness and contrast in real-time.
Flip Video (Mirror Mode)
Add an option to flip the video horizontally (cv2.flip(frame, 1)) for a mirrored effect.
FPS Control
Allow users to set a custom FPS rate when recording (cv2.VideoWriter).
Grayscale or Edge Detection Filter
Convert video to grayscale (cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)) or apply Canny edge detection.

## Assignments name ##
 Video Recorder 

## Description ##
VisionCamRecorder is a simple video recorder built using OpenCV.
It supports real-time recording, brightness/contrast adjustment, and flip mode.

## Features##
✔ Live camera feed display
✔ Recording mode with visual indicator (red circle)
✔ Adjustable brightness & contrast
✔ Flip video mode (mirror effect)
✔ Saves video in .avi format

## How to Use ##
Press SPACE to start/stop recording.
Press F to flip the video.
Adjust brightness/contrast using the sliders.
Press ESC to exit.

### code 
pip install opencv-python
python main.py


