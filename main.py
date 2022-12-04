import sys
from random import randint

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, \
    QScrollArea, QPushButton, QDialog, QDialogButtonBox, QLabel, QMessageBox, QMenu
from PyQt6.QtGui import QPalette, QColor, QCursor, QMouseEvent, QContextMenuEvent, QAction
from PyQt6.QtCore import Qt, QPoint
from services.services.text_edit_service import TextEditService


class Color(QWidget):
    def __init__(self, color):
        super().__init__()

        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class CustomDialog(QDialog):
    def __init__(self):
        super(CustomDialog, self).__init__()

        self.setWindowTitle("Hi!")

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel | \
               QDialogButtonBox.StandardButton.Help | QDialogButtonBox.StandardButton.Open

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.acepted_new)
        self.buttonBox.rejected.connect(self.close_main)

        self.layout = QVBoxLayout()
        message = QLabel("Something went wrong!")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

        self.move(QCursor.pos().x() - 150, QCursor.pos().y() - 90)

    def acepted_new(self):
        dialog = CustomDialog()
        dialog.exec()

    def close_main(self):
        print(self.parent())

    def mousePressEvent(self, event) -> None:
        self.close()

class Lable(QLabel):
    def __init__(self):
        super().__init__()

        #self.enterEvent = self.enter
        self.leaveEvent = self.leave

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.setText("Faaaaaart!")
        elif event.button() == Qt.MouseButton.RightButton:
            self.setText("Jopk!")

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.setText("GVNO")

    def mouseMoveEvent(self, ev) -> None:
        print("fart n sniff")


    # def enter(self, event):
    #     print(self)

    @staticmethod
    def leave(event):
        print("gvno")

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.lable = Lable()
        self.lable.setText("Another window! %d" % randint(0, 100))
        layout.addWidget(self.lable)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.show()

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos) -> None:
        print("Conetex menu was called")
        context = QMenu(self)
        context.addAction(QAction("test1", self))
        context.addAction(QAction("test2", self))
        context.addAction(QAction("test3", self))
        context.exec(self.mapToGlobal(pos))
        print(context.parent())
    #
    # def resizeEvent(self, event):
    #     print(self.width(), self.height())
    #     QMainWindow.resizeEvent(self, event)
    #
    # def resize_textedit(self):
    #     pass


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
