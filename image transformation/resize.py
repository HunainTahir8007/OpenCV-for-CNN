import cv2 

image=cv2.imread("d:\\cv\/abc.jpg",flags=1)
print("showing the picture before the resizing")
cv2.imshow("showing ",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(image.shape)

crop=cv2.resize(image,(183,13))
cv2.imshow("showing ",crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("resiz.png",crop) 