import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit, QMessageBox, QComboBox, QRadioButton, QScrollArea, QVBoxLayout, QCheckBox, QHBoxLayout
from PyQt6.QtCore import QSize, Qt
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from heart import Launcher
#from scripts.dbhelp import DBHelp

class Klammerung(QMainWindow):
    def __init__(self):
        global grid_layout
        #all = DBHelp.getFaecherMitNoten1213()

        #faecher = all[0]
        #noten = all[1]

        self.cbs = []

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

        for s in [ '<b>Fach</b>', '<b>HJ1</b>', '<b>HJ2</b>', '<b>HJ3</b>', '<b>HJ4</b>']:
            lbl = QLabel(s)
            lbl.resize(lbl.sizeHint())
            grid_layout.addWidget(lbl, 0, column,  Qt.AlignmentFlag.AlignLeft)
            column += 1

        for i in range(31):                                                                         #spaeter liste der belegten Faecher
            lbl = QLabel(f'test {str(i+1)}')
            lbl.resize(lbl.sizeHint())
            grid_layout.addWidget(lbl, row, 0,  Qt.AlignmentFlag.AlignLeft)
            grid_layout.setRowMinimumHeight(row, 30)
            row += 1

        row = 1
        column = 1

        self.cb_col1 = []
        self.cb_col2 = []
        self.cb_col3 = []
        self.cb_col4 = []

        for i in range(31):                                                                            #spaeter laenge der liste der belegten faecher

            cb1 = QCheckBox()
            cb2 = QCheckBox()
            cb3 = QCheckBox()
            cb4 = QCheckBox()

            cb1.setChecked(True)
            cb2.setChecked(True)
            cb3.setChecked(True)
            cb4.setChecked(True)

            self.cb_col1.append(cb1)
            self.cb_col2.append(cb2)
            self.cb_col3.append(cb3)
            self.cb_col4.append(cb4)

            grid_layout.addWidget(cb1, row, 1, Qt.AlignmentFlag.AlignLeft)
            grid_layout.addWidget(cb2, row, 2, Qt.AlignmentFlag.AlignLeft)
            grid_layout.addWidget(cb3, row, 3, Qt.AlignmentFlag.AlignLeft)
            grid_layout.addWidget(cb4, row, 4, Qt.AlignmentFlag.AlignLeft)

            row += 1


        scroll_content.setLayout(grid_layout)
        scroll_area.setWidget(scroll_content)


        main_layout.addWidget(scroll_area)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        saveb = QPushButton('speichern')
        saveb.resize(saveb.sizeHint())
        saveb.clicked.connect(self.save)
        main_layout.addWidget(saveb)

        backb = QPushButton('Zurück')
        backb.resize(backb.sizeHint())
        backb.clicked.connect(self.back)
        main_layout.addWidget(backb)


        
    def save(self):
        save1 = []
        count_col = 1

        for i in  self.cb_col1:
            if i.isChecked() == False:
                save1.append([grid_layout.itemAtPosition(count_col, 0).widget().text(), '3'])
            count_col += 1

        count_col = 1

        for i in self.cb_col2:
            if i.isChecked() == False:
                save1.append([grid_layout.itemAtPosition(count_col, 0).widget().text(), '4'])
            count_col += 1

        count_col = 1

        for i in self.cb_col3:
            if i.isChecked() == False:
                save1.append([grid_layout.itemAtPosition(count_col, 0).widget().text(), '5'])
            count_col += 1

        count_col = 1 

        for i in self.cb_col4:
            if i.isChecked() == False:
                save1.append([grid_layout.itemAtPosition(count_col, 0).widget().text(), '6'])
            count_col += 1

        print(save1)

        for i in self.cb_col1:
            i.setChecked(True)

        for i in self.cb_col2:
            i.setChecked(True)

        for i in self.cb_col3:
            i.setChecked(True)

        for i in self.cb_col4:
            i.setChecked(True)


    def back(self):
        pipi = Launcher('homepage')
        pipi.launch()





#Anzeigen / Ausführen des Programms als sepeates Fenster
app = QtWidgets.QApplication(sys.argv)
win = Klammerung()
win.show()
sys.exit(app.exec())