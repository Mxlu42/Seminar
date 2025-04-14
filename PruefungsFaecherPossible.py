from pymongo import MongoClient
from dbhelp import *
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
        self.pr2 = DBHelp.get_faecher_by_fachart("EAN")
        self.FachblockPR2 = self.setFachblockPR2()
        self.prp3 = []
        self.setPruefungsfachDrei()
        self.FachblockPR3 = self.setFachblockPR3()
        self.pr3 = None
        self.prp4 = self.setPruefungsfachVier()
        self.FachblockPR4 = self.setFachblockPR4()
        self.pr4 = None
        self.prp5 = self.setPruefungsfachFuenf()
        self.pr5 = None
        self.FachblockPR5 = self.setFachblockPR5()

    def setPF3(self, fach):
        self.pr3 = fach

    def setPF4(self, fach):
        self.pr4 = fach

    def setPF5(self,fach):
        self.pr5 = fach

    def getPFP1(self):
        return self.pr1
    
    def getPFP2(self):
        return self.pr2
    
    def getPFP3(self):
        return self.prp3
    
    def getPFP4(self):
        return self.prp4
    
    def getPFP5(self):
        return self.prp5

    def setFachblockPR2(self):
        if self.pr2 == "Mathe EAN":
            return 1
        else:
            return 2
        
    def setFachblockPR3(self):
        if self.FachblockPR2 == 1 and self.prp3 == "Deutsch":
            return 1
        elif self.FachblockPR2 == 1 and (self.prp3 == "Englisch" or self.prp3 == "Spanisch"):
            return 2
        elif self.FachblockPR2 == 2 and self.prp3 == "Mathe":
            return 3
        elif self.FachblockPR2 == 2 and (self.prp3 == "Englisch" or self.prp3 == "Spanisch"):
            return 4

    def setFachblockPR4(self):
        if (self.FachblockPR2 == 1 and (self.FachblockPR3  == 1 or self.FachblockPR3 == 2) or (self.FachblockPR2 == 2 and self.FachblockPR3 == 3)) and (self.prp4 == "GGK" or self.prp4 == "ReliKat" or self.prp4 == "ReliEva" or self.prp4 == "Ethik" or self.prp4 == "Wirtschaft"):
            return 1
        elif (self.FachblockPR2 == 1 and (self.FachblockPR3  == 1 and (self.prp4 == "Chemie" or self.prp4 == "Physik" or self.prp4 == "Englisch" or self.prp4 == "Spanisch")) or (self.FachblockPR3 == 2 and self.prp3 == "Englisch" (self.prp4 == "Chemie" or self.prp4 == "Physik" or self.prp4 == "Deutsch GAN" or self.prp4 == "Spanisch")) or self.FachblockPR3 == 3 and (self.prp4 == "Chemie" or self.prp4 == "Physik" or self.prp4 == "Englisch" or self.prp4 == "Spanisch")):
            return 2
        elif self.FachblockPR2 == 1 and self.FachblockPR3 == 4 and (self.prp4 == "GGK" or self.prp4 == "ReliKat" or self.prp4 == "ReliEva" or self.prp4 == "Ethik" or self.prp4 == "Wirtschaft"):
            return 3
        elif self.FachblockPR2 == 1 and self.FachblockPR3 == 4 and (self.prp4 == "Chemie" or self.prp4 == "Physik" or self.prp4 == "Mathe GAN"):
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

    def setPruefungsfachDrei(self):
        if self.FachblockPR2 == 1:
            self.prp3.append("Deutsch GAN")
            if DBHelp.pruefe_halbjahr_angegeben(1) == False:                                                 #Hier schau dir das mal an noah
                self.prp3.append("Englisch")
                self.prp3.append("Spanisch")
            if DBHelp.FachBelegt("Englisch") == True: #and englisch.KS.belegt == True:                     #NOAH was das?
                self.prp3.append("Englisch")
            if DBHelp.FachBelegt("SpanischN") == True or DBHelp.FachBelegt("SpanischF") == True:        #HEY SÜßI
                self.prp3.append("Spanisch")

        elif self.FachblockPR2 == 2:
            self.prp3.append("Mathe GAN")
            if DBHelp.pruefe_halbjahr_angegeben(1) == False:                                                 #Willst du dir das mal anschauen
                self.prp3.append("Englisch")
                self.prp3.append("Spanisch")
            if DBHelp.FachBelegt("Englisch") == True: #and englisch.KS.belegt == True:                     #Noah schau, mal db sachen
                self.prp3.append("Englisch")
            if DBHelp.FachBelegt("SpanischN") == True or DBHelp.FachBelegt("SpanischF") == True:        #Da fehlt was
                self.prp3.append("Spanisch")
            

    def setPruefungsfachVier(self):
        block1 = ["GGK", "ReliKat", "ReliEva", "Wirtscchaft"]
        block2 = ["Chemie", "Physik", "Deutsch GAN"]
        if DBHelp.pruefe_halbjahr_angegeben(1) == False:                                                     #>_<
            block2.append("Englisch")
            block2.append("Spanisch")
        if DBHelp.FachBelegt("Englisch") == True: #and englisch.KS.belegt == True:                     #Noah schau, mal db sachen
            self.pr3.append("Englisch")
        if DBHelp.FachBelegt("SpanischN") == True or DBHelp.FachBelegt("SpanischF") == True:      #Bitti mach ganz <OoO>
            block2.append("Spanisch")
        if self.pr3 == "Deutsch GAN":
            block2.remove("Deutsch GAN")
        if self.pr3 == "Englich":
            block2.remove("Englisch")
        if self.pr3 == "Spanisch":
            block2.remove("Spanisch")
        block3 = block1
        block4 = ["Chemie", "Physik", "Mathe GAN"]
        if self.FachblockPR2 == 1 and (self.FachblockPR3 == 1 or self.FachblockPR3 == 2 or self.FachblockPR3 == 3):
            return block1 + block2
        else:
            return block3 + block4

    def setPruefungsfachFuenf(self):
        block2 = ["GGK", "ReliKat", "ReliEva", "Ethik", "Wirtschaft", "SeminarGGK"]
        block3 = ["Chemie", "Physik", "Mathe GAN"]
        block4 = block2
        block1 = ["SeminarGGK", "SeminarProfil", "GGk", "ReliKat", "ReliEva", "Ethik", "Wirtschaft", "Chemie", "Physik", "Inforkatik", "Deutscch GAN", "Sport"]
        if DBHelp.pruefe_halbjahr_angegeben(1) == False:
            block1.append("Englisch")
            block1.append("Spanisch")
        if DBHelp.FachBelegt("Englisch") == True: #and englisch.KS.belegt == True:                     #Noah schau, mal db sachen
            self.pr3.append("Englisch")
        if DBHelp.FachBelegt("SpanischN") == True or DBHelp.FachBelegt("SpanischF") == True:      #Letzter ich schwöre
            block1.append("Spanisch")
        if self.prp2 == "Deutsch EAN" or self.prp3 == "Deutsch GAN":
            block1.remove("Deutsch GAN")
        if self.pr3 == "Englisch":
            block1.remove("Englisch")
        if self.pr3 == "Spanisch":
            block1.remove("Spanisch")
        if self.pr4 == "GGK":
            block1.remove("GGK")
        if self.prp4 == "ReliKat" or self.prp4 == "ReliEva" or self.prp4 == "Ethik":
            block1.remove("ReliKat")
            block1.remove("ReliEva")
            block1.remove("Ethik")
        if self.prp4 == "Wirtschaft":
            block1.remove("Wirtschaft")
        if self.FachblockPR4 == 1:
            return block1
        if self.FachblockPR4 == 2:
            return block2
        if self.FachblockPR4 == 3:
            return block3
        if self.FachblockPR4 == 4:
            return block4
        