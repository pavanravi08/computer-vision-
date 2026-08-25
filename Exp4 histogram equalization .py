import cv2

# Read the image
img = cv2.imread("exp4.png")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Histogram Equalization
    equalized = cv2.equalizeHist(gray)

    # Display the original grayscale image
    cv2.imshow("Original Grayscale Image", gray)

    # Display the equalized image
    cv2.imshow("Histogram Equalized Image", equalized)

    # Save the equalized image
    cv2.imwrite("equalized_output.png", equalized)

    print("Equalized image saved as equalized_output.png")

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
