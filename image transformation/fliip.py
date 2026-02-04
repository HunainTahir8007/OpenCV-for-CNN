import cv2
image=cv2.imread("d:\\cv\/abc.jpg",flags=1)
print("showing the picture before the resizing")
cv2.imshow("showing ",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

flp=cv2.flip(image,1)
flp2=cv2.flip(image, 0)
flp3=cv2.flip(image , -1)

cv2.imshow("original " , image)
cv2.imshow("horizontal ", flp)
cv2.imshow("vertiacal ", flp2)
cv2.imshow("both ", flp3)
cv2.waitKey(0)
cv2.destroyAllWindows()
