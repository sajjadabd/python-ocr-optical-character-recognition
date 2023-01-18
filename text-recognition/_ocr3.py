import cv2
from pytesseract import Output

from PIL import Image
from pytesseract import pytesseract


#img = cv2.imread('./billet.png')

tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Define path to image
#path_to_image = './en.png'
path_to_image = './main.png'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Open image with PIL
img = Image.open(path_to_image)


d = pytesseract.image_to_string(img, lang='eng' , config=tessdata_dir_config)


print(d)
"""
n_boxes = len(d['text'])
print(d['text'])
print(n_boxes)
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imwrite('img.png', img)
"""
#cv2.waitKey(0)