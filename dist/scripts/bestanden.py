from bewertung import *
from dbhelp import *

class Bestanden(object):
    def __init__(self):
        self.HJG = Halbjahrgetten()      # type: ignore #kein plan was das ist
        self.all = []

    def ElfteBestanden(self):
        self.gesuchtesHJ = 1 and 2
        self.all = DBHelp.getArrayAusHalpjahrMitFachFachartNote(self.gesuchtesHJ)       #zurÃ¼ckgegebenes Array: [[fach, fachart, Gesamtnote],[fach, fachart, Gesamtnote],...]
        a = len(self.all)
        counterHF5 = 0
        counterNF5 = 0
        counterHF6 = 0
        counterNF6 = 0
        counterHF1 = 0
        counterNF1 = 0
        counterHF2 = 0
        counterNF2 = 0
        counterHF3 = 0
        counterNF3 = 0
        for i in range(0, a):
            if self.all(i)(2) == "Hauptfach":                   # Hauptfach = Kernfach 
                if self.all(i)(2) == 5:
                    counterHF5 += 1
                elif self.all(i)(2) == 6:
                    counterHF6 += 1
                elif self.all(i)(2) == 1:
                    counterHF1 += 1
                elif self.all(i)(2) == 2:
                    counterHF2 += 1
                elif self.all(i)(2) == 3:
                    counterHF3 += 1
            else:
                if self.all(i)(2) == 5:
                    counterNF5 += 1
                elif self.all(i)(2) == 6:
                    counterNF6 += 1
                elif self.all(i)(2) == 1:
                    counterNF1 += 1
                elif self.all(i)(2) == 2:
                    counterNF2 += 1
                elif self.all(i)(2) == 3:
                    counterNF3 += 1
        if counterHF6 > 0:
            return False
        elif counterHF5 > 2:
            return False
        elif counterHF5 == 2 and (counterHF1 + counterHF2) < 2:
            return False
        elif counterHF5 == 1 and (counterHF1 == 0 or counterHF2 == 0 or counterHF3 == 0):
            return False
        elif counterNF6 == 2 and (counterHF1 >= 2 and (counterNF1 == 1 and counterNF2 < 2) and counterNF2 < 4): #Nicht correct ig   #https://thg-relaunch.jimdofree.com/unterricht/regeln/versetzungsordnung/#:~:text=Durchschnitt%20aus%20den%20Noten%20aller%20f%C3%BCr%20die,5%20oder%206%20k%C3%B6nnen%20nicht%20ausgeglichen%20werden):
            return False
        
    def AbiJahreBestanden(self):
        if DBHelp.CountFaecherBelegt()  < 36:             #in hj 3,4,5,6
            return False
        if self.spanischbelegt == 0 and DBHelp.coutFachBelegt('Englisch') != 4:
            return False
        if (self.spanischbelegt > 0 and DBHelp.coutFachBelegt('Englisch') < 4 and DBHelp.coutFachBelegt('Spanisch') < 2) or self.spanischbelegt > 0 and DBHelp.coutFachBelegt('Spanisch') < 4:
            return False
        if DBHelp.ZaehleAllePunkte() < 300:
            return False
        if DBHelp.BetegpflichtigNullCount() > 0:
            return False
        return True