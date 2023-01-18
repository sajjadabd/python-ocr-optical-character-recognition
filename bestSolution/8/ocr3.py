import numpy as np
import cv2 as cv


img = cv.imread('./billet.jpg')
#blur = cv.GaussianBlur(img,(25,25),0)

#cv.imwrite("blur.png" , blur)

imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

kernel = np.ones((2,2),np.uint8)
erosion = cv.erode(imgray,kernel,iterations = 5)
cv.imwrite("erosion.png" , erosion)

dilation = cv.dilate(imgray,kernel,iterations = 1)
cv.imwrite("dilation.png" , dilation)
opening = cv.morphologyEx(imgray, cv.MORPH_OPEN, kernel)
cv.imwrite("opening.png" , opening)
closing = cv.morphologyEx(imgray, cv.MORPH_CLOSE, kernel)
cv.imwrite("closing.png" , closing)
gradient = cv.morphologyEx(imgray, cv.MORPH_GRADIENT, kernel)
cv.imwrite("gradient.png" , gradient)


ret, thresh = cv.threshold(erosion, 127, 255, 0)
#edge = cv.Canny(imgray,200,300,True)

#cv.imwrite("canny.png" , edge)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


minArea = 10000
maxArea = 100000

counter = 0
for cnt in contours :
    area = cv.contourArea(cnt)
    if area > minArea and area < maxArea :
        #perimeter = cv.arcLength(cnt,True)
        epsilon = 0.01*cv.arcLength(cnt,True)
        approx = cv.approxPolyDP(cnt,epsilon,True)
        cv.drawContours(img, [approx], 0, (0,255,0), 3)
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

