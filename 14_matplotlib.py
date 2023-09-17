import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg',-1)
cv2.imshow('image',img)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # If we used this then the color of image become sames

plt.imshow(img)
# plt.xticks([]),plt.yticks([]) without x and y axis
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()