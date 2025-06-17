from dbhelp import *
from bewertung import *

class NotenschnnittBerechnen(object):
    def __init__(self):
        self.HJG = Halbjahrgetten()                             # type: ignore #Keine ahnung warum er sagt fehler / was type: ignore???
        self.schnitt = 0
        self.Halbjahr = []
        self.FaecherNoten = []

    def setHalbjahr(self):
        self.Halbjahr.append(self.HJG.PossibleToGesucht())      #Felix es brauch die gewünschte jahr

    def setFaecherNoten(self):
        pass                                                    #self.FaecherNoten = ->alle fächer mit den gesamtNoten aus dem halbjahr: self.Halbjahr(Array)

    def setSchnitt(self):
        a = len(self.FaecherNoten)
        counter = 0
        for i in range (0, a):
            counter += i
        self.schnitt = counter / a
        