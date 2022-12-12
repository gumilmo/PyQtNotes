import sys
from random import randint
from PIL import Image

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, \
    QScrollArea, QPushButton, QDialog, QDialogButtonBox, QLabel, QMessageBox, QMenu
from PyQt6.QtGui import QPalette, QColor, QCursor, QMouseEvent, QContextMenuEvent, QAction, QTextCursor, \
    QTextImageFormat, QTextBlock, QTextFragment, QResizeEvent
from PyQt6.QtCore import Qt, QPoint, QEvent

from services.services.text_edit_service import TextEditService
from models.text_edit_field_model import TextEditField
from models.textedit_layout import TextEditLayout
from services.services.text_edit_service import TextEditService

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(450,450)
        self.setMinimumWidth(150)
        self.setMinimumHeight(150)
        self.setMaximumHeight(620)
        self.setMaximumWidth(900)

        layout = TextEditLayout()
        self.txt = TextEditField()
        widget = QWidget()

        self.text_edit_service = TextEditService()

        #fragment = it.fragment()
        #print(fragment)
        #print(it.fragment().length())

        layout.addWidget(self.txt)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.text_edit_service.resize_main(self.txt, self)

    # def mousePressEvent(self, a0) -> None:
    #     self.text_edit_field.textCursor()
    #     self.scroll_area.verticalScrollBar().setValue(400)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

