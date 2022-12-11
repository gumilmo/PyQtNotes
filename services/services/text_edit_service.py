import sys
from PIL import Image
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QFontMetrics, QFont, QTextCursor
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QCheckBox, QComboBox, QListWidget, QLineEdit, QSpinBox, \
    QSlider, QDial, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QTabWidget, QTextEdit, \
    QScrollArea
from PyQt6.QtGui import QPalette, QColor
from services.interfaces.textedit_service_interface import TextEditServiceInterface


class TextEditService(TextEditServiceInterface):

    @staticmethod
    def resize_main(text_field) -> None:
        print(text_field.toPlainText())
        pass

    @staticmethod
    def resize_by_window(text_field) -> None:
        pass

    @staticmethod
    def resize_by_space(text_field) -> None:
        text_field.start_height += 15
        text_field.setFixedHeight(text_field.start_height)

    @staticmethod
    def resize_by_backspace(text_field) -> None:
        pass
        # if text_field.start_height > 40:
        #     text_field.start_height -= 15
        #     text_field.setFixedHeight(text_field.start_height)

    @staticmethod
    def resize_by_font_metrics(text_field: QTextEdit) -> None:
        pass

    @staticmethod
    def call_text_edit_context_menu(self) -> None:
        pass

    @staticmethod
    def change_text_font_size(self) -> None:
        pass

    @staticmethod
    def change_text_font_color(self) -> None:
        pass

    @staticmethod
    def change_text_font_weight(self) -> None:
        pass

    @staticmethod
    def change_text_font_italic(self) -> None:
        pass

    @staticmethod
    def image_resize(text_field: QTextEdit, main_window: QMainWindow) -> None:
        it = text_field.document().firstBlock().begin()
        while not it.atEnd():
            fragment = it.fragment()
            if fragment.isValid():
                if fragment.charFormat().isImageFormat():
                    new_image_format = fragment.charFormat().toImageFormat()
                    print(new_image_format)
                    # img = Image.open(new_image_format.name())
                    # width, height = img.size
                    # new_h = height * main_window.width() / width
                    # print('fffff')
                    # new_image_format.setWidth(main_window.width())
                    # new_image_format.setHeight(new_h)
                    # if new_image_format.isValid():
                    #     txt_cur = text_field.textCursor()
                    #     txt_cur.setPosition(fragment.position())
                    #     txt_cur.setPosition(fragment.position() + fragment.length(), QTextCursor.MoveMode.KeepAnchor)
                    #     txt_cur.setCharFormat(new_image_format)
            it += 1