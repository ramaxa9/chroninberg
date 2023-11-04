# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BlackView.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_BlackView(object):
    def setupUi(self, BlackView):
        if not BlackView.objectName():
            BlackView.setObjectName(u"BlackView")
        BlackView.resize(1193, 593)
        BlackView.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.horizontalLayout = QHBoxLayout(BlackView)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(BlackView)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)


        self.retranslateUi(BlackView)

        QMetaObject.connectSlotsByName(BlackView)
    # setupUi

    def retranslateUi(self, BlackView):
        BlackView.setWindowTitle(QCoreApplication.translate("BlackView", u"Form", None))
        self.label.setText(QCoreApplication.translate("BlackView", u"TextLabel", None))
    # retranslateUi

