from pymongo import MongoClient
from dbhelp import *
client = MongoClient('localhost', 27017)
db = client['school']
collection = db['students']

#Alles Für Felix was mögliche eingabe des Users sind

class PruefungsfaecherPossible(object):
    def __init__(self):
        if DBHelp.pruefe_halbjahr_angegeben(1) == True:
            if DBHelp.FachBelegt("Evangelisch", 1) == True and DBHelp.FachBelegt("Evangelisch", 3) == True:
                self.a = "Evangelisch"
                self.aState = True
            elif DBHelp.FachBelegt("Katholisch", 1) == True and DBHelp.FachBelegt("Katholisch", 3) == True:
                self.a = "Katholisch"
                self.aState = True
            elif DBHelp.FachBelegt("Ethik", 1) == True and DBHelp.FachBelegt("Ethik", 3) == True:
                self.a = "Ethik"
                self.aState = True
            else:
                self.a = ""
                self.aState = False
        else:
            self.a = "Ethik"
            self.aState = True
        
        self.pr1 = DBHelp.get_faecher_by_fachart("Hauptfach")
        self.prp2 = None

        self.pr2 = DBHelp.get_faecher_by_fachart("EAN")
        self.prp2 = None
            
        self.FachblockPR2 = self.setFachblockPR2()
        self.prp3 = self.setPruefungsfachDrei()
        self.FachblockPR3 = 0
        self.pr3 = None
        self.prp4 = self.setPruefungsfachVier()
        self.FachblockPR4 = 0
        self.pr4 = None
        self.prp5 = self.setPruefungsfachFuenf()
        self.pr5 = None
        self.FachblockPR5 = 0

    def setPF2(self, fach):
        self.pr2 = fach
    
    def setPF3(self, fach):
        self.pr3 = fach

    def setPF4(self, fach):
        self.pr4 = fach

    def setPF5(self,fach):
        print(fach)
        self.pr5 = fach

    def getPFP1(self):
        if self.pr1 == []:
            self.prp1 = self.setPrufungsfachEins()
        else:
            self.prp1 = self.pr1
        return self.prp1
    
    def getPFP2(self):
        if self.pr2 == []:
            self.prp2 = self.setPrufungsfachZwei()
        else:
            self.prp2 = self.pr2
        return self.prp2
    
    def getPFP3(self):
        self.prp3 = self.setPruefungsfachDrei()
        return self.prp3
    
    def getPFP4(self):
        self.prp4 = self.setPruefungsfachVier()
        return self.prp4
    
    def getPFP5(self):
        self.prp5 = self.setPruefungsfachFuenf()
        return self.prp5

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
        if (self.FachblockPR2 == 1 and (self.FachblockPR3  == 1 or self.FachblockPR3 == 2) or (self.FachblockPR2 == 2 and self.FachblockPR3 == 3)) and (self.pr4 == "GGK" or self.pr4 == self.a or self.pr4 == "Wirtschaft"):
            return 1
        elif (self.FachblockPR2 == 1 and (self.FachblockPR3  == 1 and (self.pr4 == "Chemie" or self.pr4 == "Physik" or self.pr4 == "Englisch" or self.pr4 == "Spanisch")) or (self.FachblockPR3 == 2 and self.pr3 == "Englisch" (self.pr4 == "Chemie" or self.pr4 == "Physik" or self.pr4 == "Deutsch" or self.pr4 == "Spanisch")) or self.FachblockPR3 == 3 and (self.pr4 == "Chemie" or self.pr4 == "Physik" or self.pr4 == "Englisch" or self.pr4 == "Spanisch")):
            return 2
        elif self.FachblockPR2 == 1 and self.FachblockPR3 == 4 and (self.pr4 == "GGK" or self.pr4 == self.a or self.pr4 == "Wirtschaft"):
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
        
    def setPrufungsfachEins(self):
        block = ["Informationstechnik", "Mechatronik", "Gestaltung_Medien"]
        return block
        
    def setPrufungsfachZwei(self):
        block = ["Mathe", "Deutsch"]
        return block

    def setPruefungsfachDrei(self):
        self.FachblockPR2 = self.setFachblockPR2()
        block = []
        if self.FachblockPR2 == 1:
            block.append("Deutsch")
            if DBHelp.pruefe_halbjahr_angegeben(1) == False:                                            #Hier schau dir das mal an noah
                block.append("Englisch")
                block.append("Spanisch")
            if DBHelp.FachBelegt("Englisch", 1) == True and DBHelp.FachBelegt("Englisch", 3) == True:                  #NOAH was das?
                block.append("Englisch")
            if DBHelp.FachBelegt("SpanischN", 1) == True or DBHelp.FachBelegt("SpanischF", 1) == True:        #HEY SÜßI
                block.append("Spanisch")

        elif self.FachblockPR2 == 2:
            block.append("Mathe")
            if DBHelp.pruefe_halbjahr_angegeben(1) == False:                                                 #Willst du dir das mal anschauen
                block.append("Englisch")
                block.append("Spanisch")
            if DBHelp.FachBelegt("Englisch", 1) == True and DBHelp.FachBelegt("Englisch", 3) == True:                     #Noah schau, mal db sachen
                block.append("Englisch")
            if DBHelp.FachBelegt("SpanischN", 1) == True or DBHelp.FachBelegt("SpanischF", 1) == True:        #Da fehlt was
                block.append("Spanisch")
        return block
            

    def setPruefungsfachVier(self):
        self.FachblockPR3 = self.setFachblockPR3()
        block1 = ["GGK", self.a, "Wirtschaft"]
        block2 = ["Chemie", "Physik", "Deutsch"]
        if DBHelp.pruefe_halbjahr_angegeben(1) == False:                                                     #>_<
            block2.append("Englisch")
            block2.append("Spanisch")
        if DBHelp.FachBelegt("Englisch", 1) == True and DBHelp.FachBelegt("Englisch", 3) == True:                     #Noah schau, mal db sachen
            block1.append("Englisch")
        if DBHelp.FachBelegt("SpanischN", 1) == True or DBHelp.FachBelegt("SpanischF", 1) == True:      #Bitti mach ganz <OoO>
            block2.append("Spanisch")
        if self.pr3 == "Deutsch":
            block2.remove("Deutsch")
        if self.pr3 == "Englich":
            block2.remove("Englisch")
        if self.pr3 == "Spanisch":
            block2.remove("Spanisch")
        if self.FachblockPR2 == 2:
            block2.remove("Deutsch")
        
        block3 = block1
        block4 = ["Chemie", "Physik", "Mathe"]
        if (self.FachblockPR2 == 1 or self.FachblockPR2 == 2) and (self.FachblockPR3 == 1 or self.FachblockPR3 == 2 or self.FachblockPR3 == 3):
            print("block 1 und 2")
            return block1 + block2
        else:
            return block3 + block4

    def setPruefungsfachFuenf(self):
        self.FachblockPR4 = self.setFachblockPR4()
        block2 = ["GGK", "Wirtschaft", "SeminarGGK"]
        block3 = ["Chemie", "Physik", "Mathe"]
        block4 = block2
        block1 = ["SeminarGGK", "SeminarProfil", "GGK", "Wirtschaft", "Chemie", "Physik", "Inforkatik", "Deutsch", "Sport"]
        if self.aState == True:
            block2.append(self.a)
            block1.append(self.a)
            if self.pr4 == self.a:
                block1.remove(self.a)
        if DBHelp.pruefe_halbjahr_angegeben(3) == False:
            if DBHelp.FachBelegt("SeminarProfil", 3):
                block1.remove("SeminarProfil")
        if DBHelp.pruefe_halbjahr_angegeben(1) == False:
            block1.append("Englisch")
            block1.append("Spanisch")
        if DBHelp.FachBelegt("Englisch", 1) == True and DBHelp.FachBelegt("Englisch", 3) == True:                     #Noah schau, mal db sachen
            self.pr3.append("Englisch")
        if DBHelp.FachBelegt("SpanischN", 1) == True or DBHelp.FachBelegt("SpanischF", 1) == True:      #Letzter ich schwöre
            block1.append("Spanisch")
        if self.pr2 == "Deutsch" or self.pr3 == "Deutsch":
            block1.remove("Deutsch")
        if self.pr3 == "Englisch":
            block1.remove("Englisch")
        if self.pr3 == "Spanisch":
            block1.remove("Spanisch")
        if self.pr4 == "GGK":
            block1.remove("GGK")
        if self.pr4 == "Wirtschaft":
            block1.remove("Wirtschaft")
        
        if self.FachblockPR4 == 1:
            return block1
        elif self.FachblockPR4 == 2:
            return block2
        elif self.FachblockPR4 == 3:
            return block3
        elif self.FachblockPR4 == 4:
            return block4
        else:
            return block1 + block2 + block3 + block4
        