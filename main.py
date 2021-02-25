from cv2 import cv2 
import numpy as np
img = cv2.imread("opencv-logo.png",1)
# cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
# cv2.imshow("Image",img)
# cv2.waitKey(0)
# cv2.imwrite("output.jpg",img)
print(type(img))