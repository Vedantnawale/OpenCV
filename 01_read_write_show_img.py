# Read Write And Show Image in OpneCV

import cv2

# imread used for read the image
img = cv2.imread('lena.jpg',1) # 0 for black And white 1 for color -1 no change
print(img)

# imshow used for show the image
cv2.imshow('image',img)
k = cv2.waitKey(0) # the argument is in miliseconds
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    # imwrite is used to create an image
    cv2.imwrite('lena_copy.png',img)
    cv2.destroyAllWindows()
