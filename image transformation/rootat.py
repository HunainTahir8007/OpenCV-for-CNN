import cv2
image=cv2.imread("d:\\cv\\ee.jpg",flags=1)


h,w=image.shape[:2]
print(h,w)
center=(w//2 , h//2)
g=cv2.getRotationMatrix2D(center=center, angle=40, scale=1)
rotated=cv2.warpAffine(image, g, (w,h))

cv2.imshow("simple" , image)
cv2.imshow("rootated" , rotated )
cv2.waitKey(0)
cv2.destroyAllWindows()
