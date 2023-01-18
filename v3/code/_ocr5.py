import cv2

width=700
height=700
y1=0
y2=700
x1=500
x2=700
img=cv2.imread('./main.jpg') #read image
#img=cv2.resize(img,(width,height)) #resize image
roi = img[y1:y2, x1:x2] #region of interest i.e where the rectangles will be
gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY) #convert roi into gray
Blur=cv2.GaussianBlur(gray,(5,5),1) #apply blur to roi
Canny=cv2.Canny(Blur,10,50) #apply canny to roi

#Find my contours
contours =cv2.findContours(Canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)[0]

#Loop through my contours to find rectangles and put them in a list, so i can view them individually later.
cntrRect = []
for i in contours:
        epsilon = 0.05*cv2.arcLength(i,True)
        approx = cv2.approxPolyDP(i,epsilon,True)
        if len(approx) == 4:
            cv2.drawContours(roi,cntrRect,-1,(0,255,0),2)
            cv2.imshow('Roi Rect ONLY',roi)
            cntrRect.append(approx)



cv2.waitKey(0)
cv2.destroyAllWindows()