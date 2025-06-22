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
        self.true_faecher = db.getAlleBelegtenFaechern([6])
        print(self.true_faecher)
        profil = db.get_faecher_by_fachart('profil')
        self.ean = db.get_faecher_by_fachart('eAn')[0]
        self.gan = db.get_faecher_by_fachart('gAn')[0]
        self.naturwissenschaft = 'Nein'
        self.matheplus = 'Nein'
        self.englisch = 'Nein'
        self.spanisch = 'Nein'
        self.wirtschaft = 'Nein'
        self.religion = 'Nein'
        self.lt = 'Nein'
        for i in self.true_faecher:
            if i == 'Physik' or i == 'Chemie':
                self.naturwissenschaft = i

            if i == 'Ethik' or i == 'Evangelisch' or i == 'Katholisch':
                self.religion = i

            if i == 'MathePlus':
                self.matheplus = 'Mathe Plus'

            if i == 'Englisch':
                self.englisch = 'Englisch'

            elif i == 'SpanischN':
                self.spanisch = 'Spanisch'

            if i == 'Wirtschaft':
                self.wirtschaft = i

            if i == 'Literatur_Theater':
                self.lt = 'Literatur und Theater'

            
        mclass = [f'{self.ean} eAn', f'{self.gan} gAn', 'Profilfach', 'GGK', 'Englisch', 'Sport', self.naturwissenschaft, 'Informatik', self.religion, self.matheplus, self.spanisch, self.englisch, self.wirtschaft, f'{self.naturwissenschaft} Labor', self.lt]
        self.items = ['Bitte Note wählen', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
        
        if self.matheplus == 'Nein':
            mclass.remove(self.matheplus)
        if self.englisch == 'Nein':
            mclass.remove(self.englisch)
        if self.spanisch == 'Nein':
            mclass.remove(self.spanisch)
        if self.wirtschaft == 'Nein':
            mclass.remove(self.wirtschaft)
        if self.lt == 'Nein':
            mclass.remove(self.lt)
        if self.religion == 'Nein':
            mclass.remove(self.religion)
        

        
        self.l = len(mclass)
        
        #Mindestgröße / Titel definieren
        self.setCentralWidget(QWidget(self))
        self.setMinimumSize(QSize(500, 600))
        self.setMaximumSize(QSize(500, 600))
        self.setWindowTitle('Noteneingabe der Klasse 13/2')

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
        self.cbb1.addItems(self.items)
        grid_layout.addWidget(self.cbb1, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb2 = QComboBox()
        self.cbb2.addItems(self.items)
        grid_layout.addWidget(self.cbb2, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb3 = QComboBox()
        self.cbb3.addItems(self.items)
        grid_layout.addWidget(self.cbb3, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb4 = QComboBox()
        self.cbb4.addItems(self.items)
        grid_layout.addWidget(self.cbb4, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb5 = QComboBox()
        self.cbb5.addItems(self.items)
        grid_layout.addWidget(self.cbb5, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb6 = QComboBox()
        self.cbb6.addItems(self.items)
        grid_layout.addWidget(self.cbb6, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb7 = QComboBox()
        self.cbb7.addItems(self.items)
        grid_layout.addWidget(self.cbb7, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb8 = QComboBox()
        self.cbb8.addItems(self.items)
        grid_layout.addWidget(self.cbb8, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb9 = QComboBox()
        self.cbb9.addItems(self.items)
        grid_layout.addWidget(self.cbb9, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb10 = QComboBox()
        self.cbb10.addItems(self.items)
        grid_layout.addWidget(self.cbb10, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb11 = QComboBox()
        self.cbb11.addItems(self.items)
        if self.l < 11:
            pass
        else:
            grid_layout.addWidget(self.cbb11, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb12 = QComboBox()
        self.cbb12.addItems(self.items)
        if self.l < 12:
            pass
        else:
            grid_layout.addWidget(self.cbb12, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb13 = QComboBox()
        self.cbb13.addItems(self.items)
        if self.l < 13:
            pass
        else:
            grid_layout.addWidget(self.cbb13, row, 1,  Qt.AlignmentFlag.AlignLeft)
        row += 1

        self.cbb14 = QComboBox()
        self.cbb14.addItems(self.items)
        if self.l < 14:
            pass
        else:
            grid_layout.addWidget(self.cbb14, row, 1,  Qt.AlignmentFlag.AlignLeft)
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
        if self.l >= 11:
            if self.cbb11.currentText() == 'Bitte Note wählen':
                QMessageBox.about(self, 'Fehler', f'Bitte Wählen Sie Ihre {mclass[10]} Note')
                return
        if self.l >= 12:    
            if self.cbb12.currentText() == 'Bitte Note wählen':
                QMessageBox.about(self, 'Fehler', f'Bitte Wählen Sie Ihre {mclass[11]} Note')
                return
        if self.l >= 13:    
            if self.cbb13.currentText() == 'Bitte Note wählen':
                QMessageBox.about(self, 'Fehler', f'Bitte Wählen Sie Ihre {mclass[12]} Note')
                return
        if self.l >= 14:    
            if self.cbb14.currentText() == 'Bitte Note wählen':
                QMessageBox.about(self, 'Fehler', f'Bitte Wählen Sie Ihre {mclass[13]} Note')
                return
        
        
        savearr = [mclass, [self.cbb1.currentText(), self.cbb2.currentText(), self.cbb3.currentText(), self.cbb4.currentText(), self.cbb5.currentText(), self.cbb6.currentText(), self.cbb7.currentText(), self.cbb8.currentText(), self.cbb9.currentText(), self.cbb10.currentText(), self.cbb11.currentText(), self.cbb12.currentText(), self.cbb13.currentText(), self.cbb14.currentText()]]  
        print(savearr)

        if self.l > 13:
            savearr[1].pop()
        elif self.l > 12:
            savearr[1].pop()
            savearr[1].pop()
        elif self.l > 11:
            savearr[1].pop()
            savearr[1].pop()
            savearr[1].pop()
        elif self.l > 10:
            savearr[1].pop()
            savearr[1].pop()
            savearr[1].pop()
            savearr[1].pop()

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

    def back(self):
        pipi = Launcher('homepage')
        pipi.launch()





#Anzeigen / Ausführen des Programms als sepeates Fenster
app = QtWidgets.QApplication(sys.argv)
win = Noteneingabe13_1()
win.show()
sys.exit(app.exec())