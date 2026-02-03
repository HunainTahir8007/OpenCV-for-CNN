import cv2
image=cv2.imread("d:\\cv\\a.jpg",flags=1)
if image is None:
    print("Image not found")
else:
    print("Imange laoded sucessfully")


a,b,c=image.shape
print(f"Height {a} , Width {b} , color chanels {c}" )