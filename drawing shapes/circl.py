import cv2 
image=cv2.imread("d:\\cv\\bird.jpg")
print(image.shape)

cir=cv2.circle(image, center=(850,325), radius=200 , color=(0,0,255), thickness=5)
cv2.imshow("circle", cir)
cv2.waitKey(0)
cv2.destroyAllWindows()