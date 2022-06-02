from decimal import getcontext
from trace import Trace
import cv2
from cv2 import namedWindow
import numpy as np

def empty(a):
    pass


###########################

widthImg = 640
heightImg = 480

###########################

cap = cv2.VideoCapture(0)
cap.set(3,widthImg)
cap.set(4,heightImg)



def preProcessing(img):
    kernel = np.ones((5,5))

    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,50,70)
    imgDial = cv2.dilate(imgCanny,kernel,iterations=2)
    imgTres = cv2.erode(imgDial,kernel,iterations=1)

    return imgTres

def reorder(myPoints):
    print('old',myPoints)
    myPoints = myPoints.reshape(4,2)
    myPointsNew = np.zeros((4,1,2),np.int32)

    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]

    diff = np.diff(myPoints,axis=1)
   
    myPointsNew[2] = myPoints[np.argmin(diff)]
    myPointsNew[1] = myPoints[np.argmax(diff)]
    print('new',myPointsNew)
   
    

    

    return myPointsNew

def getWarp(img,biggest):
    try:
        biggest = reorder(biggest)
        pts1 = np.float32(biggest)
        pts2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        imgOutput = cv2.warpPerspective(img,matrix,(widthImg,heightImg))
        return imgOutput
    except:
        return img

def getContours(img):
    biggest = np.array
    maxArea = 0
    contours , heirarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print(area)
        if area >5000:
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            if area > maxArea and len(approx)==4:
                biggest = approx
                maxArea = area
    try:
        cv2.drawContours(imgContour,biggest,-1,(0,255,0),10)
    except:
        pass
    return biggest

while True:
    success, img = cap.read()
    img = cv2.resize(img,(widthImg,heightImg))
    imgThres = preProcessing(img)
    imgContour = img.copy()
    

    biggest = getContours(imgThres)

    imgOutput = getWarp(img,biggest)

    #cv2.imshow('webcam',img)
    #cv2.imshow('result',imgThres)
    cv2.imshow('contour',imgContour)
    cv2.imshow('warped',imgOutput)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


