# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ClockView.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ClockView(object):
    def setupUi(self, ClockView):
        if not ClockView.objectName():
            ClockView.setObjectName(u"ClockView")
        ClockView.resize(1193, 593)
        ClockView.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout = QVBoxLayout(ClockView)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_clock = QLabel(ClockView)
        self.lbl_clock.setObjectName(u"lbl_clock")
        self.lbl_clock.setMinimumSize(QSize(0, 200))
        font = QFont()
        font.setPointSize(150)
        self.lbl_clock.setFont(font)
        self.lbl_clock.setStyleSheet(u"color: rgb(182, 182, 182);")
        self.lbl_clock.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_clock)


        self.retranslateUi(ClockView)

        QMetaObject.connectSlotsByName(ClockView)
    # setupUi

    def retranslateUi(self, ClockView):
        ClockView.setWindowTitle(QCoreApplication.translate("ClockView", u"Form", None))
        self.lbl_clock.setText(QCoreApplication.translate("ClockView", u"Current time", None))
    # retranslateUi

