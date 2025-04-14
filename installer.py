import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
import pymongo

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

def connect_to_mongo():
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["testdb"]
        collection = db["testcollection"]
    except Exception as e:
        return f'Error connecting to MongoDB'

class App(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("PyQt6 + MongoDB Example")
        self.setGeometry(100, 100, 300, 150)

        # Layout for widgets
        layout = QVBoxLayout()

        # Label to show connection status
        self.label = QLabel("Click the button to test MongoDB connection.", self)
        layout.addWidget(self.label)

        # Button to trigger MongoDB connection test
        self.button = QPushButton("Test Connection", self)
        self.button.clicked.connect(self.test_connection)
        layout.addWidget(self.button)

        # Set layout for the window
        self.setLayout(layout)

    def test_connection(self):
        # Call the MongoDB connection function and update label with result
        message = connect_to_mongo()
        self.label.setText(message)

# Start the application
def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()