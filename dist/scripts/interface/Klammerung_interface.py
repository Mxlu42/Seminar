import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox, QComboBox, QRadioButton
from PyQt6.QtCore import QSize, Qt
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from heart import Launcher
from dbhelp import getfaechermitnoten1213                                                                       #Miron muss noch schreiben

class SubjectChoice11(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Mindestgröße / Titel definieren
        self.setCentralWidget(QWidget(self))
        self.setMinimumSize(QSize(500, 600))
        self.setMaximumSize(QSize(500, 600))
        self.setWindowTitle('Klammerung')

        lbl = QLabel('Platzhalter für den Erklärtext')
        lbl.resize(lbl.sizeHint())
        lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        lbl.setMargin(30)
        self.setCentralWidget(lbl)

        
    def back(self):
        pipi = Launcher('homepage')
        pipi.launch()





#Anzeigen / Ausführen des Programms als sepeates Fenster
app = QtWidgets.QApplication(sys.argv)
win = SubjectChoice11()
win.show()
sys.exit(app.exec())