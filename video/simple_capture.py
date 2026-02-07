import cv2 

cap=cv2.VideoCapture(0)

while True:
    res , frame = cap.read()
    if not res:
        print("Failed to grab the frames")
        break
    cv2.imshow("webcam feed", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("quitting ......")
        break

cap.release()
cv2.destroyAllWindows()
