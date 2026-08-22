import cv2
img = cv2.imread("exp1.png")
if img is None:
    print("Image not found!")
    exit()
x, y, w, h = 180, 220, 120, 120
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.putText(img, "Watch", (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8,
            (0, 0, 255), 2)
cv2.imshow("Watch Detection", img)
cv2.imwrite("watch_detected.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
