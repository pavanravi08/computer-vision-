import cv2
img = cv2.imread("exp1.png")
if img is None:
    print("Error: Image not found!")
else:
    watermarked = img.copy()
    cv2.putText(
        watermarked,
        "WATERMARK",          
        (50, 50),            
        cv2.FONT_HERSHEY_SIMPLEX,
        1,                   
        (255, 255, 255),     
        2,                   
        cv2.LINE_AA
    )
    output = cv2.addWeighted(watermarked, 0.3, img, 0.7, 0)
    cv2.imshow("Original Image", img)
    cv2.imshow("Watermarked Image", output)
    cv2.imwrite("watermarked_output.png", output)
    print("Watermarked image saved as watermarked_output.png")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
