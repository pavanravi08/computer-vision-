import cv2

# Read the image
img = cv2.imread("exp3.png")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray, 100, 200)

    # Display the original image
    cv2.imshow("Original Image", img)

    # Display the outline (edges)
    cv2.imshow("Canny Edge Detection", edges)

    # Save the output image
    cv2.imwrite("canny_output.png", edges)

    print("Outline image saved as canny_output.png")

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
