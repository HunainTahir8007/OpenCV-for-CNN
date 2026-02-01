import cv2

image=cv2.imread("d:\\cv\\a.jpg",flags=1)
if image is None:
    print("Image not found")
else:
    print("Imange laoded sucessfully")

cv2.imshow("Image showing ",image)
cv2.waitKey(0)
cv2.destroyAllWindows() 
cv2.imwrite("zxz.jpg", image) 
