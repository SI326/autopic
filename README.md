# Webcam Person & Face Detection

This project is a simple Python application that uses OpenCV to detect people and faces in real time from a webcam feed. It leverages pre-trained Haar Cascade classifiers to identify full bodies and faces, then displays the results with visual overlays.

## Features

- Captures live video from the default webcam.
- Uses Haar Cascade models for:
  - Full-body detection.
  - Frontal face detection.
- Draws colored rectangles around detected people and faces.
- Shows the current timestamp on the video stream.
- Displays a live person count based on the number of detected faces.
- Allows the user to quit the application by pressing the `q` key.

## How It Works

The application continuously reads frames from the webcam and converts each frame to grayscale for processing. It then runs two detection models: one for full bodies and one for faces. Each detected region is highlighted with a rectangle (one color for bodies, another for faces). The total number of faces detected in the frame is treated as the person count.

Along with the detection boxes, the program overlays a timestamp and the current person count in the top-left corner of the video window. The video with all these overlays is displayed in a window titled "Webcam Person Detection". The loop continues until the user presses `q`, at which point the webcam is released and all windows are closed.

## Requirements

- Python 3
- OpenCV for Python (`opencv-python` package)
- A working webcam

## Usage

1. Install the required Python packages (primarily OpenCV).
2. Connect a webcam to your system if one is not built in.
3. Save the script (for example as `main.py`) in your project directory.
4. Run the script with Python.
5. Observe the live video with detection boxes, timestamp, and person count.
6. Press `q` to end the program and close the window.

## Notes

- Detection quality depends on lighting, camera angle, and distance.
- Haar Cascades are fast but not as robust as modern deep learning–based detectors.
- You can switch focus between body-based detection and face-based detection by using the appropriate cascade outputs.
