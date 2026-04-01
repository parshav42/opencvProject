import cv2 as p



cap = p.VideoCapture(0)
mode =  "normal"

while True:
    ret , frame = cap.read()

    if not ret :
        print("Baby Cam Is Not Working Please Check ")
        break

    if mode == "red":
        frame[:, :, 1] = 0
        frame[:, :, 0] = 0

    elif mode == "green":
        frame[:, :, 0] = 0
        frame[:, :, 2] = 0

    elif mode == "blue":
        frame[:, :, 1] = 0
        frame[:, :, 2] = 0

    elif mode == "black":
        frame[:, :, 0] = 2
        frame[:, :, 0] = 1

    p.imshow("Camera", frame)

    key = p.waitKey(1) & 0xFF

    if key == ord('r'):
        mode = "red"
    elif key == ord('g'):
        mode = "green"
    elif key == ord('b'):
        mode = "blue"
    elif key == ord('l'):
        mode = "black"    
    elif key == ord('n'):
        mode = "normal"
    elif key == 27:
        break

 

cap.release()
p.destroyAllWindows()       

