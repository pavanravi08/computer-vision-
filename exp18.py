import cv2
img = cv2.imread("exp1.png")
if img is None:
    print("Error: Image not found!")
else:
    roi = img[20:120, 20:120]
    img[20:120, 150:250] = roi
    cv2.imshow("Original Image", cv2.imread("exp1.png"))
    cv2.imshow("Cropped ROI", roi)
    cv2.imshow("Copied and Pasted Image", img)
    cv2.imwrite("roi_output.png", img)
    print("ROI image saved as roi_output.png")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
