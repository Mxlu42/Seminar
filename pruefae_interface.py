import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox, QComboBox, QRadioButton
from PyQt6.QtCore import QSize, Qt
from PruefungsFaecherPossible import *
class Pruefungsfaecherwahl(QMainWindow):
    def __init__(self):
        super().__init__()
        pfc = PruefungsfaecherPossible()
        #Mindestgröße / Titel definieren
        self.setCentralWidget(QWidget(self))
        self.setMinimumSize(QSize(500, 600))
        self.setMaximumSize(QSize(500, 600))
        self.setWindowTitle('Prüfungsfächerwahl')

        lbl = QLabel('Platzhalter für den Erklärtext')
        lbl.resize(lbl.sizeHint())
        lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        lbl.setMargin(30)
        self.setCentralWidget(lbl)

        cbb1 = QComboBox(self)
        cbb1.addItems(pfc.getPFP1())
        cbb1.resize(cbb1.sizeHint())
        self.setCentralWidget(cbb1)





#Anzeigen / Ausführen des Programms als sepeates Fenster
app = QtWidgets.QApplication(sys.argv)
win = Pruefungsfaecherwahl()
win.show()
sys.exit(app.exec())