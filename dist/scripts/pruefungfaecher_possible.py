from pymongo import MongoClient
from scripts.dbhelp import *
client = MongoClient('localhost', 27017)
db = client['school']
collection = db['students']

#Alles Für Felix was mögliche eingabe des Users sind

class PruefungsfaecherPossible(object):
    def __init__(self):
        if DBHelp.FachBelegt("Evangelisch") == True:
            self.a = "Evangelisch"
        elif DBHelp.FachBelegt("Katholisch") == True:
            self.a = "Katholisch"
        else:
            self.a = "Ethik"
        
        self.pr1 = DBHelp.get_faecher_by_fachart("Hauptfach")
        self.setFachtype(self.pr1)
        self.pr2 = []
        if DBHelp.pruefe_halbjahr_angegeben(1) == True:
            self.pr2.append(DBHelp.get_faecher_by_fachart("EAN"))
        else:
            self.pr2.append(self.setPruefungsfachZwei())
        
        self.FachblockPR2 = self.setFachblockPR2()
        self.pr3 = []
        self.setPruefungsfachDrei()
        self.FachblockPR3 = self.setFachblockPR3()
        self.pr4 = self.setPruefungsfachVier()
        self.FachblockPR4 = self.setFachblockPR4()
        self.pr5 = self.setPruefungsfachFuenf()
        self.FachblockPR5 = self.setFachblockPR5()

    def getPF1(self):
        return self.pr1
    
    def getPF2(self):
        return self.pr2
    
    def getPF3(self):
        return self.pr3
    
    def getPF4(self):
        return self.pr4
    
    def getPF5(self):
        return self.pr5

    def setFachblockPR2(self):
        if self.pr2 == "Mathe":
            return 1
        else:
            return 2
        
    def setFachblockPR3(self):
        if self.FachblockPR2 == 1 and self.pr3 == "Deutsch":
            return 1
        elif self.FachblockPR2 == 1 and (self.pr3 == "Englisch" or self.pr3 == "Spanisch"):
            return 2
        elif self.FachblockPR2 == 2 and self.pr3 == "Mathe":
            return 3
        elif self.FachblockPR2 == 2 and (self.pr3 == "Englisch" or self.pr3 == "Spanisch"):
            return 4

    def setFachblockPR4(self):
        if (self.FachblockPR2 == 1 and (self.FachblockPR3  == 1 or self.FachblockPR3 == 2) or (self.FachblockPR2 == 2 and self.FachblockPR3 == 3)) and (self.pr4 == "GGK" or self.pr4 == "ReliKat" or self.pr4 == "ReliEva" or self.pr4 == "Ethik" or self.pr4 == "Wirtschaft"):
            return 1
        elif (self.FachblockPR2 == 1 and (self.FachblockPR3  == 1 and (self.pr4 == "Chemie" or self.pr4 == "Physik" or self.pr4 == "Englisch" or self.pr4 == "Spanisch")) or (self.FachblockPR3 == 2 and self.pr3 == "Englisch" (self.pr4 == "Chemie" or self.pr4 == "Physik" or self.pr4 == "Deutsch" or self.pr4 == "Spanisch")) or self.FachblockPR3 == 3 and (self.pr4 == "Chemie" or self.pr4 == "Physik" or self.pr4 == "Englisch" or self.pr4 == "Spanisch")):
            return 2
        elif self.FachblockPR2 == 1 and self.FachblockPR3 == 4 and (self.pr4 == "GGK" or self.pr4 == "ReliKat" or self.pr4 == "ReliEva" or self.pr4 == "Ethik" or self.pr4 == "Wirtschaft"):
            return 3
        elif self.FachblockPR2 == 1 and self.FachblockPR3 == 4 and (self.pr4 == "Chemie" or self.pr4 == "Physik" or self.pr4 == "Mathe"):
            return 4


    def setFachblockPR5(self):
        if self.FachblockPR4 == 1:
            return 1
        elif self.FachblockPR4 == 2:
            return 2
        elif self.FachblockPR4 == 3:
            return 3
        elif self.FachblockPR4 == 4:
            return 4
    
    def setPruefungsfachZwei(self):
        block = ["Mathe", "Deutsch"]
        return block
    
    def setPruefungsfachDrei(self):
        if self.FachblockPR2 == 1:
            self.pr3.append("Deutsch")
            if DBHelp.pruefe_halbjahr_angegeben(1) == False:                                                 #Hier schau dir das mal an noah
                self.pr3.append("Englisch")
                self.pr3.append("SpanischN")
            if DBHelp.FachBelegt("Englisch") == True: #and englisch.KS.belegt == True:                     #NOAH was das?
                self.pr3.append("Englisch")
            if DBHelp.FachBelegt("SpanischN") == True or DBHelp.FachBelegt("SpanischF") == True:        #HEY SÜßI
                self.pr3.append("SpanischN")

        elif self.FachblockPR2 == 2:
            self.pr3.append("Mathe")
            if DBHelp.pruefe_halbjahr_angegeben(1) == False:                                                 #Willst du dir das mal anschauen
                self.pr3.append("Englisch")
                self.pr3.append("SpanischN")
            if DBHelp.FachBelegt("Englisch") == True: #and englisch.KS.belegt == True:                     #Noah schau, mal db sachen
                self.pr3.append("Englisch")
            if DBHelp.FachBelegt("SpanischN") == True or DBHelp.FachBelegt("SpanischF") == True:        #Da fehlt was
                self.pr3.append("SpanischN")
            

    def setPruefungsfachVier(self):
        block1 = ["GGK", "ReliKat", "ReliEva", "Wirtscchaft"]
        block2 = ["Chemie", "Physik", "Deutsch"]
        if DBHelp.pruefe_halbjahr_angegeben(1) == False:                                                     #>_<
            block2.append("Englisch")
            block2.append("SpanischN")
        if DBHelp.FachBelegt("Englisch") == True: #and englisch.KS.belegt == True:                     #Noah schau, mal db sachen
            self.pr3.append("Englisch")
        if DBHelp.FachBelegt("SpanischN") == True or DBHelp.FachBelegt("SpanischF") == True:      #Bitti mach ganz <OoO>
            block2.append("SpanischN")
        if self.pr3 == "Deutsch":
            block2.remove("Deutsch")
        if self.pr3 == "Englich":
            block2.remove("Englisch")
        if self.pr3 == "SpanischN":
            block2.remove("SpanischN")
        block3 = block1
        block4 = ["Chemie", "Physik", "Mathe "]
        if self.FachblockPR2 == 1 and (self.FachblockPR3 == 1 or self.FachblockPR3 == 2 or self.FachblockPR3 == 3):
            return block1 + block2
        else:
            return block3 + block4

    def setPruefungsfachFuenf(self):
        block2 = ["GGK", self.a, "Wirtschaft", "SeminarGGK"]
        block3 = ["Chemie", "Physik", "Mathe"]
        block4 = block2
        block1 = ["SeminarGGK", "SeminarProfil", "GGk", self.a, "Wirtschaft", "Chemie", "Physik", "Inforkatik", "Deutscch", "Sport"]
        if DBHelp.pruefe_halbjahr_angegeben(1) == False:
            block1.append("Englisch")
            block1.append("SpanischN")
        if DBHelp.FachBelegt("Englisch") == True: #and englisch.KS.belegt == True:                     #Noah schau, mal db sachen
            self.pr3.append("Englisch")
        if DBHelp.FachBelegt("SpanischN") == True or DBHelp.FachBelegt("SpanischF") == True:      #Letzter ich schwöre
            block1.append("SpanischN")
        if self.pr2 == "Deutsch EAN" or self.pr3 == "Deutsch":
            block1.remove("Deutsch")
        if self.pr3 == "Englisch":
            block1.remove("Englisch")
        if self.pr3 == "SpanischN":
            block1.remove("SpanischN")
        if self.pr4 == "GGK":
            block1.remove("GGK")
        if self.pr4 == self.a:
            block1.remove(self.a)
        if self.pr4 == "Wirtschaft":
            block1.remove("Wirtschaft")
        if self.FachblockPR4 == 1:
            return block1
        if self.FachblockPR4 == 2:
            return block2
        if self.FachblockPR4 == 3:
            return block3
        if self.FachblockPR4 == 4:
            return block4
        