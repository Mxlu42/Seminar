import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit, QMessageBox, QComboBox
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
        global txts, txt1, txt2, txt3, txt4, cbb, grid
        super().__init__()

        # Mindestgröße / Titel definieren
        self.setCentralWidget(QWidget(self))
        self.setMinimumSize(QSize(500, 600))
        self.setMaximumSize(QSize(500, 600))
        self.setWindowTitle('Regestrierungsformular')

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
        wid.move(round((500/2)-(380/2)), 350)
        txts = []

        row = 0

        # Dropdownmenu erstellen und im grid plazieren
        cbb = QComboBox(self)
        cbb.addItems(['Profilfach wählen', 'Informatik', 'Gestaltung- und Medientechnik', 'Mechatronik'])
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


        # WIP Button zum schliesen des Programms
        cancel = QPushButton('Beenden')
        cancel.clicked.connect(self.cancel)
        cancel.resize(cancel.sizeHint())
        cancel.move(300, 300)

        # Button zum Speichern der daten
        save = QPushButton('Speichern')
        save.clicked.connect(self.save)
        grid.addWidget(save, 5, 2, Qt.AlignmentFlag.AlignLeft)
        
        # Button zum anzeigen des Passworts beim gedrückt halten
        sp = QPushButton('Passwort zeigen')
        sp.pressed.connect(self.sp_p)
        sp.released.connect(self.sp_r)
        grid.addWidget(sp, 3, 3, Qt.AlignmentFlag.AlignRight)


    # Funktion des 'Speichern' Buttons mit Speicher benachrichtigung / Überprüfung auf Eingabefehler
    def save(self):   
        if txts[0].currentText() == 'Profilfach wählen':
            QMessageBox.about(self, 'Fehler', 'Bitte wählen Sie ein Profilfach!')
            return
        if txts[1].text().strip() == '':
            QMessageBox.about(self, 'Fehler', 'Bitte geben Sie Ihren Namen an!')
            return
        if txts[2].text().strip() == '':
            QMessageBox.about(self, 'Fehler', 'Bitte geben Sie Ihren Vornamen an!')
            return
        if txts[3].text().strip() == '':
            QMessageBox.about(self, 'Fehler', 'Bitte geben Sie ein Passwort ein! (mindestens 8 Zeichen)')
            return
        if txts[4].text().strip() == '':
            QMessageBox.about(self, 'Fehler', 'Bitte geben Sie Ihr Passwort erneut ein!')
            return
        if len(txts[3].text()) < 8:
            QMessageBox.about(self, 'Fehler', 'Das Passwort ist zu kurz! (mindestens 8 Zeichen)')
            return
        if txts[3].text() != txts[4].text():
            QMessageBox.about(self, 'Fehler', 'Die Passwörter stimmen nicht überein!')
            return


        aus = []
        aus.append(txts[0].currentText())
        aus.append(txts[1].text())
        aus.append(txts[2].text())
        aus.append(txts[3].text())
        print(aus)

# Bringt die Daten aus dem array als object in die Datenbank

        data = {'name': aus[1], 'vorname': aus[2], 'profilfach': aus[0], 'password': aus[3]}

        if collection.find_one({"name": data["name"], "password": data["password"]}):
            print("You already have an account.")
        else:
            collection.insert_one(data)

        for document in collection.find():
            print(document)
        
        cbb.setCurrentIndex(0)
        txt1.clear()
        txt2.clear()
        txt3.clear()
        txt4.clear()
        
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
