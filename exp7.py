import cv2
cap = cv2.VideoCapture("exp7.mp4")
if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()
print("Select Video Mode")
print("1. Normal Speed")
print("2. Slow Motion")
print("3. Fast Motion")
choice = input("Enter your choice (1/2/3): ")
if choice == "1":
    delay = 30     
elif choice == "2":
    delay = 100     
elif choice == "3":
    delay = 5       
else:
    print("Invalid choice! Default: Normal Speed")
    delay = 30
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Video Playback", frame)
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
