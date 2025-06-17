from dbhelp import *
from bestanden import *

class FaecherRausstreichen(object):
    def __init__(self, a):                      #a ist ein Array, das die fächer die er rausstreichen  möchte beinhaltet. im Array stehen: Alles von dem Fach (um die daten zu haben, falls der Try falsch ist)
        self.Tryfaecher = a 
        self.spanischbelegt = DBHelp.coutFachBelegt('SpanischN')
        if self.Streichen() == False or Bestanden.AbiJahreBestanden() == False:
            for i in self.Tryfaecher:
                DBHelp.setBelegt(i(1), i(2), True)
            return False
        return True

    def Streichen(self):
        pruefungfaecher = DBHelp.getpruefungsfacher()   #return ist ein eindimensionales Array das die fachnamen der pruefungsfaecher beinhaltet
        for i in self.Tryfaecher:
            for u in pruefungfaecher:
                if i(2) == u:
                    return False
            if i(2) == ('Deutsch' or 'Mathe' or 'GGK' or 'Physik' or 'Chemie') or i(3) == 'Profil' or DBHelp.coutFachBelegt('Informatik') < 2:     #i(3) soll Fachtype sein #in hj 3,4,5,6
                return False
            DBHelp.setBelegt(i(1), i(2), False)       #i(1) soll halpjahr und i(2) das fach sein
        return True