from dbhelp import *

class Notenberechnung(object):
    def __init__(self, a, b): 
        self.db = DBHelp()
        self.fach = b is not None
        self.HJ = a             #diereck von felix
        self.einzelnoten = []
        self.geteinzelnoten()
        self.BerechneHalbJahrFachGesamtNote()

    def geteinzelnoten(self):
        self.einzelnoten = self.db.GetAlleAusgefülltenNotenAlsArrayMitAngabeFach(self.fach, self.HJ)          #Alle Note in denen nicht "-" steht und mit Notentype. nichts mit den Notentype "Gesamt"

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
        self.db.setNoteInDBEsterFreierPlatzMitDemNotentypeDerNichtBelegtIst(self.fach, 7, "gesamt", erg)

    def Notendurchschnitt(self):
        noten = self.db.getAlleGesamstNotenAusHalbjahr(self.HJ)
        a = len(noten)
        znote = 0
        for i in range(0,a):
            znote += i
        erg = znote / a
        return erg
