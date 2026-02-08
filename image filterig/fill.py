import cv2 
import numpy as np 

image=cv2.imread("d:\\cv\\cam.jpg", flags=1)

sharpen_kernal= np.array([
    [0 , -1  , 0],
    [-1 , 5, -1],
    [0 , -1 , 0]
    
])

sharp = cv2.filter2D(image , -1 , sharpen_kernal)

cv2.imshow("original " , image)
cv2.imshow("sharpen ", sharp)
cv2.waitKey(0)
cv2.destroyAllWindows() 