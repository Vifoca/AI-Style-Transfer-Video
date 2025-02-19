import cv2
import torch
from torchvision import transforms
from PIL import Image
import numpy as np

# For demonstration purposes, we use a dummy style_transfer function.
# In practice, you would load a pre-trained style transfer model.
def style_transfer(image):
    # Convert image to grayscale and back to RGB to mimic a style change
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    stylized = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    return stylized

def process_video(source=0):
    cap = cv2.VideoCapture(source)  # 0 for webcam, or provide a video file path

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Apply style transfer to each frame
        output_frame = style_transfer(frame)

        cv2.imshow("Stylized Video", output_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_video()  # Use default webcam
