import cv2
import numpy as np
img = cv2.imread("exp1.png")
if img is None:
    print("Error: Image not found!")
else:
    kernel = np.ones((5,5), np.uint8)
    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    cv2.imshow("Original Image", img)
    cv2.imshow("Top Hat Image", tophat)
    cv2.imwrite("tophat_output.png", tophat)
    print("Top Hat image saved as tophat_output.png")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
