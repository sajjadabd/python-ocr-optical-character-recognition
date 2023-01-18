import numpy as np
import cv2 as cv


img = cv.imread('./billet.jpg')

imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#To draw all the contours in an image
cv.drawContours(img, contours, -1, (0,255,0), 3)

cv.imwrite("save.png" , img)

#To draw an individual contour, say 4th contour
#cv.drawContours(img, contours, 3, (0,255,0), 3)


#But most of the time, below method will be useful
#cnt = contours[4]
#cv.drawContours(img, [cnt], 0, (0,255,0), 3)

