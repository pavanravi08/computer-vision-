import cv2
img = cv2.imread("exp1.png")
if img is None:
    print("Error: Image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.addWeighted(cv2.convertScaleAbs(sobel_x), 0.5,
                            cv2.convertScaleAbs(sobel_y), 0.5, 0)
    cv2.imshow("Original Image", img)
    cv2.imshow("Sobel X", cv2.convertScaleAbs(sobel_x))
    cv2.imshow("Sobel Y", cv2.convertScaleAbs(sobel_y))
    cv2.imshow("Sobel Filtered Image", sobel)
    cv2.imwrite("sobel_output.png", sobel)
    print("Sobel filtered image saved as sobel_output.png")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
