################################################################################
## Form generated from reading UI file 'qt_design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_NotesMainWindow(object):
    def setupUi(self, NotesMainWindow):
        if not NotesMainWindow.objectName():
            NotesMainWindow.setObjectName(u"NotesMainWindow")
        NotesMainWindow.resize(401, 644)
        NotesMainWindow.setLayoutDirection(Qt.LeftToRight)
        NotesMainWindow.setStyleSheet(u"background-color: white;")
        self.main_widget = QWidget(NotesMainWindow)
        self.main_widget.setObjectName(u"main_widget")
        self.verticalLayout = QVBoxLayout(self.main_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.up_buttons_bar = QHBoxLayout()
        self.up_buttons_bar.setObjectName(u"up_buttons_bar")
        self.up_buttons_bar.setContentsMargins(-1, 0, -1, 0)
        self.up_btn4 = QPushButton(self.main_widget)
        self.up_btn4.setObjectName(u"up_btn4")
        self.up_btn4.setStyleSheet(u" background-color: red;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
" border: none;\n"
" max-width:20px;\n"
" max-height:20px;\n"
" min-width:20px;\n"
" min-height:20px;")

        self.up_buttons_bar.addWidget(self.up_btn4)

        self.up_button_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.up_buttons_bar.addItem(self.up_button_spacer)

        self.up_btn3 = QPushButton(self.main_widget)
        self.up_btn3.setObjectName(u"up_btn3")
        self.up_btn3.setStyleSheet(u" background-color: red;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
" border: none;\n"
" max-width:20px;\n"
" max-height:20px;\n"
" min-width:20px;\n"
" min-height:20px;")

        self.up_buttons_bar.addWidget(self.up_btn3)

        self.up_btn2 = QPushButton(self.main_widget)
        self.up_btn2.setObjectName(u"up_btn2")
        self.up_btn2.setStyleSheet(u" background-color: red;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
" border: none;\n"
" max-width:20px;\n"
" max-height:20px;\n"
" min-width:20px;\n"
" min-height:20px;")

        self.up_buttons_bar.addWidget(self.up_btn2)

        self.up_btn1 = QPushButton(self.main_widget)
        self.up_btn1.setObjectName(u"up_btn1")
        self.up_btn1.setStyleSheet(u" background-color: red;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
" border: none;\n"
" max-width:20px;\n"
" max-height:20px;\n"
" min-width:20px;\n"
" min-height:20px;")

        self.up_buttons_bar.addWidget(self.up_btn1)


        self.verticalLayout.addLayout(self.up_buttons_bar)

        self.central_space = QGridLayout()
        self.central_space.setObjectName(u"central_space")
        self.frst_text = QTextEdit(self.main_widget)
        self.frst_text.setObjectName(u"frst_text")
        self.frst_text.setStyleSheet(u"QScrollBar:vertical {\n"
"	display: none;\n"
"}")

        self.central_space.addWidget(self.frst_text, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.central_space)

        self.down_buttons_bar = QHBoxLayout()
        self.down_buttons_bar.setObjectName(u"down_buttons_bar")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.down_buttons_bar.addItem(self.horizontalSpacer_3)

        self.left_space = QGridLayout()
        self.left_space.setObjectName(u"left_space")

        self.down_buttons_bar.addLayout(self.left_space)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.down_buttons_bar.addItem(self.horizontalSpacer_5)

        self.right_space = QGridLayout()
        self.right_space.setObjectName(u"right_space")

        self.down_buttons_bar.addLayout(self.right_space)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.down_buttons_bar.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.down_buttons_bar.addItem(self.horizontalSpacer_4)

        self.down_btn2 = QPushButton(self.main_widget)
        self.down_btn2.setObjectName(u"down_btn2")
        self.down_btn2.setStyleSheet(u" background-color: red;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
" border: none;\n"
" max-width:20px;\n"
" max-height:20px;\n"
" min-width:20px;\n"
" min-height:20px;")

        self.down_buttons_bar.addWidget(self.down_btn2)

        self.down_btn_space = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.down_buttons_bar.addItem(self.down_btn_space)

        self.down_btn1 = QPushButton(self.main_widget)
        self.down_btn1.setObjectName(u"down_btn1")
        self.down_btn1.setStyleSheet(u" background-color: red;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:10px;\n"
" border: none;\n"
" max-width:20px;\n"
" max-height:20px;\n"
" min-width:20px;\n"
" min-height:20px;")

        self.down_buttons_bar.addWidget(self.down_btn1)


        self.verticalLayout.addLayout(self.down_buttons_bar)

        NotesMainWindow.setCentralWidget(self.main_widget)

        self.retranslateUi(NotesMainWindow)

        QMetaObject.connectSlotsByName(NotesMainWindow)
    # setupUi

    def retranslateUi(self, NotesMainWindow):
        NotesMainWindow.setWindowTitle(QCoreApplication.translate("NotesMainWindow", u"notes", None))
        self.up_btn4.setText("")
        self.up_btn3.setText("")
        self.up_btn2.setText("")
        self.up_btn1.setText("")
        self.down_btn2.setText("")
        self.down_btn1.setText("")
    # retranslateUi

