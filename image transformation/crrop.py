import cv2 
image=cv2.imread("d:\\cv\\ab.jpg", flags=1)


op=str(input("Y / N"))
print(image.shape)
print("Before resizing the image   ")
cv2.imshow("Showing the image ", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Do you want to crop the image ??")
if op == "y":
    crop=image[100:182 , 150:276 ]
    print("Before resizing the image vs after  ")
cv2.imshow("Showing the image ", image)
cv2.imshow("Showing the image ", crop)


cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("ccro.png",crop)
