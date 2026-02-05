import cv2 
image=cv2.imread("d:\\cv\\lin.jpg",flags=1)


print(image.shape)
pt1=(100,80)
pt2=(200,80)
color=(255, 0 , 0)

linn=cv2.line(image, pt1, pt2 , color , thickness=4)
cv2.imshow("showing ", linn)
cv2.waitKey(0)
cv2.destroyAllWindows()