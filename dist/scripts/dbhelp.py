from pymongo import MongoClient

class DBHelp(object):
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["test"]
        self.students = self.db["students"]

    def FachBelegt(self, fachname, halbjahr_seartch):
        # Suche nur Schüler, die das Fach irgendwo belegt haben
        results = self.students.find({
            "halbjahre.normal_faecher.fach": fachname
        })

        for student in results:
            print(f"\n{student['name']} - {student['vorname']}")

            for halbjahr in student["halbjahre"]:
                if halbjahr["name"] == halbjahr_seartch:
                    for fach in halbjahr["normal_faecher"]:
                        if fach["fach"] == fachname:
                            status = fach["belegt"]
                            if status == "true":
                                return True
                            else:
                                return False
                            
    def setzeMehrereFaecherBelegtTrue(self, faecher: list[str], jahrgänge: list[int]) -> list[str]:
        """
        1) Setzt in den angegebenen Jahrgängen zunächst alle Fächer auf belegt = "false".
        2) Setzt dann alle gewählten Fächer (plus Partnerfach Mathe↔Deutsch) auf belegt = "true".
        3) Liefert eine Liste ALLER Fächer zurück, die am Ende in diesen Jahrgängen belegt = "true" sind.
        """
        # 1) Flatten aller Listen/Tupel
        clean = []
        for x in faecher:
            if isinstance(x, (tuple, list)):
                clean += [y for y in x if isinstance(y, str)]
            elif isinstance(x, str):
                clean.append(x)
        faecher = clean

        partner_map = {"Mathe": "Deutsch", "Deutsch": "Mathe"}

        # A) Alle nicht-gewählten Fächer auf false setzen
        for jahr in jahrgänge:
            self.students.update_many(
                {"halbjahre.jahr": jahr},
                {"$set": {"halbjahre.$[h].normal_faecher.$[f].belegt": "false"}},
                array_filters=[
                    {"h.jahr": jahr},
                    {"f.fach": {"$nin": faecher}}
                ]
            )

        # B) Gewählte Fächer (und Partner) auf true setzen
        for fach_input in faecher:
            parts    = fach_input.strip().split(maxsplit=1)
            fachname = parts[0]
            fachart  = parts[1] if len(parts) > 1 else None

            for jahr in jahrgänge:
                # direktes Fach
                update_spec = {"halbjahre.$[h].normal_faecher.$[f].belegt": "true"}
                if fachart:
                    update_spec["halbjahre.$[h].normal_faecher.$[f].fachArt"] = fachart

                self.students.update_many(
                    {"halbjahre.jahr": jahr, "halbjahre.normal_faecher.fach": fachname},
                    {"$set": update_spec},
                    array_filters=[{"h.jahr": jahr}, {"f.fach": fachname}]
                )

                # Partnerfach Mathe↔Deutsch, komplementäres eAn↔gAn
                partner = partner_map.get(fachname)
                if partner and fachart and fachart.lower() in ("ean", "gan"):
                    comp = "gAn" if fachart.lower() == "ean" else "eAn"
                    self.students.update_many(
                        {"halbjahre.jahr": jahr, "halbjahre.normal_faecher.fach": partner},
                        {"$set": {
                            "halbjahre.$[h].normal_faecher.$[p].belegt": "true",
                            "halbjahre.$[h].normal_faecher.$[p].fachArt": comp
                        }},
                        array_filters=[{"h.jahr": jahr}, {"p.fach": partner}]
                    )

        # C) Aggregation: sammle alle Fächer, die jetzt belegt = "true" sind
        pipeline = [
            {"$unwind": "$halbjahre"},
            {"$match":   {"halbjahre.jahr": {"$in": jahrgänge}}},
            {"$unwind": "$halbjahre.normal_faecher"},
            {"$match":   {"halbjahre.normal_faecher.belegt": "true"}},
            {"$group":   {"_id": "$halbjahre.normal_faecher.fach"}},
            {"$sort":    {"_id": 1}}
        ]
        cursor = self.students.aggregate(pipeline)
        final_true = [doc["_id"] for doc in cursor]

        print("✅ Am Ende belegt=true in Jahren", jahrgänge, ":", final_true)
        return final_true


    def setzeJahrgängeAngegeben(self, jahrgänge: list[int]):

        results = self.students.find()

        for student in results:
            schueler_id = student['_id']
            updated_halbjahre = student.get("halbjahre", [])
            changed = False

            for halbjahr in updated_halbjahre:
                if halbjahr.get("jahr") in jahrgänge and str(halbjahr.get("angegeben")).lower() != "true":
                    halbjahr["angegeben"] = "true"
                    changed = True

            if changed:
                self.students.update_one(
                    {"_id": schueler_id},
                    {"$set": {"halbjahre": updated_halbjahre}}
                )
                print(f"✅ 'angegeben = true' gesetzt für Schüler {student.get('name')} in Jahrgänge {jahrgänge}")

    def get_noten_faecher(self, faecher: list[str], jahrgaenge: list[int]) -> dict[int, list[dict[str, any]]]:
        # 1) Flattening aller Tupel/List-Eingaben
        clean = []
        for x in faecher:
            if isinstance(x, (tuple, list)):
                clean += [y for y in x if isinstance(y, str)]
            elif isinstance(x, str):
                clean.append(x)
        faecher = clean

        result: dict[int, list[dict[str, any]]] = {}

        for jahr in jahrgaenge:
            result[jahr] = []
            # Suche alle Schüler, die dieses Halbjahr haben
            cursor = self.students.find({"halbjahre.jahr": jahr})
            for student in cursor:
                for halb in student.get("halbjahre", []):
                    if halb.get("jahr") != jahr:
                        continue
                    for fach in halb.get("normal_faecher", []):
                        if fach.get("fach") in faecher and fach.get("belegt") == "true":
                            # suche die Note vom Typ "gesamt"
                            gesamtnote = None
                            for n in fach.get("note", []):
                                if n.get("type") == "gesamt":
                                    gesamtnote = n.get("Wert")
                                    break
                            result[jahr].append({
                                "fach": fach.get("fach"),
                                "gesamtnote": gesamtnote
                            })
            # Optional: Duplikate entfernen, falls mehrere Schüler gleiches Fach haben
            # result[jahr] = [dict(t) for t in {tuple(d.items()) for d in result[jahr]}]

        # Debug-Ausgabe
        for jahr, arr in result.items():
            print(f"🏷 Halbjahr {jahr}:")
            for entry in arr:
                print(f"  • {entry['fach']}: {entry['gesamtnote']}")
        return result


    def get_faecher_by_fachart(self, fachart_suche):
        gefundene_faecher = [] 

        students_list = self.students.find({
            "halbjahre.normal_faecher.fachArt": fachart_suche
        })

        for student in students_list:
            for halbjahr in student["halbjahre"]:
                for fach in halbjahr["normal_faecher"]:
                    if fach["fachArt"] == fachart_suche:
                        gefundene_faecher.append(fach["fach"])
        return gefundene_faecher
    

    def pruefe_halbjahr_angegeben(self, jahr):          
        result = self.students.find_one({
            "halbjahre": {
                "$elemMatch": {
                    "jahr": jahr,
                    "angegeben": 'True'
                }
            }
        })
        if result == None:
            return False
        return True
    
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
    
    def setzeFaecherBelegtTrue(self, fachnamen: list[str], jahrgang: int):
        results = self.students.find()

        for student in results:
            updated = False

            for halbjahr in student.get("halbjahre", []):
                if halbjahr.get("jahr") == jahrgang:
                    for fach in halbjahr.get("normal_faecher", []):
                        if fach.get("fach") in fachnamen:
                            if fach.get("belegt") != "true":
                                fach["belegt"] = "true"
                                updated = True

            if updated:
                self.students.update_one(
                    {"_id": student["_id"]},
                    {"$set": {"halbjahre": student["halbjahre"]}}
                )
                print(f"✅ Fächer {fachnamen} in Jahrgang {jahrgang} auf 'belegt = true' gesetzt für Schüler {student.get('name')}.")


    def GetAlleAusgefülltenNotenAlsArrayMitAngabeFach(self, fachname, halbjahr_name):
        noten_liste = []

        results = self.students.find({
            "halbjahre.normal_faecher.fach": fachname
        })

        for student in results:
            for halbjahr in student["halbjahre"]:
                if halbjahr.get("name") == halbjahr_name:
                    for fach in halbjahr["normal_faecher"]:
                        if fach["fach"] == fachname:
                            note = fach.get("note", "").strip()
                            if note != "":
                                noten_liste.append({
                                    "schueler": f"{student['vorname']} {student['name']}",
                                    "halbjahr": halbjahr_name,
                                    "note": note
                                })
        return noten_liste
    
    def setNoteInDBEsterFreierPlatzMitDemNotentypeDerNichtBelegtIst(self, fachname, halbjahr_name, notentyp, note):
        results = self.students.find({
            "halbjahre.normal_faecher.fach": fachname
        })

        for student in results:
            aktualisiert = False
            for h_index, halbjahr in enumerate(student["halbjahre"]):
                if halbjahr.get("name") == halbjahr_name:
                    for f_index, fach in enumerate(halbjahr["normal_faecher"]):
                        if fach["fach"] == fachname and fach.get("belegt") == "true":
                            # Überprüfen, ob der Notentyp leer oder nicht vorhanden ist
                            aktueller_wert = fach.get(notentyp, "").strip()
                            if aktueller_wert == "":
                                feldpfad = f"halbjahre.{h_index}.normal_faecher.{f_index}.{notentyp}"
                                self.students.update_one(
                                    {"_id": student["_id"]},
                                    {"$set": {feldpfad: note}}
                                )
                                aktualisiert = True
                                print(f"Note gesetzt für {student['vorname']} {student['name']}")
            if not aktualisiert:
                print(f"Keine freie Stelle für {student['vorname']} {student['name']}")

    
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
    
    def getArrayAusAllenFaechernAndFaechertypseAndGesamtnoteInBestimmtemHalbJahr(self, halbjahr_name):
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
        faecher_noten = [[], []]  # Index 0 = Jahr 1 (12), Index 1 = Jahr 2 (13)
        results = self.students.find()

        for student in results:
            for halbjahr in student.get("halbjahre", []):
                jahr = halbjahr.get("jahr")
                if jahr in [1, 2]:  # Jahrgang 12 und 13
                    index = jahr - 1
                    for fach in halbjahr.get("normal_faecher", []):
                        if fach.get("belegt") == "true":
                            gesamtnote = None
                            for eintrag in fach.get("note", []):
                                if eintrag.get("type") == "gesamt":
                                    gesamtnote = eintrag.get("Wert")
                            faecher_noten[index].append([fach.get("fach"), gesamtnote])
        return faecher_noten

    def checkobpwkorrekt(self, arr):
        if self.students.find_one({"name": arr[0],'vorname': arr[1] ,"passwort": arr[2]}):
            return True
        else:
            return False