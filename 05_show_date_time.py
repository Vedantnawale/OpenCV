# Show Date and Time on videos using OpenCV
import cv2
import datetime
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,640)
cap.set(4,480)

# print(cap.get(3))
# print(cap.get(4))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'width : ' + str(cap.get(3)) + 'Height: ' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet,(4,15),font,0.5,(0,255,0),1,cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else :
       break

cap.release()
cv2.destroyAllWindows()