import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit, QMessageBox, QComboBox, QRadioButton, QScrollArea, QVBoxLayout, QCheckBox
from PyQt6.QtCore import QSize, Qt
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from heart import Launcher
from dbhelp import DBHelp

class Noteneingabe13_1(QMainWindow):
    def __init__(self):
        global mclass
        super().__init__()
        db = DBHelp()
        #self.true_faecher = db.getAlleBelegtenFaechern([7])
        self.true_faecher = ['Informatik', 'Deutsch  eAn', 'Mathe', 'Witrschaft', 'Seminarkurs profil']

        self.items = ['Bitte Note wählen', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
        
        
        #Mindestgröße / Titel definieren
        self.setCentralWidget(QWidget(self))
        self.setMinimumSize(QSize(500, 600))
        self.setMaximumSize(QSize(500, 600))
        self.setWindowTitle('Noteneingabe der Prüfungen')

        main_widget = QWidget()
        main_layout = QVBoxLayout()

        lbl = QLabel('Bitte geben Sie alle Ihre Noten für alle Fächer an. Wenn Sie fertig sind,<br>überprüfen Sie alles nochmal. <b>Vorsicht:</b> die Auswahlfelfer lassen sich mit dem<br>Mausrad bedienen, also immer rechts daneben Scrollen.<br>Wenn Sie fertig sind drücken Sie auf "Speichern".')
        lbl.resize(lbl.sizeHint())
        lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        lbl.setMargin(30)
        main_layout.addWidget(lbl)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        

        scroll_content = QWidget()
        grid_layout = QGridLayout()
        

        row = 1

        lbl_f = QLabel('<b>Fach</b>')
        lbl_f.resize(lbl_f.sizeHint())
        lbl_f.setMargin(0)
        grid_layout.addWidget(lbl_f, 0, 0,  Qt.AlignmentFlag.AlignLeft)

        lbl_n = QLabel('<b>Note</b>')
        lbl_n.resize(lbl_f.sizeHint())
        lbl_n.setMargin(0)
        grid_layout.addWidget(lbl_n, 0, 1,  Qt.AlignmentFlag.AlignLeft)


        

        for i in self.true_faecher:
            lbl = QLabel(i)
            lbl.resize(lbl.sizeHint())
            grid_layout.addWidget(lbl, row, 0,  Qt.AlignmentFlag.AlignLeft)
            grid_layout.setRowMinimumHeight(row, 30)
            row += 1


        self.cbb1 = QComboBox()
        self.cbb1.addItems(self.items)
        grid_layout.addWidget(self.cbb1, 1, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb2 = QComboBox()
        self.cbb2.addItems(self.items)
        grid_layout.addWidget(self.cbb2, 2, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb3 = QComboBox()
        self.cbb3.addItems(self.items)
        grid_layout.addWidget(self.cbb3, 3, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb4 = QComboBox()
        self.cbb4.addItems(self.items)
        grid_layout.addWidget(self.cbb4, 4, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb5 = QComboBox()
        self.cbb5.addItems(self.items)
        grid_layout.addWidget(self.cbb5, 5, 1,  Qt.AlignmentFlag.AlignLeft)
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
        if self.cbb1.currentText() == 'Bitte Note wählen':
            QMessageBox.about(self, 'Fehler', f'Bitte Wählen Sie Ihre {mclass[0]} Note')
            return
        if self.cbb2.currentText() == 'Bitte Note wählen':
            QMessageBox.about(self, 'Fehler', f'Bitte Wählen Sie Ihre {mclass[1]} Note')
            return
        if self.cbb3.currentText() == 'Bitte Note wählen':
            QMessageBox.about(self, 'Fehler', f'Bitte Wählen Sie Ihre {mclass[2]} Note')
            return
        if self.cbb4.currentText() == 'Bitte Note wählen':
            QMessageBox.about(self, 'Fehler', f'Bitte Wählen Sie Ihre {mclass[3]} Note')
            return
        if self.cbb5.currentText() == 'Bitte Note wählen':
            QMessageBox.about(self, 'Fehler', f'Bitte Wählen Sie Ihre {mclass[4]} Note')
            return
        
        
        savearr = [self.true_faecher, [self.cbb1.currentText(), self.cbb2.currentText(), self.cbb3.currentText(), self.cbb4.currentText(), self.cbb5.currentText()]]  
        print(savearr)


        self.cbb1.setCurrentIndex(0)
        self.cbb2.setCurrentIndex(0)
        self.cbb3.setCurrentIndex(0)
        self.cbb4.setCurrentIndex(0)
        self.cbb5.setCurrentIndex(0)
    
    def back(self):
        pipi = Launcher('Noteneingabe13_interface')
        pipi.launch()





#Anzeigen / Ausführen des Programms als sepeates Fenster
app = QtWidgets.QApplication(sys.argv)
win = Noteneingabe13_1()
win.show()
sys.exit(app.exec())