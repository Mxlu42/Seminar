import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox, QComboBox, QRadioButton
from PyQt6.QtCore import QSize, Qt
from PruefungsFaecherPossible import *
class Pruefungsfaecherwahl(QMainWindow):
    def __init__(self):
        self.pfc = PruefungsfaecherPossible()
        self.savearr = []
        super().__init__()
        #Mindestgröße / Titel definieren
        self.setCentralWidget(QWidget(self))
        self.setMinimumSize(QSize(500, 600))
        self.setMaximumSize(QSize(500, 600))
        self.setWindowTitle('Prüfungsfächerwahl')

        lble = QLabel('Platzhalter für den Erklärtext')
        lble.resize(lble.sizeHint())
        lble.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        lble.setMargin(30)
        self.setCentralWidget(lble)

        wid1 = QWidget(self)
        box1 = QVBoxLayout(wid1)
        wid1.setMinimumSize(QSize(170, 280))
        wid1.setMaximumSize(QSize(170, 280))
        wid1.move(171, 295)

        lbl1 = QLabel('1. Prüfungsfach')
        lbl1.resize(lbl1.sizeHint())
        box1.addWidget(lbl1)

        self.cbb1 = QComboBox(self)
        self.cbb1.addItem('Bitte wählen')
        self.cbb1.addItems(self.pfc.getPFP1())
        self.cbb1.resize(self.cbb1.sizeHint())
        box1.addWidget(self.cbb1)
        self.cbb1.currentIndexChanged.connect(self.update_cbb_1)

        lbl2 = QLabel('2. Prüfungsfach')
        lbl2.resize(lbl2.sizeHint())
        box1.addWidget(lbl2)
        
        self.cbb2 = QComboBox(self)
        self.cbb2.addItem('Bitte wählen')
        self.cbb2.addItems(self.pfc.getPFP2())
        self.cbb2.resize(self.cbb2.sizeHint())
        box1.addWidget(self.cbb2)
        self.cbb2.currentIndexChanged.connect(self.update_cbb_2)

        lbl3 = QLabel('3. Prüfungsfach')
        lbl3.resize(lbl3.sizeHint())
        box1.addWidget(lbl3)

        self.cbb3 = QComboBox(self)
        self.cbb3.addItem('Bitte wählen')
        self.cbb3.addItems(self.pfc.getPFP3())
        self.cbb3.resize(self.cbb3.sizeHint())
        box1.addWidget(self.cbb3)
        self.cbb3.currentIndexChanged.connect(self.update_cbb_3)

        lbl4 = QLabel('4. Prüfungsfach')
        lbl4.resize(lbl4.sizeHint())
        box1.addWidget(lbl4)

        self.cbb4 = QComboBox(self)
        self.cbb4.addItem('Bitte wählen')
        self.cbb4.addItems(self.pfc.getPFP4())
        self.cbb4.resize(self.cbb4.sizeHint())
        box1.addWidget(self.cbb4)
        self.cbb4.currentIndexChanged.connect(self.update_cbb_4)

        lbl5 = QLabel('5. Prüfungsfach')
        lbl5.resize(lbl5.sizeHint())
        box1.addWidget(lbl5)

        self.cbb5 = QComboBox(self)
        self.cbb5.addItem('Bitte wählen')
        self.cbb5.addItems(self.pfc.getPFP5())
        self.cbb5.resize(self.cbb5.sizeHint())
        box1.addWidget(self.cbb5)
        self.cbb5.currentIndexChanged.connect(self.update_cbb_5)

        saveb = QPushButton('Speichern')
        saveb.resize(saveb.sizeHint())
        saveb.clicked.connect(self.save)
        box1.addWidget(saveb)

        backwid = QWidget(self)
        backbox = QVBoxLayout(backwid)
        backwid.setMinimumSize(100, 50)
        backwid.setMaximumSize(100, 50)
        backwid.move(10, 540)

        backb = QPushButton('Zurück')
        backb.resize(backb.sizeHint())
        backb.clicked.connect(self.back)
        backbox.addWidget(backb)

    def update_cbb_1(self):
        self.cbb1.blockSignals(True)                                                            #Benötigt daten aus der db
        self.cbb1.blockSignals(False)

    def update_cbb_2(self):
        self.cbb2.blockSignals(True)
        self.cbb3.blockSignals(True)
        print("abhier")
        self.pfc.setPF2(self.cbb2.currentText())  
        new_items = self.pfc.getPFP3()
        print("new_items", new_items)
        self.cbb3.clear()
        self.cbb3.addItem("Bitte wählen")
        self.cbb3.addItems(new_items)
        self.cbb3.blockSignals(False)
        self.cbb2.blockSignals(False)

    def update_cbb_3(self):
        self.cbb3.blockSignals(True)
        self.cbb4.blockSignals(True)
        print("abhier")
        self.pfc.setPF3(self.cbb3.currentText())  
        new_items = self.pfc.getPFP4()
        print("new_items", new_items)
        self.cbb4.clear()
        self.cbb4.addItem("Bitte wählen")
        self.cbb4.addItems(new_items)
        self.cbb4.blockSignals(False)
        self.cbb3.blockSignals(False)

    def update_cbb_4(self):
        self.cbb4.blockSignals(True)
        self.cbb5.blockSignals(True)
        self.pfc.setPF4(self.cbb4.currentText())  
        new_items = self.pfc.getPFP5()
        self.cbb5.clear()
        self.cbb5.addItem("Bitte wählen")
        self.cbb5.addItems(new_items)
        self.cbb5.blockSignals(False)
        self.cbb4.blockSignals(False)

    def update_cbb_5(self):
        pass

    def save(self):
        if self.cbb1.currentText() == 'Bitte wählen':
            QMessageBox.about(self, 'Fehler', 'Bitte Wählen Sie Ihr erstes Prüfungsfach')
            return
        if self.cbb2.currentText() == 'Bitte wählen':
            QMessageBox.about(self, 'Fehler', 'Bitte Wählen Sie Ihr zweites Prüfungsfach')
            return
        if self.cbb3.currentText() == 'Bitte wählen':
            QMessageBox.about(self, 'Fehler', 'Bitte Wählen Sie Ihr drittes Prüfungsfach')
            return
        if self.cbb4.currentText() == 'Bitte wählen':
            QMessageBox.about(self, 'Fehler', 'Bitte Wählen Sie Ihr viertes Prüfungsfach')
            return
        if self.cbb5.currentText() == 'Bitte wählen': 
            QMessageBox.about(self, 'Fehler', 'Bitte Wählen Sie Ihr fünftes Prüfungsfach')
            return
        else:
            self.savearr.append(self.cbb1.currentText())
            self.savearr.append(self.cbb2.currentText())
            self.savearr.append(self.cbb3.currentText())
            self.savearr.append(self.cbb4.currentText())
            self.savearr.append(self.cbb5.currentText())
            
            print(self.savearr)

            self.cbb1.setCurrentIndex(0)
            self.cbb2.setCurrentIndex(0)
            self.cbb3.setCurrentIndex(0)
            self.cbb4.setCurrentIndex(0)
            self.cbb5.setCurrentIndex(0)

            QMessageBox.about(self, 'Speicherbenachrichtigung', 'Ihre Eingabe wurde gespeichert!')

    def back(self):
        print('man kommt dann halt zurück auf die homepage')






app = QtWidgets.QApplication(sys.argv)
win = Pruefungsfaecherwahl()
win.show()
sys.exit(app.exec())