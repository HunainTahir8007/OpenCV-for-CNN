import cv2 
import cv2
img=cv2.imread("d:\\cv\\nn.jpg", flags=1)

blur=cv2.medianBlur(img, 9)
cv2.imshow("ss", img)
cv2.imshow("s" , blur)
cv2.waitKey(0)
cv2.destroyAllWindows()