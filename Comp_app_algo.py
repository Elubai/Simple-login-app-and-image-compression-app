# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2nd_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
from PyQt5.uic import loadUi

from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5 import QtCore, QtWidgets
import PIL
from PIL import Image

class Ui_Comp_app(object):
    def setupUi(self, Comp_app):
        Comp_app.setObjectName("Comp_app")
        Comp_app.resize(567, 626)
        Comp_app.setStyleSheet("*{\n"
"    font-famly:century gothic;\n"
"    font-size:24px;\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"    background:#333;\n"
"    border-radius:15px;\n"
"}\n"
"#Comp_app\n"
"{\n"
"    background: #333;\n"
"}\n"
"QPushButton\n"
"{\n"
"  background:red;\n"
"  border-radius:60px;\n"
"}\n"
"\n"
"QToolButton\n"
"{\n"
"    background:red;\n"
"    border-radius:60px;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    color: white;\n"
"background:red;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: white;\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   color: #333;\n"
"   border-radius:15px;\n"
"   background:#49ebff;\n"
"}\n"
"Qimage_path\n"
"{ \n"
"   background: red;\n"
"   border:none;\n"
"   color: #717072;\n"
"   border-bottom:1px solid #717072;\n"
"}")
        self.label = QtWidgets.QLabel(Comp_app)
        self.label.setGeometry(QtCore.QRect(70, 60, 431, 61))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.image_path = QtWidgets.QTextEdit(Comp_app)
        self.image_path.setGeometry(QtCore.QRect(50, 170, 271, 61))
        self.image_path.setStyleSheet("*{\n"
"background:red;\n"
"}")
        self.image_path.setObjectName("image_path")
        self.Browse = QtWidgets.QPushButton(Comp_app)
        self.Browse.setGeometry(QtCore.QRect(350, 170, 161, 61))
        self.Browse.setObjectName("Browse")
        self.compress_button = QtWidgets.QPushButton(Comp_app)
        self.compress_button.setGeometry(QtCore.QRect(40, 310, 241, 61))
        self.compress_button.setObjectName("compress_button")
        self.original = QtWidgets.QPushButton(Comp_app)
        self.original.setGeometry(QtCore.QRect(30, 450, 281, 41))
        self.original.setObjectName("original")
        self.compressed = QtWidgets.QPushButton(Comp_app)
        self.compressed.setGeometry(QtCore.QRect(30, 520, 281, 41))
        self.compressed.setObjectName("compressed")
        self.logout = QtWidgets.QPushButton(Comp_app)
        self.logout.setGeometry(QtCore.QRect(420, 520, 111, 41))
        self.logout.setObjectName("logout")

        self.retranslateUi(Comp_app)
        QtCore.QMetaObject.connectSlotsByName(Comp_app)

    def retranslateUi(self, Comp_app):
        _translate = QtCore.QCoreApplication.translate
        Comp_app.setWindowTitle(_translate("Comp_app", "Form"))
        self.label.setText(_translate("Comp_app", "   Welcome to compression image app"))
        self.image_path.setHtml(_translate("Comp_app", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:24px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Browse.setText(_translate("Comp_app", "Browse"))
        self.compress_button.setText(_translate("Comp_app", "Compress image"))
        self.original.setText(_translate("Comp_app", "Show original image"))
        self.compressed.setText(_translate("Comp_app", "Show compressed image"))
        self.logout.setText(_translate("Comp_app", "Log-out"))

        # Connection
        self.Browse.clicked.connect(self.browse)

        self.compress_button.clicked.connect(self.compress_image)


        self.logout.clicked.connect(lambda:self.log_out(Comp_app))

        self.original.clicked.connect(self.open_original)
        self.compressed.clicked.connect(self.open_compressed)




    def browse(self):
        self.fname = QFileDialog.getOpenFileName(None, 'Open file', 'C:\\\'', 'Images (*.png)')
        self.image_path.setText(self.fname[0].replace('/', '\\\\'))


    def compress_image(self):
        self.img = PIL.Image.open(self.fname[0].replace('/', '\\\\'))
        self.filename = self.fname[0].replace('/', '\\\\').split('\\')[-1].split('.')[0]
        self.img.save(f'{self.filename}_compressed.png', optimize=True, quality=40)

    def log_out(self, Form):
        Form.hide()

    def open_original(self):
        self.im = Image.open(self.fname[0].replace('/', '\\\\'))
        self.im.show()


    def open_compressed(self):
        self.im_comp = Image.open(self.fname[0].replace('/', '\\\\'))
        self.im_comp.show(f'{self.filename}_compressed_.png')


