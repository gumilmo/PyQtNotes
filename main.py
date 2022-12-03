import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, \
    QScrollArea
from PyQt6.QtGui import QPalette, QColor
from services.services.text_edit_service import TextEditService


class Color(QWidget):
    def __init__(self, color):
        super().__init__()

        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        text_edit_serivce = TextEditService()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()
        area = QScrollArea()

        self.line = QTextEdit()
        self.line.setFixedHeight(30)
        self.line.textChanged.connect(lambda : text_edit_serivce.resize_main(self.line))
        layout.addWidget(self.line)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def resizeEvent(self, event):
        print(self.width(), self.height())
        QMainWindow.resizeEvent(self, event)

    def resize_textedit(self):
        pass

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
