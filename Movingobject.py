import cv2
#import time
import imutils

cam = cv2.VideoCapture(0)
#time.sleep(1)

firstframe=None
area=500

while True:
    _,img=cam.read()
    text="Aarum Illa"
    qimg=imutils.resize(img,width=1000)
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    Smooth=cv2.GaussianBlur(grayimg,(21,21),0)
    
    if firstframe is None:
        firstframe = Smooth
        continue
    
    imgdiff=cv2.absdiff(firstframe,Smooth)
    threshimg=cv2.threshold(imgdiff,25,255,cv2.THRESH_BINARY)[1]
    threshimg=cv2.dilate(threshimg,None,iterations=2)
    cnts=cv2.findContours(threshimg.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)
    for c in cnts:
            if cv2.contourArea(c)<area:
               continue
        
            (x,y,w,h)=cv2.boundingRect(c)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            text="Aarada Nee Mone"
    print(text)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2)
    cv2.imshow("Camerafeed",img)
    key=cv2.waitKey(1) & 0xFF
    if key==ord("q"):
        break
    
cam.release()
cv2.destroyAllWindows()
        
    
        
    