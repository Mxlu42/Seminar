from pymongo import MongoClient
import os
import bson

class DBHelp(object):
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["test"]
        self.students = self.db["students"]
        self.current_user_id = None

        # Lade zuletzt gespeicherte User-ID aus Datei
        try:
            with open("current_user_id.txt", "r") as f:
                oid = f.read().strip()
                if oid:
                    self.current_user_id = bson.ObjectId(oid)
        except Exception:
            pass

    def login(self, name, vorname, passwort):
        user = self.students.find_one({"name": name, "vorname": vorname, "passwort": passwort})
        if user:
            self.current_user_id = user["_id"]
            with open("current_user_id.txt", "w") as f:
                f.write(str(user["_id"]))
            return True
        return False

    def setzeMehrereFaecherBelegtTrue(self, faecher: list[str], jahrgänge: list[int]) -> list[str]:
        # 1) Flatten aller Eingaben
        clean = []
        for x in faecher:
            if isinstance(x, (tuple, list)):
                clean.extend([y for y in x if isinstance(y, str)])
            elif isinstance(x, str):
                clean.append(x)
        faecher = clean

        # 2) Map Fachname → FachArt
        fach_zu_art = {}
        for eintrag in faecher:
            parts = eintrag.strip().split(maxsplit=1)
            fach_zu_art[parts[0]] = parts[1] if len(parts) > 1 else None

        partner_map = {"Mathe": "Deutsch", "Deutsch": "Mathe"}

        # 3) Schüler laden
        student = self.students.find_one({"_id": self.current_user_id})
        if not student:
            print("❌ Kein Student mit current_user_id gefunden.")
            return []

        # 4) Halbjahre durchgehen und Fächer updaten
        updated_halbjahre = []
        for halb in student["halbjahre"]:
            jahr = halb["jahr"]
            if jahr not in jahrgänge:
                updated_halbjahre.append(halb)
                continue

            for fach in halb["normal_faecher"]:
                name = fach["fach"]
                if name in fach_zu_art:
                    # ausgewähltes Fach immer belegen
                    fach["belegt"] = "true"
                    art = fach_zu_art[name]
                    if art:
                        fach["fachArt"] = art

                    # Partner-Logik: kein neues Element, sondern nur anpassen
                    partner = partner_map.get(name)
                    if partner and art and art.lower() in ("ean", "gan"):
                        # komplementäre FachArt
                        comp = "gAn" if art.lower() == "ean" else "eAn"
                        # vorhandenes Partner‐Objekt suchen
                        p_obj = next((f for f in halb["normal_faecher"] if f["fach"] == partner), None)
                        if p_obj:
                            p_obj["belegt"] = "true"
                            p_obj["fachArt"] = comp
                else:
                    # nicht ausgewähltes Fach zurücksetzen
                    fach["belegt"] = "false"
                    fach["fachArt"] = ""

            updated_halbjahre.append(halb)

        # 5) In DB zurückschreiben
        res = self.students.update_one(
            {"_id": self.current_user_id},
            {"$set": {"halbjahre": updated_halbjahre}}
        )
        if res.modified_count:
            print(f"✅ {res.modified_count} Halbjahre aktualisiert.")
        else:
            print("⚠️ WARNUNG: Keine Änderungen!")

        # 6) Rückgabe aller aktuell belegt=true Fächer
        return self.getAlleBelegtenFaechern(jahrgänge)


    def getAlleBelegtenFaechern(self, jahrgaenge: list[int] | None = None) -> list[str]:
        student = self.students.find_one({"_id": self.current_user_id})
        if not student:
            return []
        faecher = set()
        for halb in student.get("halbjahre", []):
            if jahrgaenge is None or halb.get("jahr") in jahrgaenge:
                for fach in halb.get("normal_faecher", []):
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
    
    def FachBelegt(self, fachname, halbjahr_seartch, state):
        student = self.students.find_one({"_id": self.current_user_id})
        if not student:
            return False

        for halbjahr in student.get("halbjahre", []):
            if halbjahr["jahr"] == halbjahr_seartch:
                for fach in halbjahr["normal_faecher"]:
                    if fach["fach"] == fachname:
                        return fach["belegt"] == state
        return False

    def checkobpwkorrekt(self, arr):
        user = self.students.find_one({"name": arr[0],'vorname': arr[1] ,"passwort": arr[2]})
        if user:
            self.current_user_id = user['_id']
            return True
        return False
    
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

    def setFachart_by_Fach_and_year(self, fachname: str, halbjahre_liste: list[int], neue_fachart: str) -> int:
        total_modified = 0
        for jahr in halbjahre_liste:
            res = self.students.update_one(
                {"_id": self.current_user_id, 
                "halbjahre.jahr": jahr,
                "halbjahre.normal_faecher.fach": fachname},
                {"$set": {
                    "halbjahre.$[h].normal_faecher.$[f].fachArt": neue_fachart,
                    "halbjahre.$[h].normal_faecher.$[f].belegt": "true"
                }},
                array_filters=[
                    {"h.jahr": jahr},
                    {"f.fach": fachname}
                ]
            )
            total_modified += res.modified_count
        print(f"✅ setFachart_by_Fach_and_year geändert in {total_modified} Dokument(en).")
        return total_modified

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

        student = self.students.find_one({"_id": self.current_user_id})

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
    
    def countFachBelegt(self, fachname):
        count = 0
        relevante_jahre = ["3", "4", "5", "6"]

        student = self.students.find_one({"_id": self.current_user_id})

        for halbjahr in student.get("halbjahre", []):
            if halbjahr.get("jahr") in relevante_jahre:
                for fach in halbjahr.get("normal_faecher", []):
                    if fach.get("fach") == fachname:
                        count += 1
                        break  # Nur einmal pro Halbjahr zählen

        return count

    def istJahrgangVollständigAngegeben(self, jahrgang_werte: list[int]) -> bool:
        if not self.current_user_id:
            print("❌ Kein eingeloggter Student vorhanden.")
            return False

        student = self.students.find_one({"_id": self.current_user_id})
        if not student:
            print(f"❌ Student mit ID {self.current_user_id} nicht gefunden.")
            return False

        jahr_status = {jahr: False for jahr in jahrgang_werte}

        for halbjahr in student.get("halbjahre", []):
            jahr = halbjahr.get("jahr")
            angegeben = halbjahr.get("angegeben")
            if jahr in jahrgang_werte and str(angegeben).lower() == "true":
                jahr_status[jahr] = True

        if all(jahr_status.values()):
            print(f"✅ Schüler mit ID {self.current_user_id} hat alle Jahrgänge {jahrgang_werte} vollständig angegeben.")
            return True
        else:
            print(f"❌ Schüler mit ID {self.current_user_id} hat nicht alle Jahrgänge {jahrgang_werte} angegeben: {jahr_status}")
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

    def set_gesamtnote_by_array(self, fachnoten: list[tuple[str]], halbjahr: str) -> int:
        """
        Für den eingeloggten Schüler: Setzt die ‚gesamt‘-Note für jedes Fach in fachnoten
        im angegebenen Halbjahr. fachnoten ist eine Liste von (fachname, gesamtnote).
        Gibt die Anzahl der tatsächlich modifizierten Fächer zurück.
        """
        total_modified = 0

        for fachname, gesamtnote in fachnoten:
            res = self.students.update_one(
                {
                    "_id": self.current_user_id,
                    "halbjahre.jahr": halbjahr,
                    "halbjahre.normal_faecher.fach": fachname
                },
                {
                    "$set": {
                        # Wir nutzen zwei Array-Filters: eins für Halbjahr, eins für Fach,
                        # und eins für das Note-Array-Element mit type=="gesamt"
                        "halbjahre.$[h].normal_faecher.$[f].note.$[n].Wert": gesamtnote
                    }
                },
                array_filters=[
                    {"h.jahr": halbjahr},
                    {"f.fach": fachname},
                    {"n.type": "gesamt"}
                ]
            )
            if res.modified_count:
                print(f"✅ {fachname}: gesamtnote auf {gesamtnote} gesetzt.")
            else:
                print(f"⚠️ {fachname}: Note nicht gesetzt (vielleicht Fach nicht belegt oder kein 'gesamt'-Eintrag).")
            total_modified += res.modified_count

        print(f"🎯 Insgesamt geändert: {total_modified} Fächer im Halbjahr {halbjahr}.")
        return total_modified

    def getAlleGesamtNotenAusHalbjahr(self, halbjahr: int) -> dict[str, any]:
            """
            Liefert für den eingeloggten Schüler alle 'gesamt'-Noten
            im angegebenen Halbjahr zurück als {fachname: gesamtnote}.
            """
            # 1) Schüler laden
            student = self.students.find_one({"_id": self.current_user_id})
            if not student:
                print("❌ Kein eingeloggter Student.")
                return {}

            # 2) Ergebnis-Container
            gesamt_noten: dict[str, any] = {}

            # 3) Gewünschtes Halbjahr suchen
            for hj in student.get("halbjahre", []):
                if hj.get("jahr") == halbjahr:
                    # 4) Jedes Fach durchgehen und die 'gesamt'-Note extrahieren
                    for fach in hj.get("normal_faecher", []):
                        fachname = fach.get("fach")
                        for note in fach.get("note", []):
                            if note.get("type") == "gesamt":
                                gesamt_noten[fachname] = note.get("Wert")
                                break
                    break  # nachdem wir das richtige Halbjahr gefunden haben

            print(f"ℹ️ Gesamt-Noten Halbjahr {halbjahr}: {gesamt_noten}")
            return gesamt_noten