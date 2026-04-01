import cv2 as p
import numpy as np


cap = p.VideoCapture(0)
cap.set(3, 620)
cap.set(4, 420)
while True:
    ret , frame = cap.read()

    if not ret :
        print("Baby Cam Is Not Working Please Check ")
        break
    p.imshow("Camera", frame)
    if p.waitKey(1) & 0xFF == ord('q'):
        break







p.release()
p.destroyAllWindows()