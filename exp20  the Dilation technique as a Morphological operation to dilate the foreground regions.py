import cv2
import numpy as np
img = cv2.imread("exp1.png")
if img is None:
    print("Error: Image not found!")
else:
    kernel = np.ones((5,5), np.uint8)
    dilated = cv2.dilate(img, kernel, iterations=1)
    cv2.imshow("Original Image", img)
    cv2.imshow("Dilated Image", dilated)
    cv2.imwrite("dilated_output.png", dilated)
    print("Dilated image saved as dilated_output.png")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
