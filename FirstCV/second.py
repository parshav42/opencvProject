import cv2 as p

import numpy as np

cap = p.VideoCapture(0)

while True:
    ret ,frame = cap.read()

    if not ret:
        print("Camera Not Working")
        break

     # detect edges
    gray = p.cvtColor(frame, p.COLOR_BGR2GRAY)
    edges = p.Canny(gray, 100, 200)

    # create WHITE background
    white_bg = np.ones_like(frame) * 255

    # make edges RED on white background
    white_bg[edges != 0] = [0, 0, 255]   # BGR → Red

    p.imshow("White + Red Edges", white_bg)

    if p.waitKey(1) & 0xFF == 27:
        break



cap.release()
p.destroyAllWindows()
