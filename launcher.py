import subprocess
import sys
import os

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
    register_path = os.path.dirname(sys.executable)
else:
    register_path = os.path.dirname(os.path.abspath(__file__))

register_script = os.path.join(register_path,'scripts', 'registerpage.py')
register_script_python = os.path.join(register_path, 'dist','scripts', 'registerpage.py')

print("Using path:", register_path)
print("Launching:", register_script)
print("Working dir:", os.getcwd())
print("Executable path:", sys.executable)

if os.path.exists(register_script):
    print("✅ Found register_script.py, launching...")
    subprocess.Popen(['python', register_script], shell=True)
elif os.path.exists(register_script_python):
    print("⚠️ Fallback: Found register_script_python.py in dist, launching...")
    subprocess.Popen([sys.executable, register_script_python], shell=True)
else:
    print("❌ No script found to launch.")
