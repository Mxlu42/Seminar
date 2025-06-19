from pymongo import MongoClient
import os
from bson import ObjectId

class DBHelp(object):
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["test"]
        self.students = self.db["students"]
        
        # Versuche current_user_id aus Datei zu laden
        self.current_user_id = None
        try:
            if os.path.exists("current_user_id.txt"):
                with open("current_user_id.txt", "r") as f:
                    self.current_user_id = ObjectId(f.read().strip())
        except Exception as e:
            print("Fehler beim Laden von current_user_id:", e)

    def login(self, name, vorname, passwort):
        user = self.students.find_one({"name": name, "vorname": vorname, "passwort": passwort})
        if user:
            self.current_user_id = user['_id']
            return True
        return False

    def checkobpwkorrekt(self, arr):
        user = self.students.find_one({"name": arr[0],'vorname': arr[1] ,"passwort": arr[2]})
        if user:
            self.current_user_id = user['_id']
            return True
        return False

    def FachBelegt(self, fachname, halbjahr_seartch):
        student = self.students.find_one({"_id": self.current_user_id})
        if not student:
            return False

        for halbjahr in student.get("halbjahre", []):
            if halbjahr["jahr"] == halbjahr_seartch:
                for fach in halbjahr["normal_faecher"]:
                    if fach["fach"] == fachname:
                        return fach["belegt"] == "true"
        return False

    def setzeMehrereFaecherBelegtTrue(self, faecher: list[str], jahrgänge: list[int]) -> list[str]:
        clean = []
        for x in faecher:
            if isinstance(x, (tuple, list)):
                clean += [y for y in x if isinstance(y, str)]
            elif isinstance(x, str):
                clean.append(x)
        faecher = clean

        fach_zu_art = {}
        for eintrag in faecher:
            parts = eintrag.strip().split(maxsplit=1)
            fachname = parts[0]
            fachart = parts[1] if len(parts) > 1 else None
            fach_zu_art[fachname] = fachart

        partner_map = {"Mathe": "Deutsch", "Deutsch": "Mathe"}

        student = self.students.find_one({"_id": self.current_user_id})
        if not student:
            print("❌ Kein Student mit current_user_id gefunden.")
            return []

        original_halbjahre = student.get("halbjahre", [])
        halbjahre_neu = []

        for halbjahr in original_halbjahre:
            jahr = halbjahr.get("jahr")
            if jahr not in jahrgänge:
                halbjahre_neu.append(halbjahr)
                continue

            neue_faecher = []
            for fach in halbjahr.get("normal_faecher", []):
                name = fach.get("fach")
                if name not in fach_zu_art:
                    fach["belegt"] = "false"
                    fach["fachArt"] = ""
                else:
                    fach["belegt"] = "true"
                    art = fach_zu_art[name]
                    if art:
                        fach["fachArt"] = art

                    partner = partner_map.get(name)
                    if partner and art and art.lower() in ("ean", "gan"):
                        comp = "gAn" if art.lower() == "ean" else "eAn"
                        schon_drin = any(f.get("fach") == partner for f in neue_faecher)
                        if not schon_drin:
                            neue_faecher.append({"fach": partner, "belegt": "true", "fachArt": comp})


                neue_faecher.append(fach)

            halbjahr["normal_faecher"] = neue_faecher
            halbjahre_neu.append(halbjahr)

        result = self.students.update_one(
            {"_id": self.current_user_id},
            {"$set": {"halbjahre": halbjahre_neu}}
        )

        if result.modified_count == 0:
            print("⚠️ WARNUNG: Keine Änderungen vorgenommen!")
        else:
            print(f"✅ {result.modified_count} Datensätze geändert.")

        return self.getAlleBelegtenFaechern(jahrgänge)

    def getAlleBelegtenFaechern(self, jahrgaenge: list[int] | None = None) -> list[str]:
        student = self.students.find_one({"_id": self.current_user_id})
        if not student:
            return []

        faecher = set()
        for halbjahr in student.get("halbjahre", []):
            if jahrgaenge is None or halbjahr.get("jahr") in jahrgaenge:
                for fach in halbjahr.get("normal_faecher", []):
                    if fach.get("belegt") == "true":
                        faecher.add(fach.get("fach"))
        return sorted(faecher)

    def setzeJahrgängeAngegeben(self, jahrgänge: list[int]):            #ae
        student = self.students.find_one({"_id": self.current_user_id})
        if not student:
            return

        changed = False
        for halbjahr in student.get("halbjahre", []):
            if halbjahr.get("jahr") in jahrgänge and str(halbjahr.get("angegeben")).lower() != "true":
                halbjahr["angegeben"] = "true"
                changed = True

        if changed:
            self.students.update_one({"_id": self.current_user_id}, {"$set": {"halbjahre": student["halbjahre"]}})

    def get_noten_faecher(self, faecher: list[str], jahrgaenge: list[int]) -> dict[int, list[dict[str, any]]]:
        student = self.students.find_one({"_id": self.current_user_id})
        if not student:
            return {}

        result = {jahr: [] for jahr in jahrgaenge}
        for halbjahr in student.get("halbjahre", []):
            jahr = halbjahr.get("jahr")
            if jahr in jahrgaenge:
                for fach in halbjahr.get("normal_faecher", []):
                    if fach.get("fach") in faecher and fach.get("belegt") == "true":
                        gesamtnote = None
                        for n in fach.get("note", []):
                            if n.get("type") == "gesamt":
                                gesamtnote = n.get("Wert")
                        result[jahr].append({"fach": fach.get("fach"), "gesamtnote": gesamtnote})
        return result

    def get_faecher_by_fachart(self, fachart_suche):
        student = self.students.find_one({"_id": self.current_user_id})
        if not student:
            return []

        gefundene_faecher = []
        for halbjahr in student.get("halbjahre", []):
            for fach in halbjahr.get("normal_faecher", []):
                if fach.get("fachArt") == fachart_suche:
                    gefundene_faecher.append(fach.get("fach"))
        return gefundene_faecher

    def setFachart_by_Fach_and_year(self, fachname, halbjahre_liste, neue_fachart):
        students_list = self.students.find()  # Alle Schüler holen

        for student in students_list:
            aktualisiert = False  # Flag, um Update nur bei Änderung zu machen

            for halbjahr in student.get("halbjahre", []):
                if halbjahr.get("jahr") in [str(hj) for hj in halbjahre_liste]:
                    for fach in halbjahr.get("normal_faecher", []):
                        if fach.get("fach") == fachname:
                            if fach.get("fachArt") != neue_fachart:
                                fach["fachArt"] = neue_fachart
                                aktualisiert = True

            if aktualisiert:
                self.students.update_one(
                    {"_id": student["_id"]},  # Filter nach ID
                    {"$set": {"halbjahre": student["halbjahre"]}}  # Neues Feld schreiben
                )

    def pruefe_halbjahr_angegeben(self, jahr):
        student = self.students.find_one({"_id": self.current_user_id})
        if not student:
            return False

        for halbjahr in student.get("halbjahre", []):
            if halbjahr.get("jahr") == jahr and str(halbjahr.get("angegeben")).lower() == "true":
                return True
        return False
    
    def getArrayPruefungsfaecher(self):
        pruefungs_array = []

        student = self.current_user_id() # Der eingeloggte Benutzer

        for halbjahr in student.get("halbjahre", []):
            if halbjahr.get("jahr") == "7":
                for fach in halbjahr.get("pruefungsfaecher", []):
                    eintrag = [
                        fach.get("fach"),
                        fach.get("PruefungsfachNr"),
                        fach.get("note")
                    ]
                    pruefungs_array.append(eintrag)
                break

        return pruefungs_array

    def istJahrgangVollständigAngegeben(self, jahrgang_werte: list[int]):
            results = self.students.find()
            for student in results:
                jahr_status = {jahr: False for jahr in jahrgang_werte}

                for halbjahr in student.get("halbjahre", []):
                    jahr = halbjahr.get("jahr")
                    angegeben = halbjahr.get("angegeben")

                    if jahr in jahrgang_werte and str(angegeben).lower() == "true":
                        jahr_status[jahr] = True

                if all(jahr_status.values()):
                    print(f"✅ Jahrgang mit Jahren {jahrgang_werte} ist vollständig angegeben.")
                    return True

            print(f"❌ Jahrgang mit Jahren {jahrgang_werte} ist NICHT vollständig angegeben.")
            return False

    def getArrayAusHalpjahrMitFachFachartGesamtnote(self, gesuchtesHJ):
            ergebnis = []
            results = self.students.find()

            for student in results:
                for halbjahr in student.get("halbjahre", []):
                    if halbjahr.get("name") == gesuchtesHJ:
                        for fach in halbjahr.get("normal_faecher", []):
                            if fach.get("belegt") == "true":
                                ergebnis.append({
                                    "fach": fach.get("fach", ""),
                                    "fachart": fach.get("fachart", ""),
                                    "gesamtnote": fach.get("note", "")
                                })
            return ergebnis

    def getArrayAusAllenFaechernAndFaechertypseAndGesamtnoteInBestimmtemHalbJahr(self, halbjahr_name):      #Fach, Fachart, note
            ergebnis = []
            results = self.students.find()

            for student in results:
                for halbjahr in student.get("halbjahre", []):
                    if halbjahr.get("name") == halbjahr_name:
                        for fach in halbjahr.get("normal_faecher", []):
                            if fach.get("belegt") == "true":
                                ergebnis.append({
                                    "fach": fach.get("fach", ""),
                                    "fachart": fach.get("fachart", ""),
                                    "gesamtnote": fach.get("note", "")
                                })
            return ergebnis

    def getFaecherMitNoten1213(self):
        student = self.students.find_one({"_id": self.current_user_id})
        if not student:
            return [[], []]

        faecher_noten = [[], []]
        for halbjahr in student.get("halbjahre", []):
            jahr = halbjahr.get("jahr")
            if jahr in [1, 2]:
                index = jahr - 1
                for fach in halbjahr.get("normal_faecher", []):
                    if fach.get("belegt") == "true":
                        gesamtnote = None
                        for eintrag in fach.get("note", []):
                            if eintrag.get("type") == "gesamt":
                                gesamtnote = eintrag.get("Wert")
                        faecher_noten[index].append([fach.get("fach"), gesamtnote])
        return faecher_noten
