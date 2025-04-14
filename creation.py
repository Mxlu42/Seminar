import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
import pymongo

# Automatische Installation fehlender Pakete
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Überprüfen, ob pymongo und PyQt5 installiert sind, falls nicht, installieren
try:
    import pymongo
except ImportError:
    install("pymongo")
    import pymongo

try:
    from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
except ImportError:
    install("PyQt5")
    from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

# MongoDB-Verbindung
def connect_to_mongo():
    try:
        # Verbindung zur MongoDB-Datenbank
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["testdb"]
        collection = db["testcollection"]
        collection.insert_one({"message": "Hello, MongoDB!"})
        return "MongoDB Verbindung erfolgreich!"
    except Exception as e:
        return f"Fehler bei MongoDB-Verbindung: {str(e)}"

# GUI mit PyQt5
class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 + MongoDB Beispiel")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.label = QLabel("Drücke den Button, um MongoDB zu verbinden.", self)
        layout.addWidget(self.label)

        self.button = QPushButton("Verbindung testen", self)
        self.button.clicked.connect(self.test_connection)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def test_connection(self):
        message = connect_to_mongo()
        self.label.setText(message)

# Anwendung starten
def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()