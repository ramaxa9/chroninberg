# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'duration.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 209)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.minutes = QSpinBox(Form)
        self.minutes.setObjectName(u"minutes")

        self.horizontalLayout.addWidget(self.minutes)

        self.hours = QSpinBox(Form)
        self.hours.setObjectName(u"hours")

        self.horizontalLayout.addWidget(self.hours)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.btn_set = QPushButton(Form)
        self.btn_set.setObjectName(u"btn_set")

        self.verticalLayout.addWidget(self.btn_set)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_set.setText(QCoreApplication.translate("Form", u"Set", None))
    # retranslateUi

