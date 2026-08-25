import cv2
import numpy as np
img = cv2.imread("exp1.png")
if img is None:
    print("Error: Image not found!")
else:
    kernel = np.ones((5,5), np.uint8)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Original Image", img)
    cv2.imshow("Opening Image", opening)
    cv2.imwrite("opening_output.png", opening)
    print("Opening image saved as opening_output.png")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
