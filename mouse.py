import cv2
import numpy as np
import time
from cvzone import HandTrackingModule as htm
import pyautogui

wCam,hCam=640,480
frameReduction=100
smoothening = 7
cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

plocX,plocY=0,0
clocX,clocY=0,0
pTime=0
detector=htm.HandDetector(maxHands=1)
wScr,hScr=pyautogui.size()
while True:
    success,img=cap.read()
    allhands,img=detector.findHands(img)
    lmList=allhands[0]["lmList"]
    if len(lmList)!=0:
        x1, y1 = lmList[8][:2]
        x2, y2 = lmList[12][:2]
        
        
        fingers=detector.fingersUp(allhands[0])
        # print(fingers)
        cv2.rectangle(img,(frameReduction,frameReduction),(wCam-frameReduction,hCam-frameReduction),(255,0,255),2)
        
        if fingers[1]==1 and fingers[2]==0:
            
            
            
            x3=np.interp(x1,(frameReduction,wCam-frameReduction),(0,wScr))
            y3=np.interp(y1,(frameReduction,hCam-frameReduction),(0,hScr))
            
            clocX=plocX+(x3-plocX)/smoothening
            clocY=plocY+(y3-plocY)/smoothening
            
            
            pyautogui.moveTo(wScr-clocX,clocY)
            cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
            plocX,plocY=clocX,clocY
            
        if fingers[1]==1 and fingers[2]==1:
            
            length,lineInfo,img=detector.findDistance(lmList[8][:2],lmList[12][:2],img)
            print(length)
            if length<30:
                cv2.circle(img,(lineInfo[4],lineInfo[5]),15,(0,255,0),cv2.FILLED)
                
                pyautogui.click()
        if fingers[0]==0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3]==1 and fingers[4]==1:

            
        
            pyautogui.rightClick()
        if fingers[0]==0 and fingers[1]==1 and fingers[2]==1 and fingers[3]==1 and fingers[4]==0:
            pyautogui.doubleClick()
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("image",img)
    cv2.waitKey(1)
    