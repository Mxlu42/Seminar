#from dbhelp import *


class Halbjahrgetten(object):
    def __init__(self):
        self.possEingabe = ["11.1", "11.2", "12.1", "12.2", "13.1", "13.2", "11", "12", "13", "12 + 13.1", "12 + 13", "Prüfungen"]
        self.uebersetztEingabe = [1, 2, 3, 4, 5, 6, [1, 2], [3, 4], [5, 6], [3, 4, 5], [3, 4, 5, 6], 7]
        self.gesuchtesHalbjahr = None

    def setGesuchtesHalbjahr(self, a):
        self.gesuchtesHalbjahr = self.PossibleToGesucht(a)       #aus felix code
    
    def getGesuchtesHalbjahr(self):
        return self.gesuchtesHalbjahr

    def getPossibleEingabe(self):
        return self.possEingabe
    
    def PossibleToGesucht(self, gewuenscht):
        for i in range (0, 12):
            if self.possEingabe(i) == gewuenscht:
                return self.uebersetztEingabe(i)
            
class noteEingeben(object):
    def __init__(self, fach, HJ, Note, Notentype):
        self.fach = fach
        self.HJ = HJ
        self.Note = Note
        self.Notentype = Notentype
        DBhelp.setNoteInDB(self.fach, self.HJ, self.Note, self.Notentype)
    
