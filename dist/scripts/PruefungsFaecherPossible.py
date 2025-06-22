from pymongo import MongoClient
from dbhelp import *

class PruefungsfaecherPossible(object):
    def __init__(self):
        # Default-Werte
        self.a = None
        self.aState = False

        self.db = DBHelp()
        # Fach a ermitteln
        if self.db.pruefe_halbjahr_angegeben(1):
            if self.db.FachBelegt("Evangelisch", 1) and self.db.FachBelegt("Evangelisch", 3):
                self.a, self.aState = "Evangelisch", True
            elif self.db.FachBelegt("Katholisch", 1) and self.db.FachBelegt("Katholisch", 3):
                self.a, self.aState = "Katholisch", True
            elif self.db.FachBelegt("Ethik", 1) and self.db.FachBelegt("Ethik", 3):
                self.a, self.aState = "Ethik", True
            else:
                self.a, self.aState = "Ethik", True
        else:
            self.a, self.aState = "Ethik", True

        # Prüfungsfach-Optionen laden
        self.pr1 = self._unique(self.db.get_faecher_by_fachart("profil"))
        self.pr2 = self._unique(self.db.get_faecher_by_fachart("eAn"))
        self.FachblockPR2 = self.setFachblockPR2()

        self.pr3 = None
        self.prp3 = self._unique(self.setPruefungsfachDrei())
        self.FachblockPR3 = 0

        self.pr4 = None
        self.prp4 = self._unique(self.setPruefungsfachVier())
        self.FachblockPR4 = 0

        self.pr5 = None
        self.prp5 = self._unique(self.setPruefungsfachFuenf())
        self.FachblockPR5 = 0

    def _unique(self, seq):
        """Hilfsfunktion: erhält Reihenfolge und entfernt Duplikate"""
        return list(dict.fromkeys(seq))

    # Setter-Methoden
    def setPF2(self, fach):
        self.pr2 = fach
    def setPF3(self, fach):
        self.pr3 = fach
    def setPF4(self, fach):
        self.pr4 = fach
    def setPF5(self, fach):
        self.pr5 = fach

    # Getter-Methoden mit Fallback
    def getPFP1(self):
        if not self.pr1:
            return self._unique(self.setPrufungsfachEins())
        return self.pr1

    def getPFP2(self):
        if not self.pr2:
            return self._unique(self.setPrufungsfachZwei())
        return [self.pr2] if isinstance(self.pr2, str) else self.pr2

    def getPFP3(self):
        return self._unique(self.setPruefungsfachDrei())

    def getPFP4(self):
        return self._unique(self.setPruefungsfachVier())

    def getPFP5(self):
        return self._unique(self.setPruefungsfachFuenf())

    # Block-Logik
    def setFachblockPR2(self):
        return 1 if self.pr2 == "Mathe" else 2

    def setFachblockPR3(self):
        if self.FachblockPR2 == 1 and self.pr3 == "Deutsch":
            return 1
        if self.FachblockPR2 == 1 and self.pr3 in ("Englisch", "SpanischN"):
            return 2
        if self.FachblockPR2 == 2 and self.pr3 == "Mathe":
            return 3
        if self.FachblockPR2 == 2 and self.pr3 in ("Englisch", "SpanischN"):
            return 4
        return None

    def setFachblockPR4(self):
        # Komplexe Bedingungen, ggf. anpassen
        if ((self.FachblockPR2 == 1 and self.FachblockPR3 in (1,2)) or
            (self.FachblockPR2 == 2 and self.FachblockPR3 == 3)) and \
           self.pr4 in ("GGK", self.a, "Wirtschaft"):
            return 1
        if ((self.FachblockPR2 == 1 and self.FachblockPR3 == 1 and self.pr4 in ("Chemie","Physik","Englisch","SpanischN")) or
            (self.FachblockPR3 == 2 and self.pr3 == "Englisch" and self.pr4 in ("Chemie","Physik","Deutsch","SpanischN")) or
            (self.FachblockPR3 == 3 and self.pr4 in ("Chemie","Physik","Englisch","SpanischN"))):
            return 2
        if self.FachblockPR2 == 1 and self.FachblockPR3 == 4 and self.pr4 in ("GGK", self.a, "Wirtschaft"):
            return 3
        if self.FachblockPR2 == 1 and self.FachblockPR3 == 4 and self.pr4 in ("Chemie","Physik","Mathe"):
            return 4
        return None

    def setFachblockPR5(self):
        return self.FachblockPR4

    # Statische Prüfungsfach-Definitionen
    def setPrufungsfachEins(self):
        return ["Informationstechnik", "Mechatronik", "Gestaltung_Medien"]

    def setPrufungsfachZwei(self):
        return ["Mathe", "Deutsch"]

    def setPruefungsfachDrei(self):
        self.FachblockPR2 = self.setFachblockPR2()
        block = []
        if self.FachblockPR2 == 1:
            block.append("Deutsch")
            if not self.db.pruefe_halbjahr_angegeben(1):
                block.extend(["Englisch","SpanischN"])
            if self.db.FachBelegt("Englisch",1) and self.db.FachBelegt("Englisch",3):
                block.append("Englisch")
            if self.db.FachBelegt("SpanischN",1):
                block.append("SpanischN")
        else:
            block.append("Mathe")
            if not self.db.pruefe_halbjahr_angegeben(1):
                block.extend(["Englisch","SpanischN"])
            if self.db.FachBelegt("Englisch",1) and self.db.FachBelegt("Englisch",3):
                block.append("Englisch")
            if self.db.FachBelegt("SpanischN",1):
                block.append("SpanischN")
        return block

    def setPruefungsfachVier(self):
        self.FachblockPR3 = self.setFachblockPR3()
        block1 = ["GGK", self.a, "Wirtschaft"]
        block2 = ["Chemie","Physik","Deutsch"]
        if not self.db.pruefe_halbjahr_angegeben(1):
            block2.extend(["Englisch","Spanisch"])
        if self.db.FachBelegt("Englisch",1) and self.db.FachBelegt("Englisch",3):
            block1.append("Englisch")
        if self.db.FachBelegt("SpanischN",1):
            block2.append("Spanisch")
        # Entfernen bereits gewählter Fächer
        for f in (self.pr3,):
            if f in block2:
                block2.remove(f)
        if self.FachblockPR2 == 2 and "Deutsch" in block2:
            block2.remove("Deutsch")
        # Zusammenführen
        if self.FachblockPR3 in (1,2,3):
            return block1 + block2
        return block1 + ["Chemie","Physik","Mathe"]

    def setPruefungsfachFuenf(self):
        self.FachblockPR4 = self.setFachblockPR4()
        block1 = ["SeminarGGK","SeminarProfil","GGK","Wirtschaft","Chemie","Physik","Informatik","Deutsch","Sport"]
        block2 = ["GGK","Wirtschaft","SeminarGGK"]
        block3 = ["Chemie","Physik","Mathe"]
        # a-Fach hinzufügen
        if self.aState:
            block1.append(self.a)
            block2.append(self.a)
            if self.pr4 == self.a and self.a in block1:
                block1.remove(self.a)
        # Halbjahr-Checks
        if not self.db.pruefe_halbjahr_angegeben(3) and self.db.FachBelegt("SeminarProfil",3):
            block1.remove("SeminarProfil")
        if not self.db.pruefe_halbjahr_angegeben(1):
            block1.extend(["Englisch","Spanisch"])
        elif self.db.FachBelegt("Englisch",1) and self.db.FachBelegt("Englisch",3):
            block1.append("Englisch")
        if self.db.FachBelegt("SpanischN",1) or self.db.FachBelegt("SpanischF",1):
            block1.append("Spanisch")
        # Entfernen bereits gewählter Fächer
        for f in (self.pr2, self.pr3, self.pr4):
            if f in block1:
                block1.remove(f)
        # Auswahl nach Block
        if self.FachblockPR4 == 1:
            return block1
        if self.FachblockPR4 == 2:
            return block2
        if self.FachblockPR4 == 3:
            return block3
        if self.FachblockPR4 == 4:
            return block2
        return block1 + block2 + block3
