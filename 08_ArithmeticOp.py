import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape) # return a tuple of number of rows ,columns and chanels
print(img.size) # returns Total number of pixels is accessed
print(img.dtype) # returns Image datatype is accessed 
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340,330:390]
img[273:333, 100:160] = ball

img = cv2.resize(img,(512,512)) # It is used to resized photo 
img2 = cv2.resize(img2,(512,512))

# dst = cv2.add(img,img2) this is used to add two different images
dst = cv2.addWeighted(img,.2,img2,.8,0)


cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
