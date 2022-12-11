import sys

from PyQt6.QtCore import Qt, QObject
from PyQt6.QtGui import QKeyEvent, QWheelEvent, QTextCursor, QResizeEvent
from PyQt6.QtWidgets import QTextEdit, QWidget, QScrollArea, QPlainTextEdit, QVBoxLayout
from services.services.text_edit_service import TextEditService
from PyQt6.QtCore import QEvent


class TextEditLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()

