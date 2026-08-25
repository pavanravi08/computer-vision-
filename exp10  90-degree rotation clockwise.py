import cv2
img = cv2.imread("exp1.png")
if img is None:
    print("Error: Image not found!")
else:
    rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow("Original Image", img)
    cv2.imshow("90 Degree Clockwise Rotation", rotated)
    cv2.imwrite("rotated_output.png", rotated)
    print("Rotated image saved as rotated_output.png")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
