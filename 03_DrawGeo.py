# Draw geometric shapes on image
import numpy as np
import cv2

img = cv2.imread('lena.jpg',1)

img = cv2.line(img, (0,0),(255,255), (255,0,0), 10) # img,start-cordinate,ending-cordinate,color COLOR ALWAYS LOADED IN REVERSE ORDER i.e. BGR
img = cv2.arrowedLine(img, (0,255),(255,255), (0,255,0), 10) 
img = cv2.rectangle(img, (384,0),(510,128), (0,0,255), 5) 
img = cv2.circle(img,(447,63), 63 , (0,255,0),-1)
font = cv2.FONT_HERSHEY_SIMPLEX 
img = cv2.putText(img , 'OpenCv' ,(10,500),font,4,(0,255,255),5,cv2.LINE_AA)
# img - cv2.rectangle(img, (384,0),(510,128), (0,0,255), -1) # filled color to the whole rectangle
img = cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
