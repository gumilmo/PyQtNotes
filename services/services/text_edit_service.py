import sys
from PIL import Image
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QFontMetrics, QFont, QTextCursor, QTextFormat
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QCheckBox, QComboBox, QListWidget, QLineEdit, QSpinBox, \
    QSlider, QDial, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QTabWidget, QTextEdit, \
    QScrollArea
from PyQt6.QtGui import QPalette, QColor, QTextFragment, QTextDocument, QImage, QTransform, QTextCursor
from services.interfaces.textedit_service_interface import TextEditServiceInterface


class TextEditService(TextEditServiceInterface):

    @staticmethod
    def resize_main(text_field: QTextEdit, main_window: QMainWindow) -> None:
        for block_num in range(text_field.document().blockCount()):
            block = text_field.document().findBlockByNumber(block_num)
            block_iterator = block.begin()
            if not block_iterator.atEnd():
                fragment = block_iterator.fragment()
                if fragment.isValid():
                    for qurl in text_field.image_QUrls:
                        image_resource: QImage = text_field.document().\
                            resource(QTextDocument.ResourceType.ImageResource,qurl)
                        if fragment.charFormat().isImageFormat():
                            TextEditService.new_image_size(fragment, text_field, main_window, image_resource)
                block_iterator += 1
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
    def new_image_size(fragment: QTextFragment,
                       text_field: QTextEdit,
                       main_window: QMainWindow,
                       image_resource: QImage
                       ) -> None:
        new_size = TextEditService.image_resize(image_resource, main_window)
        image_format = TextEditService.new_image_format(fragment, new_size)
        if image_format.isValid():
            TextEditService.insert_format_to_cursor(text_field, fragment, image_format)

    @staticmethod
    def image_resize(image_resource: QImage, main_window: QMainWindow) -> QSize:
        width, height = image_resource.size().width(), image_resource.size().height()
        new_width = main_window.width() - 60
        new_height = height * new_width / width
        return QSize(int(new_width), int(new_height))

    @staticmethod
    def new_image_format(fragment: QTextFragment, new_size: QSize) -> QTextFormat:
        new_image_format = fragment.charFormat().toImageFormat()
        new_image_format.setWidth(new_size.width())
        new_image_format.setHeight(new_size.height())
        return new_image_format

    @staticmethod
    def insert_format_to_cursor(text_field: QTextEdit,
                                fragment: QTextFragment,
                                format: QTextFormat
                                ) -> None:
        txt_cur = text_field.textCursor()
        txt_cur.setPosition(fragment.position())
        txt_cur.setPosition(fragment.position() + fragment.length(), QTextCursor.MoveMode.KeepAnchor)
        txt_cur.setCharFormat(format)

