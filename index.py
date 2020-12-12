# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from os import path
import sys
from phonenumbers import geocoder, carrier, timezone
import phonenumbers

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "main.ui"))

class MainApp(QWidget, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.Handel_UI()
        self.Handel_Buttons()

    def Handel_UI(self):
        self.setWindowTitle("Phone Number Info")
        self.setFixedSize(376, 219)

    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.search)

    def search(self):
        number = self.lineEdit.text()
        number = phonenumbers.parse(number)
        self.label_7.setText(str(number.country_code))
        self.label_8.setText(str(phonenumbers.national_significant_number(number)))
        self.label_9.setText(str(geocoder.country_name_for_number(number, 'en')))
        self.label_10.setText(str(carrier.name_for_number(number, 'en')))
        self.label_12.setText(str(timezone.time_zones_for_geographical_number(number)[0]))

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
