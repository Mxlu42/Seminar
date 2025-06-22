import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit, QMessageBox, QComboBox
from PyQt6.QtCore import QSize, Qt
from pymongo import MongoClient
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from heart import Launcher
from init_db import CreateData
from dbhelp import *

client = MongoClient('localhost', 27017)
db = client['test']
collection = db['students']

class Registerpage(QMainWindow):
    def __init__(self):
        global txts, txt1, txt2, txt3, txt4, cbb, grid
        super().__init__()

        # Mindestgröße / Titel definieren
        self.setCentralWidget(QWidget(self))
        self.setMinimumSize(QSize(500, 600))
        self.setMaximumSize(QSize(500, 600))
        self.setWindowTitle('Registerpage')

        lbl = QLabel('Willkommen Bei unserem Programm! Um zu Beginnen bitte wählen Sie Ihr<br>Profilfach aus, geben Sie Ihren Namen an und Erstellen<br>Sie ein sicheres Passwort. Teilen sie dieses paswort <b>Niemals</b>.<br>Viel Spaß bei der nutzung wünschen Felix B. Miron H. und Noah L.')
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

        # Dropdownmenu erstellen und im grid plazieren
        cbb = QComboBox(self)
        cbb.addItems(['Profilfach wählen', 'Informationstechnik', 'Gestaltung_Medien', 'Mechatronik'])
        cbb.resize(cbb.sizeHint())
        grid.addWidget(cbb, row, 2, Qt.AlignmentFlag.AlignLeft)
        txts.append(cbb)

        # gesamte Breschriftung der Zeilen 1 - 5
        for s in ['Profilfach', 'Name', 'Vorname', 'Passwort', 'Passwort wiederholen']:
            lbl = QLabel(s)
            lbl.resize(lbl.sizeHint())
            grid.addWidget(lbl, row, 1,  Qt.AlignmentFlag.AlignRight)
            row += 1

        # Textfelder in der 2/3 Zeile erstellen
        txt1 = QLineEdit()
        grid.addWidget(txt1, 1, 2)
        txts += [txt1]

        txt2 = QLineEdit()
        grid.addWidget(txt2, 2, 2)
        txts += [txt2]

        # Passwort Eingabefeld in Zeile 4
        txt3 = QLineEdit()
        txt3.setEchoMode(QLineEdit.EchoMode.Password)
        grid.addWidget(txt3, 3, 2)
        txts += [txt3]

        # Passwort wiederholung Feld in Zeile 5
        txt4 = QLineEdit()
        txt4.setEchoMode(QLineEdit.EchoMode.Password)
        grid.addWidget(txt4, 4, 2)
        txts += [txt4]


        # Button zum Speichern der daten
        save = QPushButton('Speichern')
        save.clicked.connect(self.save)
        grid.addWidget(save, 5, 2, Qt.AlignmentFlag.AlignLeft)
        
        # Button zum anzeigen des Passworts beim gedrückt halten
        sp = QPushButton('Passwort zeigen')
        sp.pressed.connect(self.sp_p)
        sp.released.connect(self.sp_r)
        grid.addWidget(sp, 3, 3, Qt.AlignmentFlag.AlignRight)

        logwid = QWidget(self)
        logbox = QGridLayout(logwid)
        logwid.setLayout(logbox)
        logwid.setMinimumSize(QSize(145, 65))
        logwid.setMaximumSize(QSize(145, 65))
        logwid.move(350, 525)

        loglbl = QLabel('<u>bestehender Account:</u>')
        loglbl.resize(loglbl.sizeHint())
        loglbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
        logbox.addWidget(loglbl)

        logb = QPushButton('Anmelden')
        logb.resize(logb.sizeHint())
        logb.clicked.connect(self.directtologinpage)
        logbox.addWidget(logb)

    def directtologinpage(self):
        pass

    # Funktion des 'Speichern' Buttons mit Speicher benachrichtigung / Überprüfung auf Eingabefehler
    def save(self):
        # Validierung wie gehabt …
        if txts[0].currentText() == 'Profilfach wählen':
            QMessageBox.about(self, 'Fehler', 'Bitte wählen Sie ein Profilfach!')
            return
        # … weitere Validierungen …

        # Daten für neu-en Account zusammenbauen
        profilfach = txts[0].currentText()
        name       = txts[1].text().strip()
        vorname    = txts[2].text().strip()
        password   = txts[3].text()
        creds      = [profilfach, name, vorname, password]

        # Account anlegen, falls noch nicht vorhanden
        if collection.find_one({"name": name, "password": password}):
            QMessageBox.about(self, 'Hinweis', 'Dieser Account existiert bereits.')
        else:
            # DB initial befüllen
            txt_data = CreateData()
            replaced = txt_data.replace_data(name, vorname, password)
            txt_data.creationdb(replaced)
            QMessageBox.about(self, 'Erfolg', 'Account wurde angelegt!')

        # Jetzt direkt einloggen und ID speichern
        db = DBHelp()
        if db.login(name, vorname, password):
            # Erst nach erfolgreichem login die Fächer setzen
            db.setzeMehrereFaecherBelegtTrue([profilfach], [1,2,3,4,5,6])
            db.setFachart_by_Fach_and_year(profilfach, [1, 2, 3, 4, 5, 6], 'profil')
            QMessageBox.about(self, 'Login', 'Weiterleitung zum Programm.')
            Launcher('homepage').launch()
        else:
            QMessageBox.critical(self, 'Fehler', 'Login nach Registrierung fehlgeschlagen!')

        # Felder zurücksetzen
        cbb.setCurrentIndex(0)
        txt1.clear(); txt2.clear(); txt3.clear(); txt4.clear()

    # Funktion des 'Passwort anzeigen' Buttons
    def sp_p(self):
        txt3.setEchoMode(QLineEdit.EchoMode.Normal)

    def sp_r(self):
        txt3.setEchoMode(QLineEdit.EchoMode.Password)

def main():# Anzeigen / Ausführen des Programms als seperrates Fenster
    app = QtWidgets.QApplication(sys.argv)
    win = Registerpage()
    win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
