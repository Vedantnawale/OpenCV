import cv2 as cv
import numpy as np

img = cv.imread("lena.jpg")
# lr1 = cv.pyrDown(img)
# lr2 = cv.pyrDown(lr1)
hr1 = cv.pyrUp(img)
hr2 = cv.pyrUp(hr1)

cv.imshow("original image",img)
# cv.imshow("pyrDown 1 image ",lr1)
# cv.imshow("pyrDown 2 image ",lr2)
cv.imshow("pyrUp 1 image ",hr1)
cv.imshow("pyrUp 2 image ",hr2)
cv.waitKey(0)
cv.destroyAllWindows()