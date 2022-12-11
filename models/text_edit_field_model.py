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

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWordWrapMode(QTextOption.WrapMode.WrapAnywhere)
        self.ensureCursorVisible()

        self.cursorPositionChanged.connect(self.pos_chng)
        #clipboard_img = ImageGrab.grabclipboard()
        #clipboard_img.save('clipboard.jpg','JPG')

    def pos_chng(self) -> None:
        if self.textCursor().charFormat().isImageFormat():
            print("Image!")


    def canInsertFromMimeData(self, source):

        if source.hasImage():
            return True
        else:
            return super(TextEditField, self).canInsertFromMimeData(source)

    def insertFromMimeData(self, source):

        cursor = self.textCursor()
        document = self.document()

        if source.hasUrls():

            for u in source.urls():
                file_ext = splitext(str(u.toLocalFile()))
                if u.isLocalFile() and file_ext in IMAGE_EXTENSIONS:
                    image = QImage(u.toLocalFile())
                    document.addResource(QTextDocument.ResourceType.ImageResource, u, image)
                    cursor.insertImage(u.toLocalFile())

                else:
                    # If we hit a non-image or non-local URL break the loop and fall out
                    # to the super call & let Qt handle it
                    break

            else:
                # If all were valid images, finish here.
                return


        elif source.hasImage():
            image = source.imageData()
            uuid = hexuuid()
            document.addResource(QTextDocument.ResourceType.ImageResource, QUrl(uuid), image)
            cursor.insertImage(uuid)
            return

        super(TextEditField, self).insertFromMimeData(source)

