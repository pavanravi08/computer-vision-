import cv2

# Read the image
img = cv2.imread("exp2.png")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(img, (15, 15), 0)

    # Display original image
    cv2.imshow("Original Image", img)

    # Display blurred image
    cv2.imshow("Gaussian Blur Image", blur)

    # Save the blurred image
    cv2.imwrite("blur_output.png", blur)

    print("Blurred image saved as blur_output.png")

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
