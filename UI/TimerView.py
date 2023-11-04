# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TimerView.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QProgressBar, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_TimerView(object):
    def setupUi(self, TimerView):
        if not TimerView.objectName():
            TimerView.setObjectName(u"TimerView")
        TimerView.resize(1193, 826)
        TimerView.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(TimerView)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_timer = QLabel(TimerView)
        self.lbl_timer.setObjectName(u"lbl_timer")
        self.lbl_timer.setMinimumSize(QSize(0, 200))
        font = QFont()
        font.setPointSize(72)
        self.lbl_timer.setFont(font)
        self.lbl_timer.setStyleSheet(u"color: rgb(0, 255, 0);")
        self.lbl_timer.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_timer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.timer_progress = QProgressBar(TimerView)
        self.timer_progress.setObjectName(u"timer_progress")
        self.timer_progress.setMinimumSize(QSize(0, 0))
        self.timer_progress.setStyleSheet(u"")
        self.timer_progress.setMinimum(0)
        self.timer_progress.setMaximum(1000)
        self.timer_progress.setValue(50)
        self.timer_progress.setAlignment(Qt.AlignCenter)
        self.timer_progress.setTextVisible(False)
        self.timer_progress.setInvertedAppearance(False)

        self.horizontalLayout_2.addWidget(self.timer_progress)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_eta = QLabel(TimerView)
        self.lbl_eta.setObjectName(u"lbl_eta")
        self.lbl_eta.setMinimumSize(QSize(0, 200))
        font1 = QFont()
        font1.setPointSize(32)
        self.lbl_eta.setFont(font1)
        self.lbl_eta.setStyleSheet(u"color: rgb(182, 182, 182);")
        self.lbl_eta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_eta)

        self.lbl_clock = QLabel(TimerView)
        self.lbl_clock.setObjectName(u"lbl_clock")
        self.lbl_clock.setMinimumSize(QSize(0, 200))
        self.lbl_clock.setFont(font1)
        self.lbl_clock.setStyleSheet(u"color: rgb(182, 182, 182);")
        self.lbl_clock.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_clock)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lbl_message = QLabel(TimerView)
        self.lbl_message.setObjectName(u"lbl_message")
        self.lbl_message.setMinimumSize(QSize(0, 400))
        self.lbl_message.setMaximumSize(QSize(16777215, 400))
        self.lbl_message.setFont(font1)
        self.lbl_message.setStyleSheet(u"color: rgb(182, 182, 182);")
        self.lbl_message.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_message)


        self.retranslateUi(TimerView)

        QMetaObject.connectSlotsByName(TimerView)
    # setupUi

    def retranslateUi(self, TimerView):
        TimerView.setWindowTitle(QCoreApplication.translate("TimerView", u"Form", None))
        self.lbl_timer.setText(QCoreApplication.translate("TimerView", u"Timer", None))
        self.timer_progress.setFormat(QCoreApplication.translate("TimerView", u"%v", None))
        self.lbl_eta.setText(QCoreApplication.translate("TimerView", u"ETA", None))
        self.lbl_clock.setText(QCoreApplication.translate("TimerView", u"Current time", None))
        self.lbl_message.setText(QCoreApplication.translate("TimerView", u"Message", None))
    # retranslateUi

