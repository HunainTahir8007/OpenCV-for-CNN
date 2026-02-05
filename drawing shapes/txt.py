import cv2
image=cv2.imread("d:\\cv\\bird.jpg")
print(image.shape)

pt1=(700,150)
pt2=(1000,500)
color=(0,0,255)
thickness=4
rec=cv2.rectangle(image, pt1,pt2,color, thickness)
# Adding the text 
tt=cv2.putText(rec, "Oh !! This is a bird ", (800,700), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0 , 255 ),3 )
cv2.imshow("shaowing image with text", tt)
cv2.waitKey(0)
cv2.destroyAllWindows()
