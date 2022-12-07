import sys
from random import randint

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, \
    QScrollArea, QPushButton, QDialog, QDialogButtonBox, QLabel, QMessageBox, QMenu
from PyQt6.QtGui import QPalette, QColor, QCursor, QMouseEvent, QContextMenuEvent, QAction, QTextCursor
from PyQt6.QtCore import Qt, QPoint, QEvent

from services.services.text_edit_service import TextEditService
from models.text_edit_field_model import TextEditField

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setFixedSize(450,450)
        # self.setMinimumWidth(150)
        # self.setMinimumHeight(150)
        # self.setMaximumHeight(620)
        # self.setMaximumWidth(900)
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

        layout = QVBoxLayout()
        txt = QTextEdit()
        widget = QWidget()

        layout.addWidget(txt)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        doc = txt.document()
        cur = QTextCursor(doc)
        p1 = cur.position()
        cur.insertImage('cat.png')

    def mousePressEvent(self, a0) -> None:
        self.text_edit_field.textCursor()
        self.scroll_area.verticalScrollBar().setValue(400)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
