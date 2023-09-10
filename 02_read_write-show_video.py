# Read Write And Show Video from camera in OpneCV

import cv2

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('Filename and its Extension') if we want to give file manualy then used it
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480)) #cv2.VideoWriter( filename, fourcc, fps, frameSize )

# while(True) or 
while(cap.isOpened()): # .isOpened() --> means if file is opened it gives True otherwise False
    ret , frame = cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # It is used to videocapture in gray 

        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

# Read the documentation for more width and height