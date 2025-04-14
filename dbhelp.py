from pymongo import MongoClient

class DBHelp(object):
    def FachBelegt(fachname):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['schule']
        students = db['students']

        # Suche nur Schüler, die das Fach irgendwo belegt haben
        results = students.find({
            "halbjahre.normal_faecher.fach": fachname
        })

        for student in results:
            print(f"\n{student['name']} - {student['vorname']}")

            for halbjahr in student["halbjahre"]:
                for fach in halbjahr["normal_faecher"]:
                    if fach["fach"] == fachname:
                        status = fach["belegt"]
                        if status == "true":
                            return True
                        else:
                            return False
                        
    def ChangeAttributes(fachname, fachart, note):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['schule']
        students = db['students']

        students_list = students.find({
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
            students.update_one(
                {"_id": student["_id"]},
                {"$set": {"halbjahre": updated_halbjahre}}
            )

            print(f"✅ Aktualisiert: {student['name']} - {student['vorname']}")

    def get_faecher_by_fachart(fachart_suche):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['schule']
        students = db['students']

        gefundene_faecher = set()

        students_list = students.find({
            "halbjahre.normal_faecher.fachArt": fachart_suche
        })

        for student in students_list:
            for halbjahr in student["halbjahre"]:
                for fach in halbjahr["normal_faecher"]:
                    if fach["fachArt"] == fachart_suche:
                        gefundene_faecher.add(fach["fach"])
                        return gefundene_faecher
    

    def pruefe_halbjahr_angegeben(jahr):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['schule']
        students = db["students"]

        
        halbjahre = students.find("halbjahre", [])
        for halbjahr in halbjahre:
            if halbjahr("jahr") == jahr and halbjahr("angegeben") == "true":
                return True