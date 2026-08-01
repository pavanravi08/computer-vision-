import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("exp5.png")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Display the original image
    cv2.imshow("Original Image", img)

    # Colors used in OpenCV (BGR)
    colors = ('b', 'g', 'r')

    # Plot histogram for each color channel
    for i, color in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

    # Graph title and labels
    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")

    # Show histogram
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
