import os
import subprocess
import sys
import urllib.request
import zipfile
import time

# Vorgegebene Installationspfade
BASE_DIR = r"C:\Tools"
MONGOSH_DIR = os.path.join(BASE_DIR, "mongosh")
MONGOSH_EXE = os.path.join(MONGOSH_DIR, "mongosh-2.1.4-win32-x64", "mongosh.exe")

def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Verzeichnis erstellt: {path}")

def is_mongosh_installed():
    return os.path.exists(MONGOSH_EXE)

def install_mongosh_custom():
    print("Lade Mongosh herunter...")
    ensure_directory(MONGOSH_DIR)

    zip_path = os.path.join(MONGOSH_DIR, "mongosh.zip")
    url = "https://downloads.mongodb.com/compass/mongosh-2.1.4-win32-x64.zip"
    urllib.request.urlretrieve(url, zip_path)

    print("Entpacke Mongosh...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(MONGOSH_DIR)

    os.remove(zip_path)
    print("Mongosh wurde installiert.")

def open_launcher():
    if getattr(sys, 'frozen', False):
        launcher_path = os.path.dirname(sys.executable)
    else:
        launcher_path = os.path.dirname(os.path.abspath(__file__))

    launcher_script = os.path.join(launcher_path, 'launcher.exe')
    launcher_script_python = os.path.join(launcher_path, 'dist','launcher.exe')

    print("Using path:", launcher_path)
    print("Launching:", launcher_script)
    print("Working dir:", os.getcwd())
    print("Executable path:", sys.executable)

    if os.path.exists(launcher_script):
        print("✅ Found launcher.exe, launching...")
        time.sleep(3)
        subprocess.Popen(launcher_script, shell=True)
    elif os.path.exists(launcher_script_python):
        print("⚠️ Fallback: Found launcher_script_python.py in dist, launching...")
        time.sleep(3)
        subprocess.Popen(launcher_script_python, shell=True)
    else:
        print("❌ No script found to launch.")

def main():
    print("Starte Installation...")
    
    ensure_directory(BASE_DIR)

    if is_mongosh_installed():
        print("✅ Mongosh ist bereits installiert.")
        result = subprocess.run([MONGOSH_EXE, "--version"], capture_output=True, text=True)
        print("📦 Mongosh-Version:", result.stdout.strip())
    else:
        install_mongosh_custom()
        print("✅ Mongosh wurde erfolgreich installiert.")

    print("🎉 Alle Installationen abgeschlossen!")
    print('starting the launcher...')
    open_launcher()

if __name__ == "__main__":
    main()
