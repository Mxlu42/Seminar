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
        #self.true_faecher = db.getAlleBelegtenFaechern([6])
        self.true_faecher = ['platzhalterfach 1', 'platzhalterfach 2', 'platzhalterfach 3', 'platzhalterfach 4', 'platzhalterfach 5', 'platzhalterfach 6', 'platzhalternote 7', 'platzhalterfach 8', 'platzhalterfach 9', 'platzhalternote 10']
        self.true_faecher.append('Schnitt')
        self.true_faecher.append('Bestanden')
        self.test_Noten = ['platzhalternote 1', 'platzhalternote 2', 'platzhalternote 3', 'platzhalternote 4', 'platzhalternote 5', 'platzhalternote 6', 'platzhalternote 7', 'platzhalternote 8', 'platzhalternote 9', 'platzhalternote 10']
        self.test_Noten.append('platzhalter Schnitt')
        self.test_Noten.append('platzhalter bestanden')
        #profil = db.get_faecher_by_fachart('profil')
        #print(profil)
        

        print('hello', self.true_faecher)
        super().__init__()
        
        #Mindestgröße / Titel definieren
        self.setCentralWidget(QWidget(self))
        self.setMinimumSize(QSize(500, 600))
        self.setMaximumSize(QSize(500, 600))
        self.setWindowTitle('Ergebnisausgabe der Prüfungsfächer')

        main_widget = QWidget()
        main_layout = QVBoxLayout()

        lbl = QLabel('Dies ist Eine geordnete Übersicht aller belegten Fächer, und Noten der<br>Prüfungen. Außerdem eine information über den Notenschnitt und die Versätzung.')
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

        


        for i in self.true_faecher:
            lbl = QLabel(i)
            lbl.resize(lbl.sizeHint())
            grid_layout.addWidget(lbl, row, 0,  Qt.AlignmentFlag.AlignLeft)
            grid_layout.setRowMinimumHeight(row, 30)
            row += 1

        row = 1

        for i in self.test_Noten:
            lbl = QLabel(i)
            lbl.resize(lbl.sizeHint())
            grid_layout.addWidget(lbl, row, 1,  Qt.AlignmentFlag.AlignLeft)
            grid_layout.setRowMinimumHeight(row, 30)
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
        pass

    def back(self):
        pipi = Launcher('Ergebnisausgabe_uebergang_interface')
        pipi.launch()





#Anzeigen / Ausführen des Programms als sepeates Fenster
app = QtWidgets.QApplication(sys.argv)
win = Noteneingabe11()
win.show()
sys.exit(app.exec())