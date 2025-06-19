from dbhelp import *

class Bestanden(object):
    def __init__(self):
        self.db = DBHelp()
        self.all = []
        self.counterrgesamtpunkte = 0
        self.counterrgesamtpunkteP = 0
        

    def ElfteBestanden(self):
        self.gesuchtesHJ = 1 and 2
        self.all = self.db.getArrayAusHalpjahrMitFachFachartGesamtnote(self.gesuchtesHJ)       #zurÃ¼ckgegebenes Array: [[fach, fachart, Gesamtnote],[fach, fachart, Gesamtnote],...]
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
        return True
        
    def FachochschulreifeBetanden(self):
        self.all.clear()
        HJ = [3, 4]
        for i in HJ:
            self.all.append(self.db.getArrayAusHalpjahrMitFachFachartGesamtnote(i))
        counterkernpunkte = 0
        counterkernunter = 0
        counterfachpunkte = 0
        counterfachunter = 0
        for u in range (0, len(self.all)):
            for i in range (0, len(self.all(u))):
                if self.all(u)(i)(2) == '0':
                    return False
                if self.all(u)(i)(1) == 'profil' or self.all(u)(i)(1) == 'eAn':
                    counterkernpunkte += self.all(u)(i)(2)
                    if self.all(u)(i)(2) < 5:
                        counterkernunter += 1
                
                else:
                    counterfachpunkte += self.all(u)(i)(2)
                    if self.all(u)(i)(2) < 5:
                        counterfachunter += 1
        if counterkernpunkte < 20:
            return False
        if counterkernunter > 2:
            return False
        if counterfachpunkte < 55:
            return False
        if counterkernunter < 4:
            return False
        return True
    
    def AbiPruefungBestanden(self):
        self.all.clear
        self.all.append(self.db.getArrayPruefungsfaecher())        #0 = fach, 1 = pruefungsnummer, 2 = punkte
        
        counterunter = 0
        counterunter = 0

        for i in range (0, len(self.all)):
            self.counterrgesamtpunkteP += self.all(i)(2) * 4
            if self.all(i)(2) < 5:
                counterunter += 1
            if self.all(i)(1) == ('1' or '2') and self.all(i)(2) < 5:
                return False
            if self.all(i)(2) == 0:
                return False 

        if counterunter > 2:
            return False
        if self.counterrgesamtpunkteP < 100:
            return False
        return True
        
    def AbiJahreBestanden(self):
        self.all.clear()
        HJ = [3, 4, 5, 6]
        for i in HJ:
            self.all.append(self.db.getArrayAusHalpjahrMitFachFachartGesamtnote(i))
        
        counterunterkurs = 0
        counterunterkursleistung = 0
        for u in range (0, len(self.all)):
            for i in range (0, len(self.all(u))):
                if self.all(u)(i)(2) < 5:
                    counterunterkurs += 1
                if self.all(u)(i)(2) < 5 and ( self.all(u)(i)(1) == 'Profil' or self.all(u)(i)(1) == 'Haupt' ):
                    counterunterkursleistung += 1
                if self.all(u)(i)(1) == ('Deutsch' or 'Mathe' or 'GGK' or 'Physik' or 'Chemie' or 'Mechatronik' or 'Informationstechnik' or 'Gestaltung_Medien' ) and self.all(u)(i)(2) == 0:
                    return False
                if self.all(u)(i)(1) == 'Profil' or  self.all(u)(i)(1) == 'EAN':
                    self.counterrgesamtpunkte += self.all(u)(i)(2)                
                self.counterrgesamtpunkte += self.all(u)(i)(2)
        self.counterrgesamtpunkte = self.counterrgesamtpunkte / 48
        if self.counterrgesamtpunkte < 200:
            return False
        if counterunterkurs > 7:
            return False
        if counterunterkursleistung > 3:
            return False
        if self.db.CountFaecherBelegt()  <= 36:             #in hj 3,4,5,6
            return False
        if self.db.coutFachBelegt('SpanischN') == 0 and self.db.coutFachBelegt('Englisch') != 4:
            return False
        if (self.db.coutFachBelegt('SpanischN') > 0 and self.db.coutFachBelegt('Englisch') < 4 and self.db.coutFachBelegt('Spanisch') < 2) or self.db.coutFachBelegt('SpanischN') > 0 and self.db.coutFachBelegt('Spanisch') < 4:
            return False
        return True
    
    def AbiBestanden(self):
        if self.AbiJahreBestanden() == False or self.AbiPruefungBestanden() == False:
            return False
        if self.counterrgesamtpunkte + self.counterrgesamtpunkteP < 300:
            return False
        return True