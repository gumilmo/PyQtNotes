import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, \
    QScrollArea, QPushButton, QDialog, QDialogButtonBox, QLabel, QMessageBox
from PyQt6.QtGui import QPalette, QColor, QCursor, QMouseEvent
from PyQt6.QtCore import Qt
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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Jopa!")
        button.clicked.connect(self.btn_clicked)
        print(QCursor.pos().x())
        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def btn_clicked(self, s):
        dlg = QMessageBox.critical(self,
                                   "What?",
                                   "Are you mraz?a?a?a?a?A/A?a??a?A?A?A?A?A??A?A?A?AA?/a/a/a???",
                                   buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.NoToAll | QMessageBox.StandardButton.Ignore,
                                   defaultButton=QMessageBox.StandardButton.Yes
                                   )

        if dlg == QMessageBox.StandardButton.Yes:
            print("OK!")
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
