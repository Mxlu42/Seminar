import subprocess
import sys
import os
import time
from pymongo import MongoClient, errors

def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# Abhängigkeiten sicherstellen
try:
    import pymongo
except ImportError:
    install('pymongo')
    import pymongo

try:
    from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
except ImportError:
    install('PyQt6')
    from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

# Pfadaufbau
if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

register_script        = os.path.join(base_path, 'scripts', 'interface', 'registerpage.py')
register_script_python = os.path.join(base_path, 'dist',   'scripts', 'interface', 'registerpage.py')
login_script           = os.path.join(base_path, 'scripts', 'interface', 'loginpage.py')
login_script_python    = os.path.join(base_path, 'dist',   'scripts', 'interface', 'loginpage.py')

print("Using path:", base_path)
print("Executable:", sys.executable)
print("Working dir:", os.getcwd())

def get_mongo_client():
    """
    Versucht, eine Verbindung zu MongoDB herzustellen. Falls der Dienst
    nicht läuft, wird er gestartet. Schlägt beides fehl, wird None zurückgegeben.
    """
    try:
        client = MongoClient(
            'mongodb://localhost:27017/',
            serverSelectionTimeoutMS=3000,  # 3 Sekunden warten
        )
        client.admin.command('ping')     # prüft, ob MongoDB antwortet
        return client
    except errors.ServerSelectionTimeoutError:
        print("⚠️ MongoDB-Dienst nicht erreichbar. Versuche, ihn zu starten…")
        try:
            subprocess.check_call(['net', 'start', 'MongoDB'], shell=True)
            time.sleep(2)
            client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=3000)
            client.admin.command('ping')
            print("✅ MongoDB-Dienst gestartet.")
            return client
        except subprocess.CalledProcessError:
            print("❌ Konnte MongoDB-Dienst nicht starten. Bitte manuell prüfen.")
            return None
    except errors.OperationFailure as e:
        print("❌ Authentifizierungsfehler bei MongoDB:", e)
        return None

def check_data_and_launch():
    client = get_mongo_client()
    if not client:
        # Abbruch oder Fallback
        print("ℹ️ Kein Zugriff auf MongoDB. Starte Registrierungsseite unverändert.")
        launch = register_script if os.path.exists(register_script) else register_script_python
        subprocess.Popen([sys.executable, launch], shell=True)
        return

    db         = client['test']
    collection = db['students']

    try:
        has_data = collection.find_one() is not None
    except errors.PyMongoError as e:
        print("❌ Fehler beim Abfragen der Datenbank:", e)
        has_data = False

    if has_data:
        script = login_script if os.path.exists(login_script) else login_script_python
        print("✅ Datensatz gefunden. Starte Login:", script)
    else:
        script = register_script if os.path.exists(register_script) else register_script_python
        print("ℹ️ Kein Datensatz. Starte Registrierung:", script)

    subprocess.Popen([sys.executable, script], shell=True)

if __name__ == "__main__":
    check_data_and_launch()
