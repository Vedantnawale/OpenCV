# setting camera parameters Height and Width
import cv2
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # For width Associate Number is 3
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # For Height Associate Number is 4

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320) # or
# cap.set(3, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240) # or
# cap.set(4, 240)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # or
# print(cap.get(3))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # or
# print(cap.get(4))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()