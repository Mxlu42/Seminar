from bewertung import *
from dbhelp import *

class Notenberechnung(object):
    def __init__(self, a, b): 
        self.fach = b
        self.HJ = a             #diereck von felix
        self.einzelnoten = []
        self.geteinzelnoten()
        self.BerechneHalbJahrFachGesamtNote()

    def geteinzelnoten(self):
        self.einzelnoten = DBHelp.GetAlleAusgefülltenNotenAlsArrayMitAngabeFach(self.fach, self.HJ)          #Alle Note in denen nicht "-" steht und mit Notentype. nichts mit den Notentype "Gesamt"

    def BerechneHalbJahrFachGesamtNote(self):
        a = len(self.einzelnoten)
        gesamta = a
        gesamt = 0
        for i in range (0, a):
            if self.einzelnoten[i][2] == "Schriftlich" or self.einzelnoten[i][2] == "GSF":
                gesamt += 2 * self.einzelnoten[i][1]
                gesamta += 1
            else:
                gesamt += self.einzelnoten[i][1]
        erg = int(gesamt / gesamta)
        DBHelp.setNoteInDBEsterFreierPlatzMitDemNotentypeDerNichtBelegtIst(self.fach, 7, "gesamt", erg)
