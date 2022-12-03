import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QFontMetrics, QFont
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QCheckBox, QComboBox, QListWidget, QLineEdit, QSpinBox, \
    QSlider, QDial, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QTabWidget, QTextEdit, \
    QScrollArea
from PyQt6.QtGui import QPalette, QColor
from services.interfaces.textedit_service_interface import TextEditServiceInterface


class TextEditService(TextEditServiceInterface):

    @staticmethod
    def resize(text_field: QTextEdit):
        print(text_field.toPlainText())
        pass

    @staticmethod
    def resize_by_window(text_field: QTextEdit) -> None:
        pass

    @staticmethod
    def resize_by_space(text_field: QTextEdit) -> None:
        pass

    @staticmethod
    def resize_by_font_metrics(text_field: QTextEdit) -> None:
        pass
