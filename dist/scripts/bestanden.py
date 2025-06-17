from Bewertung import *
#Importe DBHelp

class Bestanden(object):
    def __init__(self):
        self.HJG = Halbjahrgetten()      # type: ignore #kein plan was das ist
        self.all = []

    def ElfteBestanden(self):
        self.gesuchtesHJ = self.HJG.getGesuchtesHalbjahr()
        self.all = DBHelp.getArrayAusHalpjahrMitFachFachartNote(self.gesuchtesHJ)       #zurückgegebenes Array: [[fach, fachart, Note],[fach, fachart, Note],...]
        a = len(self.all)
        counterHF5 = 0
        counterNF5 = 0
        counterHF6 = 0
        counterNF6 = 0
        counterHF1 = 0
        counterNF1 = 0
        counterHF2 = 0
        counterNF2 = 0
        for i in range(0, a):
            if self.all(i)(1) == "Hauptfach":
                if self.all(i)(2) == 5:
                    counterHF5 += 1
                elif self.all(i)(2) == 6:
                    counterHF6 += 1
                elif self.all(i)(2) == 1:
                    counterHF1 += 1
                elif self.all(i)(2) == 2:
                    counterHF2 += 1
            else:
                if self.all(i)(2) == 5:
                    counterNF5 += 1
                elif self.all(i)(2) == 6:
                    counterNF6 += 1
                elif self.all(i)(2) == 1:
                    counterNF1 += 1
                elif self.all(i)(2) == 2:
                    counterNF2 += 1
        if counterHF6 >= 2:
            return False
        elif counterHF6 == 1 and counterHF1 > 1:
            return True
        #usw