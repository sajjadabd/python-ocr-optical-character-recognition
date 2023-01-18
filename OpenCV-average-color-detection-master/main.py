# -*- coding: utf-8 -*-

"""
OpenCV Python image average color detection script. You can use this to finding darkest color.
Coded by : Lakmal Niranga. 2016
"""

import os
import cv2
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(790, 550)
        Dialog.setSizeGripEnabled(True)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 230, 361, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnImg1_pc = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnImg1_pc.setObjectName(_fromUtf8("btnImg1_pc"))
        self.horizontalLayout.addWidget(self.btnImg1_pc)
        self.btnImg1_cam = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnImg1_cam.setObjectName(_fromUtf8("btnImg1_cam"))
        self.horizontalLayout.addWidget(self.btnImg1_cam)
        self.label_img1 = QtGui.QLabel(self.frame)
        self.label_img1.setGeometry(QtCore.QRect(10, 10, 361, 211))
        self.label_img1.setText(_fromUtf8(""))
        self.label_img1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img1.setObjectName(_fromUtf8("label_img1"))
        self.horizontalLayoutWidget.raise_()
        self.label_img1.raise_()
        self.frame_3 = QtGui.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(400, 10, 381, 281))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.frame_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 230, 361, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnImg2_pc = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.btnImg2_pc.setObjectName(_fromUtf8("btnImg2_pc"))
        self.horizontalLayout_2.addWidget(self.btnImg2_pc)
        self.btnImg2_cam = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.btnImg2_cam.setObjectName(_fromUtf8("btnImg2_cam"))
        self.horizontalLayout_2.addWidget(self.btnImg2_cam)
        self.label_img2 = QtGui.QLabel(self.frame_3)
        self.label_img2.setGeometry(QtCore.QRect(10, 10, 361, 211))
        self.label_img2.setText(_fromUtf8(""))
        self.label_img2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img2.setObjectName(_fromUtf8("label_img2"))
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 370, 771, 41))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 410, 381, 143))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.colorbox_1 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.colorbox_1.setText(_fromUtf8(""))
        self.colorbox_1.setObjectName(_fromUtf8("colorbox_1"))
        self.verticalLayout_2.addWidget(self.colorbox_1)
        self.lable_img1 = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lable_img1.setFont(font)
        self.lable_img1.setAlignment(QtCore.Qt.AlignCenter)
        self.lable_img1.setObjectName(_fromUtf8("lable_img1"))
        self.verticalLayout_2.addWidget(self.lable_img1)
        self.verticalLayoutWidget_3 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(400, 410, 381, 143))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.colorbox_2 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.colorbox_2.setText(_fromUtf8(""))
        self.colorbox_2.setObjectName(_fromUtf8("colorbox_2"))
        self.verticalLayout_3.addWidget(self.colorbox_2)
        self.lable_img2 = QtGui.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lable_img2.setFont(font)
        self.label_img1.setObjectName(_fromUtf8("label_img1"))
        self.horizontalLayoutWidget.raise_()
        self.lable_img2.setAlignment(QtCore.Qt.AlignCenter)
        self.lable_img2.setObjectName(_fromUtf8("lable_img2"))
        self.verticalLayout_3.addWidget(self.lable_img2)
        self.btnComp = QtGui.QPushButton(Dialog)
        self.btnComp.setGeometry(QtCore.QRect(310, 310, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnComp.setFont(font)
        self.btnComp.setObjectName(_fromUtf8("btnComp"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "OpenCV Darkest Cloth Identifier", None))
        self.btnImg1_pc.setText(_translate("Dialog", "Select image from PC", None))
        self.btnImg1_cam.setText(_translate("Dialog", "Take image from camera", None))
        self.btnImg2_pc.setText(_translate("Dialog", "Select image from PC", None))
        self.btnImg2_cam.setText(_translate("Dialog", "Take image from camera", None))
        self.label.setText(_translate("Dialog", "Most Suitable Average Color", None))
        self.lable_img1.setText(_translate("Dialog", "", None))
        self.lable_img2.setText(_translate("Dialog", "", None))
        self.btnComp.setText(_translate("Dialog", "Compare", None))

        self.btnImg1_pc.clicked.connect(self.openimg1)
        self.btnImg2_pc.clicked.connect(self.openimg2)
        self.btnComp.clicked.connect(self.compare_color)
        self.btnImg1_cam.clicked.connect(self.cameraImg1)
        self.btnImg2_cam.clicked.connect(self.cameraImg2)

    avg1=None
    avg2=None

    def get_avg_color(self, img_path):
    	img = cv2.imread(img_path,cv2.IMREAD_COLOR)

    	img_width = img.shape[1]
    	img_height = img.shape[0]

    	rows_cols = 10

    	part_of_width = img_width/rows_cols
    	part_of_height = img_height/rows_cols

    	avg_B=0
    	avg_G=0
    	avg_R=0

    	for x in range(part_of_width,img_width-part_of_width,part_of_width):
    		for y in range(part_of_height,img_height-part_of_height,part_of_height):
    			color = img[y,x] #[y and x] - gives BGR
    			avg_B+=color[0]
    			avg_G+=color[1]
    			avg_R+=color[2]
    			cv2.circle(img,(x,y), 5, (0,0,0), -1) #[x and y]

    	return (avg_B/81,avg_G/81,avg_R/81)[::-1] #return tuple in BGR

    def openimg1(self):
        global avg1
        img1_path = QtGui.QFileDialog.getOpenFileName(Dialog, 'Open file', os.getcwd() ,"Image files (*.jpg *.gif)")
        self.label_img1.setScaledContents(True)
        self.label_img1.setPixmap(QtGui.QPixmap(img1_path))
        avg1 = self.get_avg_color(str(img1_path))
        self.colorbox_1.setStyleSheet('background-color: rgb'+ str(avg1))

    def openimg2(self):
        global avg2
        img2_path = QtGui.QFileDialog.getOpenFileName(Dialog, 'Open file', os.getcwd() ,"Image files (*.jpg *.gif)")
        self.label_img2.setScaledContents(True)
        self.label_img2.setPixmap(QtGui.QPixmap(img2_path))
        avg2 = self.get_avg_color(str(img2_path))
        self.colorbox_2.setStyleSheet('background-color: rgb'+ str(avg2))

    def compare_color(self):
        global avg1, avg2

        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Critical)

        try:
            img1_avarage = sum(i for i in avg1)
            img2_avarage = sum(i for i in avg2)

            avg1_per = (float(img1_avarage)/(img1_avarage+img2_avarage))*100
            avg2_per = (float(img2_avarage)/(img1_avarage+img2_avarage))*100

            self.lable_img1.setText(str(round(100-avg1_per, 2)) + "%")
            self.lable_img2.setText(str(round(100-avg2_per, 2)) + "%")
        except NameError as e:
            msgBox.setText("Please select images first!")
            msgBox.setWindowTitle("Error")
            msgBox.exec_()


    def cameraImg1(self):
        global avg1
        cap = cv2.VideoCapture(0)

        while(True):
            global avg1

            ret, frame = cap.read()

            cv2.imshow('press S to take image | press C to cancel',frame)
            k = cv2.waitKey(3) & 0xFF
            if k == ord('s'):
                img_path="image1.jpg"
                cv2.imwrite(img_path, frame)
                self.label_img1.setScaledContents(True)
                self.label_img1.setPixmap(QtGui.QPixmap(img_path))
                avg1 = self.get_avg_color(str(img_path))
                self.colorbox_1.setStyleSheet('background-color: rgb'+ str(avg1))
                break
            if k == ord('c'):
                break
        cap.release()
        cv2.destroyAllWindows()

    def cameraImg2(self):
        global avg2
        cap = cv2.VideoCapture(0)

        while(True):
            global avg2

            ret, frame = cap.read()

            cv2.imshow('press S to take image | press C to cancel',frame)
            k = cv2.waitKey(3) & 0xFF
            if k == ord('s'):
                img_path="image2.jpg"
                cv2.imwrite(img_path, frame)
                self.label_img2.setScaledContents(True)
                self.label_img2.setPixmap(QtGui.QPixmap(img_path))
                avg2 = self.get_avg_color(str(img_path))
                self.colorbox_2.setStyleSheet('background-color: rgb'+ str(avg2))
                break
            if k == ord('c'):
                break
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    Dialog.setFixedSize(790, 550)
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
