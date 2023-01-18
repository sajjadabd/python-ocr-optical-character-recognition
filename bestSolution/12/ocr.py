import numpy as np
import cv2 as cv


img = cv.imread('./billet.jpg')

imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imwrite("imgray.png" , imgray)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
#cv.imwrite("thresh.png" , thresh)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


#gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#gray = np.float32(imgray)
#dst = cv.cornerHarris(gray,2,3,0.04)
#result is dilated for marking the corners, not important
#dst = cv.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
#img[dst>0.01*dst.max()]=[0,255,0]



minArea = 10000
maxArea = 50000

counter = 0
for cnt in contours :
    area = cv.contourArea(cnt)
    if area > minArea and area < maxArea :
        #perimeter = cv.arcLength(cnt,True)
        epsilon = 0.001*cv.arcLength(cnt,True)
        approx = cv.approxPolyDP(cnt,epsilon,True)
        #if cv.isContourConvex(approx) == True :
        hull = cv.convexHull(cnt)
        #cv.drawContours(img, [hull], 0, (0,255,0), 3)
        
        x,y,w,h = cv.boundingRect(cnt)
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cut = img[y:y+h,x:x+w]
        cv.imwrite("save_" + str(counter) + ".png" , cut)

        rect = cv.minAreaRect(hull)
        box = cv.boxPoints(rect)
        box = np.int0(box)
        cv.drawContours(img,[box],0,(0,0,255),2)
        
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

