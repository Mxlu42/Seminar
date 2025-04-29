from bewertung import *
#Importe DBHelp

class Notenberechnung(object):
    def __init__(self):
        self.HJG = Halbjahrgetten()      # type: ignore #kein plan was das ist
        self.fach = None
        self.HJ = None
        self.einzelnoten = []
        self.geteinzelnoten()
        self.gesamtNote = self.BerechneHalbJahrFachGesamtNote()

    def setfach(self, a):
        self.fach = a                                                                               #Von felix bidde

    def setHJ(self):
        self.HJ = self.HJG.getGesuchtesHalbjahr()

    def geteinzelnoten(self):
        self.einzelnoten = DBHelp.GetAlleAusgefülltenNotenAlsArrayMitAngabeFach(self.fach)          #Alle Note in denen nicht "-" steht und mit Notentype. nichts mit den Notentype "Gesamt"

    def BerechneHalbJahrFachGesamtNote(self):
        a = len(self.einzelnoten)
        gesamt = 0
        for i in range (0, a):
            if self.einzelnoten(i)(2) == "Schriftlich" or self.einzelnoten(i)(2) == "GSF":
                gesamt += self.einzelnoten(i)(1)
            else:
                gesamt += 0.5*self.einzelnoten(i)(1)
        self.gesamtNote = gesamt / a
