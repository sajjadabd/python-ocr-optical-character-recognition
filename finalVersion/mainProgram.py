import numpy as np
import cv2 as cv

import os

from PIL import Image
from pytesseract import pytesseract

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *




tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Define path to image
#path_to_image = './en.png'
#path_to_image = './billet.jpg'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract



img = cv.imread('./billet.jpg')



imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imwrite("imgray.png" , imgray)
ret, thresh = cv.threshold(imgray, 157, 255, 0)
cv.imwrite("thresh.png" , thresh)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


#gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#gray = np.float32(imgray)
#dst = cv.cornerHarris(gray,2,3,0.04)
#result is dilated for marking the corners, not important
#dst = cv.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
#img[dst>0.01*dst.max()]=[0,255,0]


myFont = 'Tahoma'
fontSize = 24

window = tk.Tk()
window.title("Image Processing")

window.configure(bg='#333')
#window.grid()
ocrLabel = tk.Label(window, text="..." , font=(myFont,fontSize) , pady=10 )
ocrLabel.configure(bg='#333', fg='white')
#label_section.grid(row = 0 , column = 0 , columnspan=4)
ocrLabel.pack_propagate(0)
ocrLabel.pack(fill="both", expand=1)

window.geometry('600x240')


minArea = 5000
maxArea = 500000

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
        
        cut = img[y:y+h , x:x+w]

        rect = cv.minAreaRect(hull)
        box = cv.boxPoints(rect)
        box = np.int0(box)
        cv.drawContours(img,[box],0,(0,0,255),2)
        
        
        cv.imwrite("img_" + str(counter) + ".png" , cut)
        textImage = Image.open("./img_" + str(counter) + ".png")
        ocrText = pytesseract.image_to_string(textImage  , lang='eng' , config=tessdata_dir_config)
        
        if "-" in ocrText :
            ocrLabel.configure(text=ocrText)
            print(ocrText)
        else : 
            os.remove("./img_" + str(counter) + ".png")

        
        
        counter += 1
        
        
print('number of shaped detected : ' , counter)

cv.imwrite("save.png" , img)


window.mainloop()

#To draw all the contours in an image
#cv.drawContours(img, contours, -1, (0,255,0), 3)


#To draw an individual contour, say 4th contour
#cv.drawContours(img, contours, 3, (0,255,0), 3)


#But most of the time, below method will be useful
#cnt = contours[4]
#cv.drawContours(img, [cnt], 0, (0,255,0), 3)

