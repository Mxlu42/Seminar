from pymongo import MongoClient

class DBHelp(object):
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["schule"]
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
                        
    def ChangeAttributes(self, fachname, fachart, note):
        students_list = self.students.find({
            "halbjahre.normal_faecher.fach": fachname
        })

        for student in students_list:
            updated_halbjahre = []

            for halbjahr in student["halbjahre"]:
                neue_faecher = []

                for fach in halbjahr["normal_faecher"]:
                    if fach["fach"] == fachname:
                        fach["fachArt"] = fachart
                        fach["note"] = note
                    neue_faecher.append(fach)

                halbjahr["normal_faecher"] = neue_faecher
                updated_halbjahre.append(halbjahr)

            # Update das gesamte halbjahre-Array
            self.students.update_one(
                {"_id": student["_id"]},
                {"$set": {"halbjahre": updated_halbjahre}}
            )
            print(f"✅ Aktualisiert: {student['name']} - {student['vorname']}")

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
                    "angegeben": True
                }
            }
        })
        return result is not None
    
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