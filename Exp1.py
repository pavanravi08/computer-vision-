import cv2

# Read the image
image = cv2.imread("exp1.png")

# Check if the image is loaded
if image is None:
    print("Image not found!")
else:
    # Display the original image
    cv2.imshow("Original Image", image)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the grayscale image
    cv2.imshow("Gray Image", gray)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
