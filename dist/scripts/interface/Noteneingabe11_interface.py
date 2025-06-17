import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit, QMessageBox, QComboBox, QRadioButton, QScrollArea, QVBoxLayout, QCheckBox
from PyQt6.QtCore import QSize, Qt
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from heart import Launcher
from dbhelp import DBHelp

class Noteneingabe11(QMainWindow):
    def __init__(self):
        db = DBHelp()
        print(db.getArrayAusAllenFaechernAndFaechertypseAndGesamtnoteInBestimmtemHalbJahr(0))
        super().__init__()
        
        #Mindestgröße / Titel definieren
        self.setCentralWidget(QWidget(self))
        self.setMinimumSize(QSize(500, 600))
        self.setMaximumSize(QSize(500, 600))
        self.setWindowTitle('Klammerung')

        main_widget = QWidget()
        main_layout = QVBoxLayout()

        lbl = QLabel('Platzhalter für den Erklärtext')
        lbl.resize(lbl.sizeHint())
        lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        lbl.setMargin(30)
        main_layout.addWidget(lbl)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        

        scroll_content = QWidget()
        grid_layout = QGridLayout()
        

        column = 0
        row = 1

        for s in [ '<b>Fach</b>', '<b>Note</b>']:
            lbl = QLabel(s)
            lbl.resize(lbl.sizeHint())
            grid_layout.addWidget(lbl, 0, column,  Qt.AlignmentFlag.AlignLeft)
            column += 1

        for i in range(30):
            lbl = QLabel('Test')
            lbl.resize(lbl.sizeHint())
            grid_layout.addWidget(lbl, row, 0,  Qt.AlignmentFlag.AlignLeft)
            grid_layout.setRowMinimumHeight(row, 30)
            row += 1

        row = 1
        column = 1

        for i in range(30):
            name = QComboBox()
            name.addItem('Bitte Note wählen')
            name.addItem('1')
            name.addItem('2')
            name.addItem('3')
            name.addItem('4')
            name.addItem('5')
            name.addItem('6')
            grid_layout.addWidget(name, row, 1,  Qt.AlignmentFlag.AlignLeft)
            row += 1
            

        scroll_content.setLayout(grid_layout)
        scroll_area.setWidget(scroll_content)


        main_layout.addWidget(scroll_area)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


        backb = QPushButton('Zurück')
        backb.resize(backb.sizeHint())
        backb.clicked.connect(self.back)
        main_layout.addWidget(backb)

        

        

    def NBox(self):
        name = QComboBox()
        name.addItem('Bitte Note wählen')
        name.addItem('1')
        name.addItem('2')
        name.addItem('3')
        name.addItem('4')
        name.addItem('5')
        name.addItem('6')

    def back(self):
        pipi = Launcher('homepage')
        pipi.launch()





#Anzeigen / Ausführen des Programms als sepeates Fenster
app = QtWidgets.QApplication(sys.argv)
win = Noteneingabe11()
win.show()
sys.exit(app.exec())