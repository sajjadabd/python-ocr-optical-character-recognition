import cv2
import numpy as np


image = cv2.imread('./main.png')
original = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([0, 208, 94], dtype="uint8")
upper = np.array([179, 255, 232], dtype="uint8")
mask = cv2.inRange(image, lower, upper)

# Find contours
cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Extract contours depending on OpenCV version
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

# Iterate through contours and filter by the number of vertices 
for c in cnts:
   perimeter = cv2.arcLength(c, True)
   approx = cv2.approxPolyDP(c, 0.04 * perimeter, True)
   if len(approx) > 5:
       cv2.drawContours(original, [c], -1, (36, 255, 12), -1)

cv2.imshow('mask', mask)
cv2.imshow('original', original)
cv2.waitKey()


"""
import cv2
import numpy as np

image = cv2.imread('./main.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = np.array([10, 0, 0], dtype="uint8") 
upper = np.array([15, 255, 255], dtype="uint8")

hue = image[:,:,0]
cv2.imshow('hue', hue)

cv2.imshow('hue', (hue-np.min(hue))/(np.max(hue)-np.min(hue))*255)
"""