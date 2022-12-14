import sys
from PIL import ImageGrab
from PyQt6.QtCore import Qt, QObject, QUrl
from PyQt6.QtGui import QKeyEvent, QWheelEvent, QTextCursor, QResizeEvent, QTextOption, QTextCharFormat, \
    QTextBlockFormat, QFont, QImage, QTextDocument
from PyQt6.QtWidgets import QTextEdit, QWidget, QScrollArea, QPlainTextEdit
from services.services.text_edit_service import TextEditService
from PyQt6.QtCore import QEvent

import os
import sys
import uuid

IMAGE_EXTENSIONS = ['.jpg','.png','.bmp']

def hexuuid():
    return uuid.uuid4().hex

def splitext(p):
    return os.path.splitext(p)[1].lower()

class TextEditField(QTextEdit):
    def __init__(self):
        super().__init__()

        self.text_edit_service = TextEditService()

        self.image_QUrls = {}
        self.near_to_image = False

        self.ensureCursorVisible()
        self.setWordWrapMode(QTextOption.WrapMode.WrapAnywhere)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.textChanged.connect(self.move_cursor_if_image)
        self.cursorPositionChanged.connect(self.text_cursor_position_changed)

    def text_cursor_position_changed(self) -> None:
        is_image_format = self.textCursor().charFormat().isImageFormat()
        self.near_to_image = True if is_image_format else False
        print(self.textCursor().blockFormat().lineHeightType())

    def move_cursor_if_image(self) -> None:
        if self.near_to_image: #TODO and char not backspace
            print("Image!1234")
            self.textCursor().insertText('\n')
            #TODO change text format

    def canInsertFromMimeData(self, source):
        if source.hasImage():
            return True
        else:
            return super(TextEditField, self).canInsertFromMimeData(source)

    def insertFromMimeData(self, source):
        cursor = self.textCursor()
        document = self.document()

        if source.hasUrls():
            self.text_edit_service.paste_image_from_local_file(source, self, document, cursor)
        elif source.hasImage():
            self.text_edit_service.paste_image_from_clipboard(source, self, document, cursor)

        super(TextEditField, self).insertFromMimeData(source)

