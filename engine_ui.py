import sys
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import (Slot, Signal, QObject)
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel,
                               QPushButton, QWidget, QVBoxLayout, QLineEdit)

app = QApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.load('ai_chatbox.qml')

sys.exit(app.exec())