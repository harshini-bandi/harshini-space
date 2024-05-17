import cv2
import numpy as np

# Create a window to display the camera feed
cv2.namedWindow("Ripeness Detection")

# Open a connection to the camera (0 for default camera, adjust as needed)
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame.")
        break

    # Convert the frame to the HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define color ranges for ripe and unripe fruits (you may need to adjust these)
    lower_ripe = np.array([20, 100, 100])
    upper_ripe = np.array([30, 255, 255])
    lower_unripe = np.array([40, 100, 100])
    upper_unripe = np.array([50, 255, 255])

    # Create masks to identify ripe and unripe regions in the frame
    ripe_mask = cv2.inRange(hsv_frame, lower_ripe, upper_ripe)
    unripe_mask = cv2.inRange(hsv_frame, lower_unripe, upper_unripe)

    # Find the percentage of ripe and unripe pixels
    total_pixels = frame.shape[0] * frame.shape[1]
    ripe_pixels = cv2.countNonZero(ripe_mask)
    unripe_pixels = cv2.countNonZero(unripe_mask)

    ripe_percentage = (ripe_pixels / total_pixels) * 100
    unripe_percentage = (unripe_pixels / total_pixels) * 100

    # Determine the ripeness based on a threshold (adjust as needed)
    if ripe_percentage > 5:
        ripeness = "Ripe"
    elif unripe_percentage > 5:
        ripeness = "Unripe"
    else:
        ripeness = "Not Sure"

    # Display the ripeness on the frame
    cv2.putText(frame, f"Ripeness: {ripeness}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Ripeness Detection", frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()