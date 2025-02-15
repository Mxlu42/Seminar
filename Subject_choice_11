import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox, QComboBox, QRadioButton
from PyQt6.QtCore import QSize, Qt
import time
class SubjectChoice11(QMainWindow):
    def __init__(self):
        global r_cp, r_cl, r_pl, r_dsms, r_ds, r_ms, r_sgsef, r_sg, r_se, r_f, r_erkre, r_er, r_kr, r_e
        super().__init__()
        
        #Mindestgröße / Titel definieren
        self.setCentralWidget(QWidget(self))
        self.setMinimumSize(QSize(500, 600))
        self.setMaximumSize(QSize(500, 600))
        self.setWindowTitle('11te klasse Fächerwahl')

        lbl = QLabel('Platzhalter für den Erklärtext')
        lbl.resize(lbl.sizeHint())
        lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        lbl.setMargin(30)
        self.setCentralWidget(lbl)

        wid1 = QWidget(self)
        grid1 = QVBoxLayout(wid1)
        wid1.setLayout(grid1)
        wid1.setMinimumSize(QSize(150, 57))
        wid1.setMaximumSize(QSize(150, 57))
        wid1.move(100, 342)
        r_cp = []

        r_cl = QRadioButton('Chemie Labor')
        r_cl.toggled.connect(self.r_clt)

        r_pl = QRadioButton('Physik Labor')
        r_pl.toggled.connect(self.r_plt)

        grid1.addWidget(r_cl)
        grid1.addWidget(r_pl)


        wid2 = QWidget(self)
        grid2 = QVBoxLayout(wid2)
        wid2.setLayout(grid2)
        wid2.setMinimumSize(QSize(150, 57))
        wid2.setMaximumSize(QSize(150, 57))
        wid2.move(300, 342)
        r_dsms = []

        r_ds = QRadioButton('Deutsch stütz')
        r_ds.toggled.connect(self.r_dst)

        r_ms = QRadioButton('Mathe stütz')
        r_ms.toggled.connect(self.r_mst)

        grid2.addWidget(r_ds)
        grid2.addWidget(r_ms)


        wid3 = QWidget(self)
        grid3 = QVBoxLayout(wid3)
        wid3.setLayout(grid3)
        wid3.setMinimumSize(QSize(200, 80))
        wid3.setMaximumSize(QSize(200, 80))
        wid3.move(100, 402)
        r_sgsef = []

        r_sg = QRadioButton('Spanisch gAn')
        r_sg.toggled.connect(self.r_sgt)

        r_se = QRadioButton('Spanisch eAn')
        r_se.toggled.connect(self.r_set)

        r_f = QRadioButton('Französisch vorkenntnisse')
        r_f.toggled.connect(self.r_ft)

        grid3.addWidget(r_sg)
        grid3.addWidget(r_se)
        grid3.addWidget(r_f)


        wid4 = QWidget(self)
        grid4 = QVBoxLayout(wid4)
        wid4.setLayout(grid3)
        wid4.setMinimumSize(QSize(200, 80))
        wid4.setMaximumSize(QSize(200, 80))
        wid4.move(300, 402)
        r_erkre = []

        r_er = QRadioButton('evangelische Religion')
        r_er.toggled.connect(self.r_ert)

        r_kr = QRadioButton('katholische Religion')
        r_kr.toggled.connect(self.r_krt)

        r_e = QRadioButton('Ethik')
        r_e.toggled.connect(self.r_et)

        grid4.addWidget(r_er)
        grid4.addWidget(r_kr)
        grid4.addWidget(r_e)





    def r_clt(self):
        if r_cl.isChecked() == True:
            r_cp = []
            r_cp.append('Chemie Labor')
            #Schnittstelle für Datenbank (jedes print steht für das Speichern der Wahl in einem Array)
            print(r_cp[0])
        else:
            return
        
    def r_plt(self):
        if r_pl.isChecked() == True:
            r_cp = []
            r_cp.append('Physik Labor')
            #Schnittstelle für Datenbank (jedes print steht für das Speichern der Wahl in einem Array)
            print(r_cp[0])
        else:
            return
        
    def r_dst(self):
        if r_ds.isChecked() == True:
            r_dsms = []
            r_dsms.append('Deutsch stütz')
            #Schnittstelle für Datenbank (jedes print steht für das Speichern der Wahl in einem Array)
            print(r_dsms[0])
        else:
            return
        
    def r_mst(self):
        if r_ms.isChecked() == True:
            r_dsms = []
            r_dsms.append('Mathe stütz')
            #Schnittstelle für Datenbank (jedes print steht für das Speichern der Wahl in einem Array)
            print(r_dsms[0])
        else:
            return
    
    def r_sgt(self):
        if r_sg.isChecked() == True:
            r_sgsef = []
            r_sgsef.append('Spanisch gAn')
            #Schnittstelle für Datenbank (jedes print steht für das Speichern der Wahl in einem Array)
            print(r_sgsef[0])
        else:
            return
    
    def r_set(self):
        if r_se.isChecked() == True:
            r_sgsef = []
            r_sgsef.append('Spanisch eAn')
            #Schnittstelle für Datenbank (jedes print steht für das Speichern der Wahl in einem Array)
            print(r_sgsef[0])
        else:
            return
        
    def r_ft(self):
        if r_f.isChecked() == True:
            r_sgsef = []
            r_sgsef.append('Französisch vorkenntnisse')
            #Schnittstelle für Datenbank (jedes print steht für das Speichern der Wahl in einem Array)
            print(r_sgsef[0])
        else:
            return
        
    def r_ert(self):
        if r_er.isChecked() == True:
            r_erkre = []
            r_erkre.append('evangelische Religion')
            #Schnittstelle für Datenbank (jedes print steht für das Speichern der Wahl in einem Array)
            print(r_erkre[0])
        else:
            return
        
    def r_krt(self):
        if r_kr.isChecked() == True:
            r_erkre = []
            r_erkre.append('katholische Religion')
            #Schnittstelle für Datenbank (jedes print steht für das Speichern der Wahl in einem Array)
            print(r_erkre[0])
        else:
            return
        
    def r_et(self):
        if r_e.isChecked() == True:
            r_erkre = []
            r_erkre.append('Ethik')
            #Schnittstelle für Datenbank (jedes print steht für das Speichern der Wahl in einem Array)
            print(r_erkre[0])
        else:
            return





#Anzeigen / Ausführen des Programms als sepeates Fenster
app = QtWidgets.QApplication(sys.argv)
win = SubjectChoice11()
win.show()
sys.exit(app.exec())