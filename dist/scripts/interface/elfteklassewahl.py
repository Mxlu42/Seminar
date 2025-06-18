import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox, QComboBox, QRadioButton
from PyQt6.QtCore import QSize, Qt
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pymongo import MongoClient
from heart import Launcher
from dbhelp import *

class SubjectChoice11(QMainWindow):
    def __init__(self):
        global r_cp, r_cl, r_pl, r_dsms, r_ds, r_ms, r_sgsef, r_sg, r_se, r_f, r_erkre, r_er, r_kr, r_e
        r_cp = []
        r_dsms = []
        r_sgsef = []
        r_erkre = []
        super().__init__()
        
        #Mindestgröße / Titel definieren
        self.setCentralWidget(QWidget(self))
        self.setMinimumSize(QSize(500, 600))
        self.setMaximumSize(QSize(500, 600))
        self.setWindowTitle('11te klasse Fächerwahl')

        lbl = QLabel('Hier werden Sie vier Verscshiedene Wahlen treffen.<br>Erstens: die Wahl Zwischen Chemie- und Physik Labor. Labor ist ein Fach in dem<br>man praktische Übungen zusätzlich zum Theorieunterricht durchführt. Sie<br>müssen jedoch immernoch beide Theorieuntterrichte Besuchen.<br>Zweitens: die Wahl zwischen Deutsch- und Mathe Stütz. Hierbei dreht es sich um<br>eine Schulstunde in der Woche bei der für das gewählte Fach Themen nochmal<br>intensiv wiederholt werden.<br>Drittens: die Wahl der Dritten Fremdsprache. Wenn Sie bereits eine Fremdsprache<br>für mindestens vier Jahre belegt haben, dann ist Spanisch gAn für Sie Freiwillig<br>(ansonsten wählen Sie "Bereits belegt"). Wenn Sie Spanisch vor der elften Klasse<br>bereits für einen Teil der Zeit belegt haben, wählen Sie Spanisch eAn. Wenn keines<br>dieser beiden Szenarien für Sie zutreffend sind, sind sie dazu <b>Verpflichtet</b><br>Spanisch gAn zu wählen.<br>Viertens: die Wahl der Glaubenslehre. Hier ist es wichtig anzumerken dass es nur<br>möglich ist dieses Fach in der Abiturprüfung zu wählen, wenn man es drei Jahre in<br>Folge belegt hat (also 11, 12, 13).<br>Wenn Sie Ihre Wahl getrofen, und überprüft haben, drücken<br>Sie einfach auf "sperichern".')
        lbl.resize(lbl.sizeHint())
        lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        lbl.setMargin(30)
        self.setCentralWidget(lbl)

        wid1 = QWidget(self)
        grid1 = QVBoxLayout(wid1)
        wid1.setLayout(grid1)
        wid1.setMinimumSize(QSize(155, 62))
        wid1.setMaximumSize(QSize(155, 62))
        wid1.move(100, 342)

        r_cl = QRadioButton('Chemie-L')
        r_cl.toggled.connect(self.r_clt)

        r_pl = QRadioButton('Physik-L')
        r_pl.toggled.connect(self.r_plt)

        grid1.addWidget(r_cl)
        grid1.addWidget(r_pl)


        wid2 = QWidget(self)
        grid2 = QVBoxLayout(wid2)
        wid2.setLayout(grid2)
        wid2.setMinimumSize(QSize(155, 62))
        wid2.setMaximumSize(QSize(155, 62))
        wid2.move(300, 342)

        r_ds = QRadioButton('Deutsch Stütz')
        r_ds.toggled.connect(self.r_dst)

        r_ms = QRadioButton('Mathe Stütz')
        r_ms.toggled.connect(self.r_mst)

        grid2.addWidget(r_ds)
        grid2.addWidget(r_ms)


        wid3 = QWidget(self)
        grid3 = QVBoxLayout(wid3)
        wid3.setLayout(grid3)
        wid3.setMinimumSize(QSize(205, 85))
        wid3.setMaximumSize(QSize(205, 85))
        wid3.move(100, 402)

        r_sg = QRadioButton('SpanischN')
        r_sg.toggled.connect(self.r_sgt)

        r_se = QRadioButton('SpanischF')
        r_se.toggled.connect(self.r_set)

        r_f = QRadioButton('3. Fremdsprache bereits belegt')
        r_f.toggled.connect(self.r_ft)

        grid3.addWidget(r_sg)
        grid3.addWidget(r_se)
        grid3.addWidget(r_f)


        wid4 = QWidget(self)
        grid4 = QVBoxLayout(wid4)
        wid4.setLayout(grid3)
        wid4.setMinimumSize(QSize(205, 85))
        wid4.setMaximumSize(QSize(205, 85))
        wid4.move(300, 402)

        r_er = QRadioButton('evangelische Religion')
        r_er.toggled.connect(self.r_ert)

        r_kr = QRadioButton('katholische Religion')
        r_kr.toggled.connect(self.r_krt)

        r_e = QRadioButton('Ethik')
        r_e.toggled.connect(self.r_et)

        grid4.addWidget(r_er)
        grid4.addWidget(r_kr)
        grid4.addWidget(r_e)

        backwid = QWidget(self)
        backbox = QVBoxLayout(backwid)
        backwid.setMinimumSize(100, 50)
        backwid.setMaximumSize(100, 50)
        backwid.move(10, 540)

        backb = QPushButton('Zurück')
        backb.resize(backb.sizeHint())
        backb.clicked.connect(self.back)
        backbox.addWidget(backb)

        savewid = QWidget(self)
        savebox  = QVBoxLayout(savewid)
        savewid.setMinimumSize(100, 50)
        savewid.setMaximumSize(100, 50)
        savewid.move(200, 540)

        saveb = QPushButton('Speichern')
        saveb.resize(saveb.sizeHint())
        saveb.clicked.connect(self.save)
        savebox.addWidget(saveb)




    def r_clt(self):
        if r_cl.isChecked() == True:
            r_cp.clear()
            r_cp.append('Chemie-L')
        else:
            return
        
    def r_plt(self):
        if r_pl.isChecked() == True:
            r_cp.clear()
            r_cp.append('Physik-L')
        else:
            return
        
    def r_dst(self):
        if r_ds.isChecked() == True:
            r_dsms.clear()
            r_dsms.append('DeutschStuetz')
        else:
            return
        
    def r_mst(self):
        if r_ms.isChecked() == True:
            r_dsms.clear()
            r_dsms.append('MatheStuetz')
        else:
            return
    
    def r_sgt(self):
        if r_sg.isChecked() == True:
            r_sgsef.clear()
            r_sgsef.append('SpanischN')
        else:
            return
    
    def r_set(self):
        if r_se.isChecked() == True:
            r_sgsef.clear()
            r_sgsef.append('SpanischF')
        else:
            return
        
    def r_ft(self):
        if r_f.isChecked() == True:
            r_sgsef.clear()
            r_sgsef.append('3. Fremdsprache bereits belegt')
        else:
            return
        
    def r_ert(self):
        if r_er.isChecked() == True:
            r_erkre.clear()
            r_erkre.append('Evangelisch')
        else:
            return
        
    def r_krt(self):
        if r_kr.isChecked() == True:
            r_erkre.clear()
            r_erkre.append('Katholisch')
        else:
            return
        
    def r_et(self):
        if r_e.isChecked() == True:
            r_erkre.clear()
            r_erkre.append('Ethik')
        else:
            return
        
    def save(self):
        if r_cl.isChecked() == False and r_pl.isChecked() == False:
            QMessageBox.about(self, 'Fehler', 'Bitte Wählen Sie Pysik Labor oder Chemie Labor')
            return
        if r_ds.isChecked() == False and r_ms.isChecked() == False:
            QMessageBox.about(self, 'Fehler', 'Bitte Wählen Sie Mathe stütz oder Deutsch stütz')
            return
        if r_sg.isChecked() == False and r_se.isChecked() == False and r_f.isChecked() == False:
            QMessageBox.about(self, 'Fehler', 'Bitte Wählen Sie Spanisch eAn, Spanisch gAn oder ob Sie bereits<br> eine dritte Fremdsprache belegt haben')
            return
        if r_kr.isChecked() == False and r_er.isChecked() == False and r_e.isChecked() == False:
            QMessageBox.about(self, 'Fehler', 'Bitte Wählen Sie katholische Religion, evangelische Religion oder Ethik')
            return
        else:
            finalsavearr = []
            mclass = ['Mathe', 'Deutsch','GGK', 'Englisch', 'Sport', 'Chemie', 'Physik', 'Informatik','Wirtschaft']
            finalsavearr.extend(mclass)
            finalsavearr.append(r_cp[0])
            finalsavearr.append(r_dsms[0])
            finalsavearr.append(r_sgsef[0])
            finalsavearr.append(r_erkre[0])
            print(finalsavearr)

            r_cl.setAutoExclusive(False)
            r_cl.setChecked(False)
            r_cl.setAutoExclusive(True)

            r_pl.setAutoExclusive(False)
            r_pl.setChecked(False)
            r_pl.setAutoExclusive(True)

            r_ds.setAutoExclusive(False)
            r_ds.setChecked(False)
            r_ds.setAutoExclusive(True)

            r_ms.setAutoExclusive(False)
            r_ms.setChecked(False)
            r_ms.setAutoExclusive(True)

            r_sg.setAutoExclusive(False)
            r_sg.setChecked(False)
            r_sg.setAutoExclusive(True)

            r_se.setAutoExclusive(False)
            r_se.setChecked(False)
            r_se.setAutoExclusive(True)

            r_f.setAutoExclusive(False)
            r_f.setChecked(False)
            r_f.setAutoExclusive(True)

            r_er.setAutoExclusive(False)
            r_er.setChecked(False)
            r_er.setAutoExclusive(True)

            r_kr.setAutoExclusive(False)
            r_kr.setChecked(False)
            r_kr.setAutoExclusive(True)

            r_e.setAutoExclusive(False)
            r_e.setChecked(False)
            r_e.setAutoExclusive(True)


            QMessageBox.about(self, 'Speicherbenachrichtigung', 'Ihre Eingabe wurde gespeichert!')
            db = DBHelp()
            print('Fächer werden in der Datenbank gespeichert')
            alleTrue = db.setzeMehrereFaecherBelegtTrue(finalsavearr, [1, 2])
            print(alleTrue)
            db.setzeJahrgängeAngegeben([1,2])
        
    def back(self):
        pipi = Launcher('homepage')
        pipi.launch()

#Anzeigen / Ausführen des Programms als sepeates Fenster
app = QtWidgets.QApplication(sys.argv)
win = SubjectChoice11()
win.show()
sys.exit(app.exec())