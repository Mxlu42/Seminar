import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox, QComboBox, QRadioButton
from PyQt6.QtCore import QSize, Qt
from PruefungsFaecherPossible import *
class Pruefungsfaecherwahl(QMainWindow):
    def __init__(self):
        pfc = PruefungsfaecherPossible()
        PFP1 = pfc.getPFP1()
        PFP2 = pfc.getPFP2()
        PFP3 = pfc.getPFP3()
        PFP4 = pfc.getPFP4()
        PFP5 = pfc.getPFP5()
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
        wid1.setMinimumSize(QSize(150, 300))
        wid1.setMaximumSize(QSize(150, 300))
        wid1.move(200, 250)

        lbl1 = QLabel('1. Prüfungsfach')
        lbl1.resize(lbl1.sizeHint())
        box1.addWidget(lbl1)

        cbb1 = QComboBox(self)
        cbb1.addItem('Bitte wählen')
        cbb1.addItems(PFP1)
        cbb1.resize(cbb1.sizeHint())
        box1.addWidget(cbb1)
        cbb1.currentIndexChanged.connect(self.update_cbb_1())

        lbl2 = QLabel('2. Prüfungsfach')
        lbl2.resize(lbl2.sizeHint())
        box1.addWidget(lbl2)
        
        cbb2 = QComboBox(self)
        cbb2.addItem('Bitte wählen')
        cbb2.addItems(PFP2)
        cbb2.resize(cbb2.sizeHint())
        box1.addWidget(cbb2)
        cbb2.currentIndexChanged.connect(self.update_cbb_2())

        lbl3 = QLabel('3. Prüfungsfach')
        lbl3.resize(lbl3.sizeHint())
        box1.addWidget(lbl3)

        cbb3 = QComboBox(self)
        cbb3.addItem('Bitte wählen')
        cbb3.addItems(PFP3)
        cbb3.resize(cbb3.sizeHint())
        box1.addWidget(cbb3)
        cbb3.currentIndexChanged.connect(self.update_cbb_3())

        lbl4 = QLabel('4. Prüfungsfach')
        lbl4.resize(lbl4.sizeHint())
        box1.addWidget(lbl4)

        cbb4 = QComboBox(self)
        cbb4.addItem('Bitte wählen')
        cbb4.addItems(PFP4)
        cbb4.resize(cbb4.sizeHint())
        box1.addWidget(cbb4)
        cbb4.currentIndexChanged.connect(self.update_cbb_4())

        lbl5 = QLabel('5. Prüfungsfach')
        lbl5.resize(lbl5.sizeHint())
        box1.addWidget(lbl5)

        cbb5 = QComboBox(self)
        cbb5.addItem('Bitte wählen')
        cbb5.addItems(['PFP5 placeholder'])
        cbb5.resize(cbb5.sizeHint())
        box1.addWidget(cbb5)
        cbb5.currentIndexChanged.connect(self.update_cbb_5())

    def update_cbb_1():
        pass

    def update_cbb_2():
        pass

    def update_cbb_3():
        pass

    def update_cbb_4():
        pass

    def update_cbb_5():
        pass


        self.combo_boxes = []
        for i in range(5):
            label = QLabel(f'{i + 1}. Prüfungsfach')
            layout.addWidget(label)

            combo = QComboBox(self)
            combo.addItem('Bitte wählen')
            if i == 0:
                combo.addItems(self.PFP1)  # First dropdown gets PFP1
            elif i == 1:
                combo.addItems(self.PFP2)  # Second dropdown gets PFP2
            elif i == 2:
                combo.addItems(self.PFP3)  # Third dropdown gets PFP3
            elif i == 3:
                combo.addItems(self.PFP4)  # Fourth dropdown gets PFP4
            else:
                combo.addItem('PFP5 placeholder')  # Placeholder for PFP5
            combo.currentIndexChanged.connect(self.update_dropdowns)
            self.combo_boxes.append(combo)
            layout.addWidget(combo)

        self.setCentralWidget(main_widget)

    def update_dropdowns(self):
        # Update dropdown choices based on the selections made
        selected_values = [combo.currentText() for combo in self.combo_boxes]
        
        # Example update logic: change PFP5 options based on PFP1-4
        if self.combo_boxes[0].currentIndex() != 0:  # If PFP1 is selected
            self.combo_boxes[4].clear()  # Clear PFP5 options
            self.combo_boxes[4].addItems(self.PFP5)  # Add PFP5 option
        





#Anzeigen / Ausführen des Programms als sepeates Fenster
app = QtWidgets.QApplication(sys.argv)
win = Pruefungsfaecherwahl()
win.show()
sys.exit(app.exec())