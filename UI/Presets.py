# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Presets.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Presets(object):
    def setupUi(self, Presets):
        if not Presets.objectName():
            Presets.setObjectName(u"Presets")
        Presets.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Presets)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.btn_preset_8 = QPushButton(Presets)
        self.btn_preset_8.setObjectName(u"btn_preset_8")
        self.btn_preset_8.setEnabled(True)
        font = QFont()
        font.setPointSize(12)
        self.btn_preset_8.setFont(font)

        self.gridLayout.addWidget(self.btn_preset_8, 2, 1, 1, 1)

        self.btn_preset_3 = QPushButton(Presets)
        self.btn_preset_3.setObjectName(u"btn_preset_3")
        self.btn_preset_3.setEnabled(True)
        self.btn_preset_3.setFont(font)

        self.gridLayout.addWidget(self.btn_preset_3, 0, 2, 1, 1)

        self.btn_preset_6 = QPushButton(Presets)
        self.btn_preset_6.setObjectName(u"btn_preset_6")
        self.btn_preset_6.setEnabled(True)
        self.btn_preset_6.setFont(font)

        self.gridLayout.addWidget(self.btn_preset_6, 1, 2, 1, 1)

        self.btn_preset_2 = QPushButton(Presets)
        self.btn_preset_2.setObjectName(u"btn_preset_2")
        self.btn_preset_2.setEnabled(True)
        self.btn_preset_2.setFont(font)

        self.gridLayout.addWidget(self.btn_preset_2, 0, 1, 1, 1)

        self.btn_preset_1 = QPushButton(Presets)
        self.btn_preset_1.setObjectName(u"btn_preset_1")
        self.btn_preset_1.setEnabled(True)
        self.btn_preset_1.setFont(font)

        self.gridLayout.addWidget(self.btn_preset_1, 0, 0, 1, 1)

        self.btn_preset_7 = QPushButton(Presets)
        self.btn_preset_7.setObjectName(u"btn_preset_7")
        self.btn_preset_7.setEnabled(True)
        self.btn_preset_7.setFont(font)

        self.gridLayout.addWidget(self.btn_preset_7, 2, 0, 1, 1)

        self.btn_preset_10 = QPushButton(Presets)
        self.btn_preset_10.setObjectName(u"btn_preset_10")
        self.btn_preset_10.setEnabled(True)
        self.btn_preset_10.setFont(font)

        self.gridLayout.addWidget(self.btn_preset_10, 3, 0, 1, 1)

        self.btn_preset_11 = QPushButton(Presets)
        self.btn_preset_11.setObjectName(u"btn_preset_11")
        self.btn_preset_11.setEnabled(True)
        self.btn_preset_11.setFont(font)

        self.gridLayout.addWidget(self.btn_preset_11, 3, 1, 1, 1)

        self.btn_preset_5 = QPushButton(Presets)
        self.btn_preset_5.setObjectName(u"btn_preset_5")
        self.btn_preset_5.setEnabled(True)
        self.btn_preset_5.setFont(font)

        self.gridLayout.addWidget(self.btn_preset_5, 1, 1, 1, 1)

        self.btn_preset_9 = QPushButton(Presets)
        self.btn_preset_9.setObjectName(u"btn_preset_9")
        self.btn_preset_9.setEnabled(True)
        self.btn_preset_9.setFont(font)

        self.gridLayout.addWidget(self.btn_preset_9, 2, 2, 1, 1)

        self.btn_preset_4 = QPushButton(Presets)
        self.btn_preset_4.setObjectName(u"btn_preset_4")
        self.btn_preset_4.setEnabled(True)
        self.btn_preset_4.setFont(font)

        self.gridLayout.addWidget(self.btn_preset_4, 1, 0, 1, 1)

        self.btn_preset_12 = QPushButton(Presets)
        self.btn_preset_12.setObjectName(u"btn_preset_12")
        self.btn_preset_12.setEnabled(True)
        self.btn_preset_12.setFont(font)

        self.gridLayout.addWidget(self.btn_preset_12, 3, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Presets)

        QMetaObject.connectSlotsByName(Presets)
    # setupUi

    def retranslateUi(self, Presets):
        Presets.setWindowTitle(QCoreApplication.translate("Presets", u"Form", None))
        self.btn_preset_8.setText(QCoreApplication.translate("Presets", u"40:00", None))
        self.btn_preset_3.setText(QCoreApplication.translate("Presets", u"15:00", None))
        self.btn_preset_6.setText(QCoreApplication.translate("Presets", u"30:00", None))
        self.btn_preset_2.setText(QCoreApplication.translate("Presets", u"10:00", None))
        self.btn_preset_1.setText(QCoreApplication.translate("Presets", u"05:00", None))
        self.btn_preset_7.setText(QCoreApplication.translate("Presets", u"35:00", None))
        self.btn_preset_10.setText(QCoreApplication.translate("Presets", u"50:00", None))
        self.btn_preset_11.setText(QCoreApplication.translate("Presets", u"55:00", None))
        self.btn_preset_5.setText(QCoreApplication.translate("Presets", u"25:00", None))
        self.btn_preset_9.setText(QCoreApplication.translate("Presets", u"45:00", None))
        self.btn_preset_4.setText(QCoreApplication.translate("Presets", u"20:00", None))
        self.btn_preset_12.setText(QCoreApplication.translate("Presets", u"60:00", None))
    # retranslateUi

