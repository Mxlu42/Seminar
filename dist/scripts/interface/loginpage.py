import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit, QMessageBox, QComboBox, QVBoxLayout
from PyQt6.QtCore import QSize, Qt
from pymongo import MongoClient
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from heart import Launcher

helpi = False
client = MongoClient('localhost', 27017)
db = client['school']
collection = db['students']

class Window(QMainWindow):
    def __init__(self):
        global txts, txt1, txt2, txt3, grid
        super().__init__()

        # Mindestgröße / Titel definieren
        self.setCentralWidget(QWidget(self))
        self.setMinimumSize(QSize(500, 600))
        self.setMaximumSize(QSize(500, 600))
        self.setWindowTitle('Loginpage')

        lbl = QLabel('Platzhalter für den Erklärtext')
        lbl.resize(lbl.sizeHint())
        lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        lbl.setMargin(30)
        self.setCentralWidget(lbl)



        # Fenster im Fenster für das gridlayout erstellen und definieren

        wid = QWidget(self)
        grid = QGridLayout(wid)
        wid.setLayout(grid)
        wid.setMinimumSize(QSize(380, 200))
        wid.setMaximumSize(QSize(380, 200))
        wid.move(round((500/2)-(380/2)), 250)
        txts = []

        row = 0


        # gesamte Breschriftung der Zeilen 1 - 5
        for s in [ 'Name', 'Vorname', 'Passwort']:
            lbl = QLabel(s)
            lbl.resize(lbl.sizeHint())
            grid.addWidget(lbl, row, 1,  Qt.AlignmentFlag.AlignRight)
            row += 1

        # Textfelder in der 2/3 Zeile erstellen
        txt1 = QLineEdit()
        grid.addWidget(txt1, 0, 2)
        txts += [txt1]

        txt2 = QLineEdit()
        grid.addWidget(txt2, 1, 2)
        txts += [txt2]

        # Passwort Eingabefeld in Zeile 4
        txt3 = QLineEdit()
        txt3.setEchoMode(QLineEdit.EchoMode.Password)
        grid.addWidget(txt3, 2, 2)
        txts += [txt3]


        # Button zum Speichern der daten
        save = QPushButton('Speichern')
        save.clicked.connect(self.save)
        grid.addWidget(save, 4, 2, Qt.AlignmentFlag.AlignLeft)
        
        # Button zum anzeigen des Passworts beim gedrückt halten
        sp = QPushButton('Passwort zeigen')
        sp.pressed.connect(self.sp_p)
        sp.released.connect(self.sp_r)
        grid.addWidget(sp, 2, 3, Qt.AlignmentFlag.AlignRight)

        regwid = QWidget(self)
        regbox = QGridLayout(regwid)
        regwid.setLayout(regbox)
        regwid.setMinimumSize(QSize(145, 65))
        regwid.setMaximumSize(QSize(145, 65))
        regwid.move(350, 525)

        reglbl = QLabel('<u>Neuen Accout erstellen:</u>')
        reglbl.resize(reglbl.sizeHint())
        reglbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
        regbox.addWidget(reglbl)

        regb = QPushButton('Neuer Account')
        regb.resize(regb.sizeHint())
        regb.clicked.connect(self.directtoregisterpage)
        regbox.addWidget(regb)




    def directtoregisterpage(self):
        print('Weiterleiten zu: registerpage')
        lnh = Launcher('registerpage')
        lnh.launch()

    # Funktion des 'Speichern' Buttons mit Speicher benachrichtigung / Überprüfung auf Eingabefehler
    def save(self):   
        if txts[0].text().strip() == '':
            QMessageBox.about(self, 'Fehler', 'Bitte geben Sie Ihren Namen an!')
            return
        if txts[1].text().strip() == '':
            QMessageBox.about(self, 'Fehler', 'Bitte geben Sie Ihren Vornamen an!')
            return
        if txts[2].text().strip() == '':
            QMessageBox.about(self, 'Fehler', 'Bitte geben Sie ein Passwort ein!')
            return


        aus = []
        aus.append(txts[0].text())
        aus.append(txts[1].text())
        aus.append(txts[2].text())
        print(aus)

# Bringt die Daten aus dem array als object in die Datenbank

        
        txt1.clear()
        txt2.clear()
        txt3.clear()
        
        QMessageBox.about(self, 'Speicherbenachrichtigung', 'Deine Daten Wurden gespeichert!')
        pipi = Launcher('homepage')
        pipi.launch()

    # Funktion des 'Passwort anzeigen' Buttons
    def sp_p(self):
        txt3.setEchoMode(QLineEdit.EchoMode.Normal)

    def sp_r(self):
        txt3.setEchoMode(QLineEdit.EchoMode.Password)

def main():# Anzeigen / Ausführen des Programms als seperrates Fenster
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
