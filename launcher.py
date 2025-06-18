import subprocess
import sys
import os
from pymongo import MongoClient
import time

def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

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

# ✅ Proper path setup
if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

register_script        = os.path.join(base_path, 'scripts', 'interface', 'registerpage.py')
register_script_python = os.path.join(base_path, 'dist',    'scripts', 'interface', 'registerpage.py')
login_script           = os.path.join(base_path, 'scripts', 'interface', 'loginpage.py')
login_script_python    = os.path.join(base_path, 'dist',    'scripts', 'interface', 'loginpage.py')

print("Using path:", base_path)
print("Launching:", register_script)
print("Working dir:", os.getcwd())
print("Executable path:", sys.executable)

# ─── Spezifisches MongoDB-Bin-Verzeichnis ins PATH packen ────────────────────
MONGOD_DIR = r"C:\Tools\mongodb\mongodb-win32-x86_64-windows-7.0.8\bin"
if MONGOD_DIR not in os.environ.get("PATH", ""):
    os.environ["PATH"] = MONGOD_DIR + ";" + os.environ["PATH"]

# ─── sicherstellen, dass mongod.exe läuft ────────────────────────────────────
MONGOD_EXE = os.path.join(MONGOD_DIR, "mongod.exe")
def ensure_mongod_running():
    try:
        tmp = MongoClient("localhost", 27017, serverSelectionTimeoutMS=2000)
        tmp.admin.command("ping")
    except Exception:
        print("⚠️ MongoDB nicht erreichbar – starte mongod.exe …")
        # Passe dbpath nach Bedarf an:
        dbpath = os.path.join(MONGOD_DIR, "..", "..", "data", "db")
        os.makedirs(dbpath, exist_ok=True)
        subprocess.Popen([MONGOD_EXE, "--dbpath", dbpath], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(2)

ensure_mongod_running()

client     = MongoClient('localhost', 27017)
db         = client['test']
collection = db['students']

def check_data():
    print('🔍 checking for database...')
    time.sleep(5)
    if collection.find_one():
        print('✅ Found database')
        return True
    print('❌ Didn\'t find a database')
    print('Starting Registerpage')
    time.sleep(2)
    return False

if check_data():
    if os.path.exists(login_script):
        print("✅ Found login_script.py, launching...")
        subprocess.Popen(['python', login_script], shell=True)
    elif os.path.exists(login_script_python):
        print("⚠️ Fallback: Found login_script_python.py in dist, launching...")
        subprocess.Popen([sys.executable, login_script_python], shell=True)
    else:
        print("❌ No script found to launch.")
else:
    if os.path.exists(register_script):
        print("✅ Found register_script.py, launching...")
        subprocess.Popen(['python', register_script], shell=True)
    elif os.path.exists(register_script_python):
        print("⚠️ Fallback: Found register_script_python.py in dist, launching...")
        subprocess.Popen([sys.executable, register_script_python], shell=True)
    else:
        print("❌ No script found to launch.")
