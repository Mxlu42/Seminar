import os
import subprocess
import sys
import urllib.request
import zipfile
import time

# Installationspfade
BASE_DIR = r"C:\Tools"
MONGOSH_DIR = os.path.join(BASE_DIR, "mongosh")
MONGOSH_EXE = os.path.join(MONGOSH_DIR, "mongosh-2.1.4-win32-x64", "bin" ,"mongosh.exe")

MONGOD_DIR = os.path.join(BASE_DIR, "mongodb")
MONGOD_EXE = os.path.join(MONGOD_DIR, "mongodb-win32-x86_64-windows-7.0.8", "bin", "mongod.exe")

def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"📁 Verzeichnis erstellt: {path}")

def is_mongosh_installed():
    return os.path.exists(MONGOSH_EXE)

def is_mongod_installed():
    return os.path.exists(MONGOD_EXE)

def install_mongosh_custom():
    print("⬇️ Lade Mongosh herunter...")
    ensure_directory(MONGOSH_DIR)
    zip_path = os.path.join(MONGOSH_DIR, "mongosh.zip")
    url = "https://downloads.mongodb.com/compass/mongosh-2.1.4-win32-x64.zip"
    urllib.request.urlretrieve(url, zip_path)

    print("📦 Entpacke Mongosh...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(MONGOSH_DIR)
    os.remove(zip_path)
    print("✅ Mongosh wurde installiert.")

def install_mongodb_server():
    print("⬇️ Lade MongoDB Server herunter...")
    ensure_directory(MONGOD_DIR)
    zip_path = os.path.join(MONGOD_DIR, "mongodb.zip")
    url = "https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-7.0.8.zip"
    urllib.request.urlretrieve(url, zip_path)

    print("📦 Entpacke MongoDB Server...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(MONGOD_DIR)
    os.remove(zip_path)
    print("✅ MongoDB Server wurde installiert.")

def start_mongod():
    data_path = os.path.join(MONGOD_DIR, "data", "db")
    ensure_directory(data_path)
    print("🚀 Starte MongoDB Server...")
    subprocess.Popen([MONGOD_EXE, "--dbpath", data_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def open_launcher():
    if getattr(sys, 'frozen', False):
        launcher_path = os.path.dirname(sys.executable)
    else:
        launcher_path = os.path.dirname(os.path.abspath(__file__))

    launcher_script = os.path.join(launcher_path, 'launcher.exe')
    launcher_script_python = os.path.join(launcher_path, 'dist','launcher.exe')

    print("💡 Using path:", launcher_path)
    print("🚀 Launching:", launcher_script)

    if os.path.exists(launcher_script):
        print("✅ Found launcher.exe, launching...")
        time.sleep(3)
        subprocess.Popen(launcher_script, shell=True)
    elif os.path.exists(launcher_script_python):
        print("⚠️ Fallback: Found launcher_script_python.exe in dist, launching...")
        time.sleep(3)
        subprocess.Popen(launcher_script_python, shell=True)
    else:
        print("❌ Kein launcher gefunden.")

def main():
    print("🚧 Starte Installation...")
    ensure_directory(BASE_DIR)

    if is_mongosh_installed():
        print("✅ Mongosh ist bereits installiert.")
    else:
        install_mongosh_custom()

    if is_mongod_installed():
        print("✅ MongoDB Server ist bereits installiert.")
    else:
        install_mongodb_server()

    # Server starten
    start_mongod()

    print("🎉 Alle Installationen abgeschlossen!")
    print("📦 MongoDB & Mongosh bereit.")
    print('🟢 Starte Launcher...')
    open_launcher()

if __name__ == "__main__":
    main()
