import cv2
img=cv2.imread("d:\\cv\\pro.jpg", flags=1)

blur=cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow("s" , blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
