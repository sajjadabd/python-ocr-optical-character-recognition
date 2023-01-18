from PIL import Image
from pytesseract import pytesseract

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *

#pip install opencv-python
#pip install pytesseract
#pip install pillow



#https://python-bloggers.com/2022/05/extract-text-from-image-using-python/
#https://www.section.io/engineering-education/extract-text-from-images-using-pytesseract/
#https://nanonets.com/blog/ocr-with-tesseract/
#https://www.tutorialspoint.com/how-to-detect-a-rectangle-and-square-in-an-image-using-opencv-python




tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Define path to image
path_to_image = './en.png'
#path_to_image = './billet.jpg'

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


print(ocrText)

window.mainloop()





