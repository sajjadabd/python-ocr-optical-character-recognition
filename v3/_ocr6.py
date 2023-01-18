import cv2
import numpy as np

img = cv2.imread("./main.jpg")

cut = ''
tresh = ''

def process(img):
    global tresh 
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY)
    img_blur = cv2.GaussianBlur(thresh, (5, 5), 2)
    img_canny = cv2.Canny(img_blur, 0, 0)
    return img_canny

def get_contours(img):
    global cut 
    contours, _ = cv2.findContours(process(img), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    r1, r2 = sorted(contours, key=cv2.contourArea)[-3:-1]
    x, y, w, h = cv2.boundingRect(np.r_[r1, r2])
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cut = img[y:y+h , x:x+w]

get_contours(img)

cv2.imshow("img_processed", img)

cv2.imwrite("final.jpg" , cut)

cv2.waitKey(0)