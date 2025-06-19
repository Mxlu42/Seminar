from dbhelp import *
from bestanden import *

class FaecherRausstreichen(object):
    def __init__(self, a):                      #a ist ein Array, das die fächer die er rausstreichen  möchte beinhaltet. im Array stehen: Alles von dem Fach (um die daten zu haben, falls der Try falsch ist)
        bestanden = Bestanden()
        self.db = DBHelp()
        self.Tryfaecher = a 
        self.spanischbelegt = self.db.countFachBelegt('SpanischN')
        if self.Streichen() == False or bestanden.AbiBestanden() == False:
            for i in self.Tryfaecher:
                self.db.FachBelegt(i(1), i(2), 'true')
            return False
        return True

    def Streichen(self):
        pruefungfaecher = self.db.getArrayPruefungsfaecher()   #return ist ein eindimensionales Array das die fachnamen der pruefungsfaecher beinhaltet
        for i in self.Tryfaecher:
            for u in pruefungfaecher:
                if i(0) == u:
                    return False
            if i(0) == ('Deutsch' or 'Mathe' or 'GGK' or 'Physik' or 'Chemie') or i(3) == 'Profil' or self.db.coutFachBelegt('Informatik') < 2:     #i(3) soll Fachtype sein #in hj 3,4,5,6
                return False
            self.db.FachBelegt(i(1), i(0), 'false')       #i(1) soll halpjahr und i(0) das fach sein
        return True