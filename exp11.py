import cv2
img = cv2.imread("exp1.png")
if img is None:
    print("Error: Image not found!")
else:
    rotated = cv2.rotate(img, cv2.ROTATE_180)
    cv2.imshow("Original Image", img)
    cv2.imshow("180 Degree Rotated Image", rotated)
    cv2.imwrite("rotated_180_output.png", rotated)
    print("180 Degree Rotated image saved as rotated_180_output.png")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
