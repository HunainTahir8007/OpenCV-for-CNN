import cv2

camera = cv2.VideoCapture(0)

get_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
get_height= int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec= cv2.VideoWriter.fourcc(*'XVID')

recorder = cv2.VideoWriter("my_video.mp4", codec , 25 , (get_width, get_height))

while True:
    succes , frame = camera.read()
    if succes is not True: 
        break
    recorder.write(frame)
    cv2.imshow("Recording Real Time", frame)
    
    if cv2.waitKey(1) & 0XFF== ord('q'):
        print("Quitting .....")
        break

camera.release()
cv2.destroyAllWindows() 