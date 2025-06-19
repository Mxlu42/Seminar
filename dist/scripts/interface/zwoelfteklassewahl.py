import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox, QComboBox, QRadioButton
from PyQt6.QtCore import QSize, Qt
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from heart import Launcher
from dbhelp import *

class SubjectChoice11(QMainWindow):
    def __init__(self):
        global r_p, r_c, r_dm, r_de, r_me, r_sparr, r_sgarr, r_sp, r_sg, r_warr, r_ltarr, r_mparr, r_mp, r_w, r_lt, r_erkre, r_er, r_kr, r_e, r_en, r_s, r_enarr, r_sarr, r_cparr
        r_dm = []
        r_sparr = []
        r_sgarr = []
        r_warr = []
        r_ltarr = []
        r_mparr = []
        r_erkre = []
        r_enarr = []
        r_sarr = []
        r_cparr = []
        self.controll = 0
        self.controll0 = 0
        self.controll1 = 0
        self.controll2 = 0
        self.controll3 = 0
        self.controll4 = 0
        self.controll5 = 0
        super().__init__()
        
        #Mindestgröße / Titel definieren
        self.setCentralWidget(QWidget(self))
        self.setMinimumSize(QSize(500, 600))
        self.setMaximumSize(QSize(500, 600))
        self.setWindowTitle('12te klasse Fächerwahl')

        lbl = QLabel('Hie haben Sie zwei Verschiedene Arten von Wahlen zu tätigen, Wahlpflichtfächer<br>und Wahlfächer.<br>Bei den Wahlpflichtfächern geht es um Mathe- oder Deutsch eAn,<br>diese Wahl setzt gleichzeitig Ihr zweites Prüfungsfach auf das gewählte Fach.<br>Bei der Wahl der Glaubenslehre, können Sie sich neu Entscheiden, sollten dies aber<br>nicht tun wenn Sie das Fach im Abitur zur Auswahl haben möchten da dies nur<br>dann geht, wenn man es ab der elften Klasse belegt hat.<br>Bei der Wahl Englisch/Spanisch haben alle die Spanisch in der elften hatten die<br>möglichkeit Englisch abzuwählen. Sollten Sie kein Spanisch in der elften Klasse<br>gehabt haben, müssen Sie Englisch wählen.<br>Die Wahlpflichtfächer sind alle Vollkommen frei zu wählen alle bis auf Wirtschaft<br>befinden sich meist außerhalb der regulären Unterrichtszeit und können nicht als<br>Prüfungsfach gewählt werden (beim Seminarkurs gibt es eine Sonderregelung)')
        lbl.resize(lbl.sizeHint())
        lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        lbl.setMargin(30)
        self.setCentralWidget(lbl)

        wid1 = QWidget(self)
        grid1 = QVBoxLayout(wid1)
        wid1.setLayout(grid1)
        wid1.setMinimumSize(QSize(155, 62))
        wid1.setMaximumSize(QSize(155, 62))
        wid1.move(100, 307)

        r_de = QRadioButton('Deutsch eAn / Mathe gAn')
        r_de.toggled.connect(self.r_det)

        r_me = QRadioButton('Mathe eAn / Deutsch gAn')
        r_me.toggled.connect(self.r_met)

        grid1.addWidget(r_de)
        grid1.addWidget(r_me)


        wid2 = QWidget(self)
        grid2 = QVBoxLayout(wid2)
        wid2.setLayout(grid2)
        wid2.setMinimumSize(QSize(155, 62))
        wid2.setMaximumSize(QSize(155, 62))
        wid2.move(300, 307)

        r_sp = QRadioButton('Seminarkurs Profil')
        r_sp.toggled.connect(self.r_spt)

        r_sg = QRadioButton('Seminarkurs GGK')
        r_sg.toggled.connect(self.r_sgt)

        grid2.addWidget(r_sp)
        grid2.addWidget(r_sg)


        wid_w = QWidget(self)
        grid_w = QVBoxLayout(wid_w)
        wid_w.setLayout(grid_w)
        wid_w.setMinimumSize(QSize(205, 35))
        wid_w.setMaximumSize(QSize(205, 35))
        wid_w.move(300, 367)

        wid_lt = QWidget(self)
        grid_lt = QVBoxLayout(wid_lt)
        wid_lt.setLayout(grid_lt)
        wid_lt.setMinimumSize(QSize(205, 35))
        wid_lt.setMaximumSize(QSize(205, 35))
        wid_lt.move(300, 391)

        wid_mp = QWidget(self)
        grid_mp = QVBoxLayout(wid_mp)
        wid_mp.setLayout(grid_mp)
        wid_mp.setMinimumSize(QSize(205, 35))
        wid_mp.setMaximumSize(QSize(205, 35))
        wid_mp.move(300, 415)

        r_w = QRadioButton('Wirtschaft')
        r_w.toggled.connect(self.r_wt)

        r_lt = QRadioButton('Litheratur und Theater')
        r_lt.toggled.connect(self.r_ltt)

        r_mp = QRadioButton('Mathe plus')
        r_mp.toggled.connect(self.r_mpt)

        grid_w.addWidget(r_w)
        grid_lt.addWidget(r_lt)
        grid_mp.addWidget(r_mp)

        wid4 = QWidget(self)
        grid4 = QVBoxLayout(wid4)
        wid4.setLayout(grid4)
        wid4.setMinimumSize(QSize(205, 85))
        wid4.setMaximumSize(QSize(205, 85))
        wid4.move(100, 367)

        r_er = QRadioButton('evangelische Religion')
        r_er.toggled.connect(self.r_ert)

        r_kr = QRadioButton('katholische Religion')
        r_kr.toggled.connect(self.r_krt)

        r_e = QRadioButton('Ethik')
        r_e.toggled.connect(self.r_et)

        grid4.addWidget(r_er)
        grid4.addWidget(r_kr)
        grid4.addWidget(r_e)

        wid_en = QWidget(self)
        grid_en = QVBoxLayout(wid_en)
        wid_en.setLayout(grid_en)
        wid_en.setMinimumSize(QSize(205, 35))
        wid_en.setMaximumSize(QSize(205, 35))
        wid_en.move(100, 452)

        wid_s = QWidget(self)
        grid_s = QVBoxLayout(wid_s)
        wid_s.setLayout(grid_s)
        wid_s.setMinimumSize(QSize(205, 35))
        wid_s.setMaximumSize(QSize(205, 35))
        wid_s.move(100, 476)

        r_en = QRadioButton('Englisch')
        r_en.toggled.connect(self.r_ent)

        r_s = QRadioButton('Spanisch')
        r_s.toggled.connect(self.r_st)

        grid_en.addWidget(r_en)
        grid_s.addWidget(r_s)

        wid_pc = QWidget(self)
        grid_pc = QVBoxLayout(wid_pc)
        wid_pc.setLayout(grid_s)
        wid_pc.setMinimumSize(QSize(205, 62))
        wid_pc.setMaximumSize(QSize(205, 62))
        wid_pc.move(100, 510)

        r_p = QRadioButton('Physik')
        r_p.toggled.connect(self.r_pt)

        r_c = QRadioButton('Chemie')
        r_c.toggled.connect(self.r_ct)

        grid_pc.addWidget(r_c)
        grid_pc.addWidget(r_p)

        wpfwid = QWidget(self)
        wpfbox = QVBoxLayout(wpfwid)
        wpfwid.setMinimumSize(150, 50)
        wpfwid.setMaximumSize(150, 50)
        wpfwid.move(100, 267)

        wfwid = QWidget(self)
        wfbox = QVBoxLayout(wfwid)
        wfwid.setMinimumSize(100, 50)
        wfwid.setMaximumSize(100, 50)
        wfwid.move(300, 267)

        wpflbl = QLabel('<u>Wahlpflichtfächer:</u>')
        wpflbl.resize(wpflbl.sizeHint())

        wflbl = QLabel('<u>Wahlfächer:</u>')
        wflbl.resize(wpflbl.sizeHint())

        wpfbox.addWidget(wpflbl)
        wfbox.addWidget(wflbl)




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




    def r_det(self):
        if r_de.isChecked() == True:
            r_dm.clear()
            r_dm.append('Deutsch eAn')
        else:
            return
        
    def r_met(self):
        if r_me.isChecked() == True:
            r_dm.clear()
            r_dm.append('Mathe eAn')
        else:
            return
        
    def r_spt(self):
        if r_sp.isChecked() == True:
            self.controll = 1
            r_sparr.clear()
            r_sparr.append('Seminarkurs Profilfach')
        elif r_sp.isChecked() == False:
            r_sparr.clear()
            self.controll = 0
        
    def r_sgt(self):
        if r_sg.isChecked() == True:
            self.controll0 = 1
            r_sgarr.clear()
            r_sgarr.append('Seminarkurs GGK')
        elif r_sg.isChecked() == False:
            r_sgarr.clear()
            self.controll0 = 0
    
    def r_wt(self):
        if r_w.isChecked() == True:
            self.controll1 = 1
            r_warr.clear()
            r_warr.append('Wirtschaft')
        elif r_w.isChecked() == False:
            r_warr.clear()
            self.controll1 = 0
    
    def r_ltt(self):
        if r_lt.isChecked() == True:
            self.controll2 = 1
            r_ltarr.clear()
            r_ltarr.append('Literatur_Theater')
        elif r_lt.isChecked() == False:
            r_ltarr.clear()
            self.controll2 = 0
        
    def r_mpt(self):
        
        if r_mp.isChecked() == True:
            self.controll3 = 1
            r_mparr.clear()
            r_mparr.append('MathePlus')
        elif r_mp.isChecked() == False:
            r_mparr.clear()
            self.controll3 = 0
        
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
        
    def r_ent(self):
        if r_en.isChecked() == True:
            self.controll4 = 1
            r_enarr.clear()
            r_enarr.append('Englisch')
        elif r_en.isChecked() == False:
            r_enarr.clear()
            self.controll4 = 0

    def r_st(self):
        if r_s.isChecked() == True:
            self.controll5 = 1
            r_sarr.clear()
            r_sarr.append('SpanischN')
        elif r_s.isChecked() == False:
            r_sarr.clear()
            self.controll5 = 0

    def r_ct(self):
        if r_c.isChecked() == True:
            r_cparr.clear()
            r_cparr.append('Chemie')
            r_cparr.append('Chemie Labor')
        else:
            return

    def r_pt(self):
        if r_p.isChecked() == True:
            r_cparr.clear()
            r_cparr.append('Physik')
            r_cparr.append('Physik Labor')
        else:
            return
        
    def save(self):
        if r_de.isChecked() == False and r_me.isChecked() == False:
            QMessageBox.about(self, 'Fehler', 'Bitte Wählen Sie Deutsch eAn oder Mathe eAn')
            return
        if r_kr.isChecked() == False and r_er.isChecked() == False and r_e.isChecked() == False:
            QMessageBox.about(self, 'Fehler', 'Bitte Wählen Sie katholische Religion, evangelische Religion oder Ethik')
            return
        if r_en.isChecked() == False and r_s.isChecked() == False:
            QMessageBox.about(self, 'Fehler', 'Bitte Wählen Sie katholische Englisch oder Spanisch')
            return
        else:
            finalsavearr = []
            mclass = ['Mathe','GGK','Deutsch', 'Englisch', 'Sport','Informatik']
            for i in range(len(mclass)):
                finalsavearr.append(mclass[i])

            finalsavearr.append(r_dm[0])
            if self.controll == 1:
                finalsavearr.append(r_sparr[0])

            if self.controll0 == 1:
                finalsavearr.append(r_sgarr[0])

            if self.controll1 == 1:
                finalsavearr.append(r_warr[0])
                
            if self.controll2 == 1:
                finalsavearr.append(r_ltarr[0])
                
            if self.controll3 == 1:
                finalsavearr.append(r_mparr[0])
                
            finalsavearr.append(r_erkre[0])

            if self.controll4 == 1:
                finalsavearr.append(r_enarr[0])

            if self.controll5 == 1:
                finalsavearr.append(r_sarr[0])

            finalsavearr.append(r_cparr[0])
            finalsavearr.append(r_cparr[1])

            print(finalsavearr)
            final = finalsavearr.copy()
            finalsavearr.clear()

            r_de.setAutoExclusive(False)
            r_de.setChecked(False)
            r_de.setAutoExclusive(True)

            r_me.setAutoExclusive(False)
            r_me.setChecked(False)
            r_me.setAutoExclusive(True)

            r_sp.setAutoExclusive(False)
            r_sp.setChecked(False)
            r_sp.setAutoExclusive(True)

            r_sg.setAutoExclusive(False)
            r_sg.setChecked(False)
            r_sg.setAutoExclusive(True)

            r_w.setAutoExclusive(False)
            r_w.setChecked(False)
            r_w.setAutoExclusive(True)

            r_lt.setAutoExclusive(False)
            r_lt.setChecked(False)
            r_lt.setAutoExclusive(True)

            r_mp.setAutoExclusive(False)
            r_mp.setChecked(False)
            r_mp.setAutoExclusive(True)
            

            r_er.setAutoExclusive(False)
            r_er.setChecked(False)
            r_er.setAutoExclusive(True)

            r_kr.setAutoExclusive(False)
            r_kr.setChecked(False)
            r_kr.setAutoExclusive(True)

            r_e.setAutoExclusive(False)
            r_e.setChecked(False)
            r_e.setAutoExclusive(True)

            r_en.setAutoExclusive(False)
            r_en.setChecked(False)
            r_en.setAutoExclusive(True)

            r_s.setAutoExclusive(False)
            r_s.setChecked(False)
            r_s.setAutoExclusive(True)

            r_c.setAutoExclusive(False)
            r_c.setChecked(False)
            r_c.setAutoExclusive(True)

            r_p.setAutoExclusive(False)
            r_p.setChecked(False)
            r_p.setAutoExclusive(True)


            QMessageBox.about(self, 'Speicherbenachrichtigung', 'Ihre Eingabe wurde gespeichert!')
            db = DBHelp()
            print('Fächer werden in der Datenbank gespeichert')
            db.setzeMehrereFaecherBelegtTrue(final, [3, 4])
            db.setzeJahrgängeAngegeben([3,4])
        
    def back(self):
        pipi = Launcher('homepage')
        pipi.launch()





#Anzeigen / Ausführen des Programms als sepeates Fenster
app = QtWidgets.QApplication(sys.argv)
win = SubjectChoice11()
win.show()
sys.exit(app.exec())