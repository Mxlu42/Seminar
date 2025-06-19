import sys
import os
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit, QMessageBox, QComboBox, QVBoxLayout
from PyQt6.QtCore import QSize, Qt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from heart import Launcher
from dbhelp import *

class Ergebnisausgabe(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setCentralWidget(QWidget(self))
        self.setMinimumSize(QSize(500, 600))
        self.setMaximumSize(QSize(500, 600))
        self.setWindowTitle('Noteneingabe Klasse 12')


        txt = QLabel('Für genauere Informationen<br>bewegen Sie einfach Ihren Coursor über den Knopf<br>der Sie interressiert, und warten Sie zwei Sekunden.', self)
        txt.setMinimumSize(QSize(400, 100))
        txt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        txt.move(self.Center(txt), 30)

        bmh = 150

        k12 = QLabel('<u>Klasse 12 (Jahrgangsstufe 1)</u>', self)
        k12.setFixedWidth(200)
        k12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        k12.move(self.Center(k12), bmh)
        bmh += 40

        fw12 = QPushButton('Eingabe der Klasse 12/1', self)
        fw12.resize(fw12.sizeHint())
        fw12.setToolTip('Hier geben sie alle ihre Noten des Halbjahres 12/1 ein')
        fw12.clicked.connect(self.fw12_clicked)
        fw12.move(self.Center(fw12), bmh)
        bmh += 40

        fw13 = QPushButton('Eingabe der Klasse 12/2', self)
        fw13.resize(fw13.sizeHint())
        fw13.setToolTip('Hier geben sie alle ihre Noten des Halbjahres 12/2 ein')
        fw13.clicked.connect(self.fw13_clicked)
        fw13.move(self.Center(fw13), bmh)
        bmh += 40

        backwid = QWidget(self)
        backbox = QVBoxLayout(backwid)
        backwid.setMinimumSize(100, 50)
        backwid.setMaximumSize(100, 50)
        backwid.move(10, 540)

        backb = QPushButton('Zurück')
        backb.resize(backb.sizeHint())
        backb.clicked.connect(self.back)
        backbox.addWidget(backb)




    def Center(self, x):
        w = x.width()
        return 250 - (w // 2)

    


    
    def fw12_clicked(self):
        print('Weiterleitung zur Seite "Noteneingabe 12/1"')
        lnh = Launcher('Noteneingabe12_1_interface')
        lnh.launch()

    
    def fw13_clicked(self):
        print('Weiterleitung zur Seite "Noteneingabe 12/2"')
        lnh = Launcher('Noteneingabe12_2_interface')
        lnh.launch()

    def back(self):
        pipi = Launcher('homepage')
        pipi.launch()



app = QtWidgets.QApplication(sys.argv)
win = Ergebnisausgabe()
win.show()
sys.exit(app.exec())