# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())


# load the example image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# check to see if we should apply thresholding to preprocess the
# image
if args["preprocess"] == "thresh":
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# make a check to see if median blurring should be done to remove
# noise
elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)



# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

# show the output images
#cv2.imshow("Image", image)
cv2.imwrite("Output.png", gray)


tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Define path to image
#path_to_image = './en.png'
path_to_image = './Output.png'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Open image with PIL
img = Image.open(path_to_image)

#Extract text from image
ocrText = pytesseract.image_to_string(img  , lang='eng' , config=tessdata_dir_config)

myFont = 'Shabnam FD'
fontSize = 24

window = tk.Tk()
window.title("Image Processing")



window.configure(bg='#333')
#window.grid()
ocrLabel = tk.Label(window, text="پردازش تصویر" , font=(myFont,fontSize) , pady=10 )
ocrLabel.configure(bg='#333', fg='white')
#label_section.grid(row = 0 , column = 0 , columnspan=4)
ocrLabel.pack_propagate(0)
ocrLabel.pack(fill="both", expand=1)

window.geometry('600x240')

ocrLabel.configure(text=ocrText)


window.mainloop()


#cv2.waitKey(0)


#python _ocr2.py --image ./main.jpg