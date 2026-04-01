import     cv2 as p 
import numpy as np  


image = p.imread("image.png")



h,w = image.shape[:2]

(B,G,R ) = image[100,200]

print("RRed",R)
print("Green",G)
print("Blue",B)


roi = image[10:600,20:700]
p.imshow("Image",roi)
p.waitKey(0)
print("height :", h)
print("width :", w) 