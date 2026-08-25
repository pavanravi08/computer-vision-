import cv2
import numpy as np
img = cv2.imread("exp1.png")
if img is None:
    print("Error: Image not found!")
else:
    kernel = np.ones((5,5), np.uint8)
    blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
    cv2.imshow("Original Image", img)
    cv2.imshow("Black Hat Image", blackhat)
    cv2.imwrite("blackhat_output.png", blackhat)
    print("Black Hat image saved as blackhat_output.png")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
