import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit, QMessageBox, QComboBox, QRadioButton, QScrollArea, QVBoxLayout, QCheckBox
from PyQt6.QtCore import QSize, Qt
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from heart import Launcher
#from dbhelp import DBHelp

class Noteneingabe12(QMainWindow):
    def __init__(self):
        global mclass
        mclass = ['Mathe', 'Deutsch', 'Profielfach (DB)', 'GGK', 'Englisch', 'Sport', 'Naturwissenschaft (DB)', 'Informatik', 'Religion (DB)', 'Mathe plus (DB)', 'Fremdsprache (DB)', 'Wirtaschaft (DB)','Labor (DB)', 'LT (DB)', 'Seminar (DB)']
        #db = DBHelp()
        #print(db.getArrayAusAllenFaechernAndFaechertypseAndGesamtnoteInBestimmtemHalbJahr(0))
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

        


        for i in mclass:
            lbl = QLabel(i)
            lbl.resize(lbl.sizeHint())
            grid_layout.addWidget(lbl, row, 0,  Qt.AlignmentFlag.AlignLeft)
            grid_layout.setRowMinimumHeight(row, 30)
            row += 1

        row = 1
        column = 1

        self.cbb1 = QComboBox()
        self.cbb1.addItem('Bitte Note wählen')
        self.cbb1.addItem('1')
        self.cbb1.addItem('2')
        self.cbb1.addItem('3')
        self.cbb1.addItem('4')
        self.cbb1.addItem('5')
        self.cbb1.addItem('6')
        grid_layout.addWidget(self.cbb1, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb2 = QComboBox()
        self.cbb2.addItem('Bitte Note wählen')
        self.cbb2.addItem('1')
        self.cbb2.addItem('2')
        self.cbb2.addItem('3')
        self.cbb2.addItem('4')
        self.cbb2.addItem('5')
        self.cbb2.addItem('6')
        grid_layout.addWidget(self.cbb2, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb3 = QComboBox()
        self.cbb3.addItem('Bitte Note wählen')
        self.cbb3.addItem('1')
        self.cbb3.addItem('2')
        self.cbb3.addItem('3')
        self.cbb3.addItem('4')
        self.cbb3.addItem('5')
        self.cbb3.addItem('6')
        grid_layout.addWidget(self.cbb3, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb4 = QComboBox()
        self.cbb4.addItem('Bitte Note wählen')
        self.cbb4.addItem('1')
        self.cbb4.addItem('2')
        self.cbb4.addItem('3')
        self.cbb4.addItem('4')
        self.cbb4.addItem('5')
        self.cbb4.addItem('6')
        grid_layout.addWidget(self.cbb4, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb5 = QComboBox()
        self.cbb5.addItem('Bitte Note wählen')
        self.cbb5.addItem('1')
        self.cbb5.addItem('2')
        self.cbb5.addItem('3')
        self.cbb5.addItem('4')
        self.cbb5.addItem('5')
        self.cbb5.addItem('6')
        grid_layout.addWidget(self.cbb5, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb6 = QComboBox()
        self.cbb6.addItem('Bitte Note wählen')
        self.cbb6.addItem('1')
        self.cbb6.addItem('2')
        self.cbb6.addItem('3')
        self.cbb6.addItem('4')
        self.cbb6.addItem('5')
        self.cbb6.addItem('6')
        grid_layout.addWidget(self.cbb6, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb7 = QComboBox()
        self.cbb7.addItem('Bitte Note wählen')
        self.cbb7.addItem('1')
        self.cbb7.addItem('2')
        self.cbb7.addItem('3')
        self.cbb7.addItem('4')
        self.cbb7.addItem('5')
        self.cbb7.addItem('6')
        grid_layout.addWidget(self.cbb7, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb8 = QComboBox()
        self.cbb8.addItem('Bitte Note wählen')
        self.cbb8.addItem('1')
        self.cbb8.addItem('2')
        self.cbb8.addItem('3')
        self.cbb8.addItem('4')
        self.cbb8.addItem('5')
        self.cbb8.addItem('6')
        grid_layout.addWidget(self.cbb8, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb9 = QComboBox()
        self.cbb9.addItem('Bitte Note wählen')
        self.cbb9.addItem('1')
        self.cbb9.addItem('2')
        self.cbb9.addItem('3')
        self.cbb9.addItem('4')
        self.cbb9.addItem('5')
        self.cbb9.addItem('6')
        grid_layout.addWidget(self.cbb9, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb10 = QComboBox()
        self.cbb10.addItem('Bitte Note wählen')
        self.cbb10.addItem('1')
        self.cbb10.addItem('2')
        self.cbb10.addItem('3')
        self.cbb10.addItem('4')
        self.cbb10.addItem('5')
        self.cbb10.addItem('6')
        grid_layout.addWidget(self.cbb10, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb11 = QComboBox()
        self.cbb11.addItem('Bitte Note wählen')
        self.cbb11.addItem('1')
        self.cbb11.addItem('2')
        self.cbb11.addItem('3')
        self.cbb11.addItem('4')
        self.cbb11.addItem('5')
        self.cbb11.addItem('6')
        grid_layout.addWidget(self.cbb11, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb12 = QComboBox()
        self.cbb12.addItem('Bitte Note wählen')
        self.cbb12.addItem('1')
        self.cbb12.addItem('2')
        self.cbb12.addItem('3')
        self.cbb12.addItem('4')
        self.cbb12.addItem('5')
        self.cbb12.addItem('6')
        grid_layout.addWidget(self.cbb12, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb13 = QComboBox()
        self.cbb13.addItem('Bitte Note wählen')
        self.cbb13.addItem('1')
        self.cbb13.addItem('2')
        self.cbb13.addItem('3')
        self.cbb13.addItem('4')
        self.cbb13.addItem('5')
        self.cbb13.addItem('6')
        grid_layout.addWidget(self.cbb13, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb14 = QComboBox()
        self.cbb14.addItem('Bitte Note wählen')
        self.cbb14.addItem('1')
        self.cbb14.addItem('2')
        self.cbb14.addItem('3')
        self.cbb14.addItem('4')
        self.cbb14.addItem('5')
        self.cbb14.addItem('6')
        grid_layout.addWidget(self.cbb14, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb15 = QComboBox()
        self.cbb15.addItem('Bitte Note wählen')
        self.cbb15.addItem('1')
        self.cbb15.addItem('2')
        self.cbb15.addItem('3')
        self.cbb15.addItem('4')
        self.cbb15.addItem('5')
        self.cbb15.addItem('6')
        grid_layout.addWidget(self.cbb15, row, 1,  Qt.AlignmentFlag.AlignLeft)
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
        if self.cbb6.currentText() == 'Bitte Note wählen':
            QMessageBox.about(self, 'Fehler', f'Bitte Wählen Sie Ihre {mclass[5]} Note')
            return
        if self.cbb7.currentText() == 'Bitte Note wählen':
            QMessageBox.about(self, 'Fehler', f'Bitte Wählen Sie Ihre {mclass[6]} Note')
            return
        if self.cbb8.currentText() == 'Bitte Note wählen':
            QMessageBox.about(self, 'Fehler', f'Bitte Wählen Sie Ihre {mclass[7]} Note')
            return
        if self.cbb9.currentText() == 'Bitte Note wählen':
            QMessageBox.about(self, 'Fehler', f'Bitte Wählen Sie Ihre {mclass[8]} Note')
            return
        if self.cbb10.currentText() == 'Bitte Note wählen':
            QMessageBox.about(self, 'Fehler', f'Bitte Wählen Sie Ihre {mclass[9]} Note')
            return
        if self.cbb11.currentText() == 'Bitte Note wählen':
            QMessageBox.about(self, 'Fehler', f'Bitte Wählen Sie Ihre {mclass[10]} Note')
            return
        if self.cbb12.currentText() == 'Bitte Note wählen':
            QMessageBox.about(self, 'Fehler', f'Bitte Wählen Sie Ihre {mclass[11]} Note')
            return
        if self.cbb13.currentText() == 'Bitte Note wählen':
            QMessageBox.about(self, 'Fehler', f'Bitte Wählen Sie Ihre {mclass[12]} Note')
            return
        if self.cbb14.currentText() == 'Bitte Note wählen':
            QMessageBox.about(self, 'Fehler', f'Bitte Wählen Sie Ihre {mclass[13]} Note')
            return
        if self.cbb15.currentText() == 'Bitte Note wählen':
            QMessageBox.about(self, 'Fehler', f'Bitte Wählen Sie Ihre {mclass[14]} Note')
            return
        
        
        savearr = [mclass, [self.cbb1.currentText(), self.cbb2.currentText(), self.cbb3.currentText(), self.cbb4.currentText(), self.cbb5.currentText(), self.cbb6.currentText(), self.cbb7.currentText(), self.cbb8.currentText(), self.cbb9.currentText(), self.cbb10.currentText(), self.cbb11.currentText(), self.cbb12.currentText(), self.cbb13.currentText(), self.cbb14.currentText(), self.cbb15.currentText()]]  
        print(savearr)

        self.cbb1.setCurrentIndex(0)
        self.cbb2.setCurrentIndex(0)
        self.cbb3.setCurrentIndex(0)
        self.cbb4.setCurrentIndex(0)
        self.cbb5.setCurrentIndex(0)
        self.cbb6.setCurrentIndex(0)
        self.cbb7.setCurrentIndex(0)
        self.cbb8.setCurrentIndex(0)
        self.cbb9.setCurrentIndex(0)
        self.cbb10.setCurrentIndex(0)
        self.cbb11.setCurrentIndex(0)
        self.cbb12.setCurrentIndex(0)
        self.cbb13.setCurrentIndex(0)
        self.cbb14.setCurrentIndex(0)
        self.cbb15.setCurrentIndex(0)

    def back(self):
        pipi = Launcher('homepage')
        pipi.launch()





#Anzeigen / Ausführen des Programms als sepeates Fenster
app = QtWidgets.QApplication(sys.argv)
win = Noteneingabe12()
win.show()
sys.exit(app.exec())