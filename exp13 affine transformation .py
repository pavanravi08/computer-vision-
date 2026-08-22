import cv2
import numpy as np
img = cv2.imread("exp1.png")
if img is None:
    print("Error: Image not found!")
else:
    rows, cols = img.shape[:2]
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    matrix = cv2.getAffineTransform(pts1, pts2)
    affine = cv2.warpAffine(img, matrix, (cols, rows))
    cv2.imshow("Original Image", img)
    cv2.imshow("Affine Transformed Image", affine)
    cv2.imwrite("affine_output.png", affine)
    print("Affine transformed image saved as affine_output.png")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
