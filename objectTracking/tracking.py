import cv2 as cv
import numpy as np

# Take each frame
frame = cv.imread('./billet.jpg')


# Convert BGR to HSV
hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
# define range of blue color in HSV
lower_blue = np.array([0,0,0])
upper_blue = np.array([165,165,165])
# Threshold the HSV image to get only blue colors
mask = cv.inRange(hsv, lower_blue, upper_blue)
# Bitwise-AND mask and original image
res = cv.bitwise_and(frame,frame, mask= mask)
cv.imwrite('frame.png',frame)
cv.imwrite('mask.png',mask)
cv.imwrite('res.png',res)
    