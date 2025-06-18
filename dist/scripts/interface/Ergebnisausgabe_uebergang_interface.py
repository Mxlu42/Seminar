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
        self.setWindowTitle('Ergebnisausgabe')


        txt = QLabel('Für genauere Informationen<br>bewegen Sie einfach Ihren Coursor über den Knopf<br>der Sie interressiert, und warten Sie zwei Sekunden.', self)
        txt.setMinimumSize(QSize(400, 100))
        txt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        txt.move(self.Center(txt), 30)

        bmh = 150

        

        k11 = QLabel('<u>Klasse 11 (Eingangsklasse)</u>', self)
        k11.setFixedWidth(200)
        k11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        k11.move(self.Center(k11), bmh)
        bmh += 40

        fw11 = QPushButton('Ausgabe der Klasse 11', self)
        fw11.resize(fw11.sizeHint())
        fw11.setToolTip('Eine geordnete Übersicht der Klasse 11<br>mit möglichkeit sie als .pdf zu Speichern')
        fw11.clicked.connect(self.fw11_clicked)
        fw11.move(self.Center(fw11), bmh)
        bmh += 40

        k12 = QLabel('<u>Klasse 12 (Jahrgangsstufe 1)</u>', self)
        k12.setFixedWidth(200)
        k12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        k12.move(self.Center(k12), bmh)
        bmh += 40

        fw12 = QPushButton('Ausgabe der Klasse 12', self)
        fw12.resize(fw12.sizeHint())
        fw12.setToolTip('Eine geordnete Übersicht der Klasse 12<br>mit möglichkeit sie als .pdf zu Speichern')
        fw12.clicked.connect(self.fw12_clicked)
        fw12.move(self.Center(fw12), bmh)
        bmh += 40

        k13 = QLabel('<u>Klasse 13 (Jahrgangsstufe 2)</u>', self)
        k13.setFixedWidth(200)
        k13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        k13.move(self.Center(k13), bmh)
        bmh += 40

        fw13 = QPushButton('Ausgabe der Klasse 13', self)
        fw13.resize(fw13.sizeHint())
        fw13.setToolTip('Eine geordnete Übersicht der Klasse 13<br>mit möglichkeit sie als .pdf zu Speichern')
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

    

    def fw11_clicked(self):
        lnh = Launcher('elfteklassewahl')
        lnh.launch()

    
    def fw12_clicked(self):
        print('Weiterleitung zur Seite "Faecherwahl 12"')
        lnh = Launcher('elfteklassewahl')
        lnh.launch()

    
    def fw13_clicked(self):
        print('Weiterleitung zur Seite "Faecherwahl 13"')
        lnh = Launcher('pruefae_interface')
        lnh.launch()

    def back(self):
        pipi = Launcher('homepage')
        pipi.launch()



app = QtWidgets.QApplication(sys.argv)
win = Ergebnisausgabe()
win.show()
sys.exit(app.exec())