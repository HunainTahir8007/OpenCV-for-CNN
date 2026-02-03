import cv2
file_loc= "d:\\cv\\ee.jpg"
image=cv2.imread(file_loc, flags=1)
if image is None:
    print("Could not load the image ")
else:
    print("Image loaded sucessfully ")


print("Do U want to convert in gray scale image ??")
key=str(input("Y / N "))
if key is "y":
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow(" gray scale image " , gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Do to want to save the image ?? ")
    op=str(input("Y / N"))
    if op is "y":
        cv2.imwrite("new_img.jpg",gray)
    else:
        print("Image cannot saved ")
else:
    print("Image canot conver=t into the gray scale ")
    cv2.imshow("  coloured image " , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Do to want to save this image ?? ")
    op=str(input("Y / N"))
    if op is "y":
        cv2.imwrite("new_img.jpg",image)
    else:
        print("Image cannot saved ")