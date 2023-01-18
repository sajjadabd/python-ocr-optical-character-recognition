import numpy as np
import cv2 as cv


img = cv.imread('./billet.jpg')

imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


minArea = 10000

counter = 0
for cnt in contours :
    area = cv.contourArea(cnt)
    if area > minArea :
        #perimeter = cv.arcLength(cnt,True)
        epsilon = 0.01*cv.arcLength(cnt,True)
        approx = cv.approxPolyDP(cnt,epsilon,True)
        #if cv.isContourConvex(approx) == True :
        #hull = cv.convexHull(cnt)
        #cv.drawContours(img, [hull], 0, (0,255,0), 3)
        x,y,w,h = cv.boundingRect(approx)
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        counter += 1
        
        
print('number of shaped detected : ' , counter)

cv.imwrite("save.png" , img)


#To draw all the contours in an image
#cv.drawContours(img, contours, -1, (0,255,0), 3)


#To draw an individual contour, say 4th contour
#cv.drawContours(img, contours, 3, (0,255,0), 3)


#But most of the time, below method will be useful
#cnt = contours[4]
#cv.drawContours(img, [cnt], 0, (0,255,0), 3)

