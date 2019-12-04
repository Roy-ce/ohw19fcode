import numpy as np
import cv2
lenth=1024
width=678
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def drawface(x,y,w,h,img):
    fc=x+w/2
    mid=lenth/2
    limit=50
    if fc<mid-limit:
        a=255
        b=0
#        print('l\n')
    elif fc>mid+limit:
        a=0
        b=255
#        print('r\n')
    else:
        a=255
        b=255
    cv2.rectangle(img,(0,0),(x,y),(a,b,0),5)
    cv2.rectangle(img,(x,0),(x+w,y),(a,b,0),5)
    cv2.rectangle(img,(x+w,0),(lenth,y),(a,b,0),5)
    cv2.rectangle(img,(0,y),(x,y+h),(a,b,0),5)
    cv2.rectangle(img,(x+w,y),(lenth,y+h),(a,b,0),5)
    cv2.rectangle(img,(0,y+h),(x,width),(a,b,0),5)
    cv2.rectangle(img,(x,y+h),(x+w,width),(a,b,0),5)
    cv2.rectangle(img,(x+w,y+h),(lenth,width),(a,b,0),5)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.resize(frame,(lenth,width),interpolation=cv2.INTER_CUBIC)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        drawface(x,y,w,h,gray)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
