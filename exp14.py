import cv2
import numpy as np
img = cv2.imread("exp1.png")
if img is None:
    print("Error: Image not found!")
else:
    rows, cols = img.shape[:2]
    pts1 = np.float32([[50, 50], [250, 50], [50, 250], [250, 250]])
    pts2 = np.float32([[10, 100], [220, 50], [100, 250], [250, 220]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    perspective = cv2.warpPerspective(img, matrix, (cols, rows))
    cv2.imshow("Original Image", img)
    cv2.imshow("Perspective Transformed Image", perspective)
    cv2.imwrite("perspective_output.png", perspective)
    print("Perspective transformed image saved as perspective_output.png")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
