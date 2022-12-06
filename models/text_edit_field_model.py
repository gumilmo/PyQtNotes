import sys

from PyQt6.QtCore import Qt, QObject
from PyQt6.QtGui import QKeyEvent, QWheelEvent, QTextCursor
from PyQt6.QtWidgets import QTextEdit, QWidget, QScrollArea, QPlainTextEdit
from services.services.text_edit_service import TextEditService
from PyQt6.QtCore import QEvent

class TextEditField(QPlainTextEdit):
    def __init__(self):
        super().__init__()

        self.start_height = 40

        self.installEventFilter(self)
        self.text_edit_service = TextEditService()
        self.setFixedHeight(self.start_height)
        self.setMaximumHeight(420)
        self.ensureCursorVisible()
        self.moveCursor(QTextCursor.MoveOperation.End)
        self.setFixedHeight(40)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.verticalScrollBar().setValue(self.verticalScrollBar().minimum())

        self.verticalScrollBar().setDisabled(True)

        self.updateRequest.connect(self.resize_test)
        self.resize_test()

        self.ensureCursorVisible()
        cursor = self.textCursor()
        self.setTextCursor(cursor)

        self.textChanged.connect(self.move_main_scrollbar_to_cursor)

    def wheelEvent(self, e: QWheelEvent) -> None:
        scroll_area = self.parent().parent().parent()
        val = scroll_area.verticalScrollBar().value()
        val -= int(e.angleDelta().y() / 5)
        scroll_area.verticalScrollBar().setValue(val)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.KeyPress and obj is self:
            if event.key() == Qt.Key.Key_Return and self.hasFocus():
                self.text_edit_service.resize_by_space(self)
                scroll_area = self.parent().parent().parent()
                scroll_area = self.parent().parent().parent()
                scroll_area.verticalScrollBar().setValue(
                    int(self.blockBoundingGeometry(self.textCursor().block()).bottom()) - 40)
            if event.key() == Qt.Key.Key_Backspace and obj is self:
                self.text_edit_service.resize_by_backspace(self)
            elif event.key() == Qt.Key.Key_Up:
                scroll_area = self.parent().parent().parent()
                scroll_area.verticalScrollBar().setValue(
                    int(self.blockBoundingGeometry(self.textCursor().block()).bottom()) - 20)
            elif event.key() == Qt.Key.Key_Down:
                scroll_area = self.parent().parent().parent()
                scroll_area.verticalScrollBar().setValue(
                    int(self.blockBoundingGeometry(self.textCursor().block()).bottom()) - 20)
        return super().eventFilter(obj, event)

    def resize_test(self):
        doc = self.document()
        tb = doc.findBlockByNumber(doc.blockCount() - 1)
        h = self.blockBoundingGeometry(tb).bottom() + 2 * doc.documentMargin()
        self.setFixedHeight(int(h))
        #print(self.blockBoundingGeometry(self.textCursor().block()).bottom())


    def move_main_scrollbar_to_cursor(self):
        #self.ensureCursorVisible()
        scroll_area = self.parent().parent().parent()
        scroll_area.verticalScrollBar().setValue(int(self.pos().y() / 10))
        scroll_area.verticalScrollBar().setValue(int(self.blockBoundingGeometry(self.textCursor().block()).bottom()))
        # print(self.textCursor().position(), "pos")
        # print(self.height(),"hhhhh")
        # print("Scroll area var: ", scroll_area.verticalScrollBar().value())
        # print("Self scroll bar: ", self.verticalScrollBar().value())
        #self.setFixedHeight(scroll_area.height())
        #self.verticalScrollBar().setValue(0)
        #self.ensureCursorVisible()
        #scroll_area.verticalScrollBar().setValue(self.height() + 40)
        #scroll_area.verticalScrollBar().setValue(self.verticalScrollBar().value())


