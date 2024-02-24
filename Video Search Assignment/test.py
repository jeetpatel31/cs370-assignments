import numpy as np
import cv2

# Load the frames from the .npy file
frames = np.load('frames.npy')

# Iterate over each frame in the array and display it
for frame in frames:
    # Assuming the frames are in the range [0, 1], scale to [0, 255] and convert to uint8
    frame = (frame * 255).astype(np.uint8)

    # Convert the frame from RGB to BGR for OpenCV display
    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Show the frame
    cv2.imshow('Frame', frame_bgr)

    # Wait for 25 ms and check if the 'q' key is pressed to exit the loop
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Close the OpenCV window
cv2.destroyAllWindows()
