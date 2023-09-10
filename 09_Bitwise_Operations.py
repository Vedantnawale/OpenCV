import cv2
import  numpy as np

img1 = np.zeros((250,500,3), np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2 = cv2.imread("imag1_1.jpg")

img1 = cv2.resize(img1,(512,512))
img2 = cv2.resize(img2,(512,512))
# bitAnd = cv2.bitwise_and(img2,img1)
# bitOr = cv2.bitwise_or(img2,img1)
# bitxor = cv2.bitwise_xor(img2,img1)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow('bitNot1', bitNot1)
cv2.imshow('bitNot2', bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows() 