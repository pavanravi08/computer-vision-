import cv2
img = cv2.imread("exp1.png")
if img is None:
    print("Error: Image not found!")
    exit()
print("Image Scaling")
print("1. Enlarge Image")
print("2. Reduce Image")
choice = int(input("Enter your choice (1/2): "))
if choice == 1:
    output = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    cv2.imshow("Enlarged Image", output)
    cv2.imwrite("enlarged_output.png", output)
    print("Enlarged image saved as enlarged_output.png")
elif choice == 2:
    output = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow("Reduced Image", output)
    cv2.imwrite("reduced_output.png", output)
    print("Reduced image saved as reduced_output.png")
else:
    print("Invalid Choice!")
cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
