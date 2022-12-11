import sys
from random import randint
from PIL import Image

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, \
    QScrollArea, QPushButton, QDialog, QDialogButtonBox, QLabel, QMessageBox, QMenu
from PyQt6.QtGui import QPalette, QColor, QCursor, QMouseEvent, QContextMenuEvent, QAction, QTextCursor, \
    QTextImageFormat, QTextBlock, QTextFragment
from PyQt6.QtCore import Qt, QPoint, QEvent

from services.services.text_edit_service import TextEditService
from models.text_edit_field_model import TextEditField
from models.textedit_layout import TextEditLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(450,450)
        self.setMinimumWidth(150)
        self.setMinimumHeight(150)
        self.setMaximumHeight(620)
        self.setMaximumWidth(900)
        #
        # self.scroll_area = QScrollArea()
        # self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        # self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # self.scroll_area.setWidgetResizable(True)
        # self.scroll_area.verticalScrollBar().setContentsMargins(10,10,10,10)
        #
        # self.text_edit_field = TextEditField()
        #
        # layout = QVBoxLayout()
        # layout.setContentsMargins(10,20,10,20)
        # layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        #
        # widget = QWidget()
        #
        # layout.addWidget(self.text_edit_field)
        # widget.setLayout(layout)
        # self.scroll_area.setWidget(widget)
        #
        # self.setCentralWidget(self.scroll_area)

        layout = TextEditLayout()
        txt = TextEditField()
        widget = QWidget()


        doc = txt.document()
        cur = QTextCursor(doc)
        p1 = cur.position()
        cur.insertImage('cat2.png')

        print("doc", layout.sizeHint().width())

        it = txt.document().firstBlock().begin()
        while not it.atEnd():
            fragment = it.fragment()
            if fragment.isValid():
                if fragment.charFormat().isImageFormat():
                    new_image_format = fragment.charFormat().toImageFormat()
                    img = Image.open(new_image_format.name())
                    width, height = img.size
                    new_h = height * self.width() / width
                    print('fffff')
                    new_image_format.setWidth(self.width())
                    new_image_format.setHeight(new_h)
                    if new_image_format.isValid():
                        txt_cur = txt.textCursor()
                        txt_cur.setPosition(fragment.position())
                        txt_cur.setPosition(fragment.position() + fragment.length(), QTextCursor.MoveMode.KeepAnchor)
                        txt_cur.setCharFormat(new_image_format)
            it += 1

        #fragment = it.fragment()
        #print(fragment)
        #print(it.fragment().length())

        layout.addWidget(txt)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    # def mousePressEvent(self, a0) -> None:
    #     self.text_edit_field.textCursor()
    #     self.scroll_area.verticalScrollBar().setValue(400)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

