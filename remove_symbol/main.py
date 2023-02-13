import cv2
import numpy as np

# Load the video
cap = cv2.VideoCapture("video.mp4")

# Get the video dimensions
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width, height))

# Loop over the frames of the video
while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Convert the grayscale frame to a binary frame
        _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

        # Find the contours in the binary frame
        _, contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Iterate over the contours and draw rectangles around the symbols
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), -1)

        # Display the result
        cv2.imshow("Result", frame)

        # Write the result to the output video
        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the VideoCapture and VideoWriter objects
cap.release()
out.release()

# Close all windows
cv2.destroyAllWindows()
