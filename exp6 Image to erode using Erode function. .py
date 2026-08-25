import cv2
import numpy as np

# Read the image
img = cv2.imread("exp1.png")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Create a 5x5 kernel
    kernel = np.ones((5,5), np.uint8)

    # Apply Erosion
    eroded = cv2.erode(img, kernel, iterations=1)

    # Display original image
    cv2.imshow("Original Image", img)

    # Display eroded image
    cv2.imshow("Eroded Image", eroded)

    # Save the output image
    cv2.imwrite("eroded_output.png", eroded)

    print("Eroded image saved as eroded_output.png")

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
