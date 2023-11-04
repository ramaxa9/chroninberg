# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTextEdit,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1191, 781)
        self.verticalLayout_7 = QVBoxLayout(MainWindow)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.WindowTitle = QLabel(MainWindow)
        self.WindowTitle.setObjectName(u"WindowTitle")
        self.WindowTitle.setMinimumSize(QSize(0, 30))
        self.WindowTitle.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.WindowTitle.setFont(font)
        self.WindowTitle.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_7.addWidget(self.WindowTitle)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 0, 1, 1, 1)

        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.grp_time_timer = QGroupBox(self.widget)
        self.grp_time_timer.setObjectName(u"grp_time_timer")
        self.grp_time_timer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_3 = QVBoxLayout(self.grp_time_timer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.grp_time_timer)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.minutes = QSpinBox(self.grp_time_timer)
        self.minutes.setObjectName(u"minutes")
        font1 = QFont()
        font1.setPointSize(24)
        self.minutes.setFont(font1)
        self.minutes.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.minutes.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.minutes.setValue(15)

        self.verticalLayout_3.addWidget(self.minutes)

        self.btn_set = QPushButton(self.grp_time_timer)
        self.btn_set.setObjectName(u"btn_set")
        font2 = QFont()
        font2.setPointSize(16)
        self.btn_set.setFont(font2)

        self.verticalLayout_3.addWidget(self.btn_set)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.horizontalLayout_4.addWidget(self.grp_time_timer)

        self.grp_time_remain = QGroupBox(self.widget)
        self.grp_time_remain.setObjectName(u"grp_time_remain")
        self.horizontalLayout_10 = QHBoxLayout(self.grp_time_remain)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.btn_increase_5min = QPushButton(self.grp_time_remain)
        self.btn_increase_5min.setObjectName(u"btn_increase_5min")
        self.btn_increase_5min.setEnabled(False)
        self.btn_increase_5min.setMinimumSize(QSize(30, 50))
        icon = QIcon()
        icon.addFile(u":/app_icons/icons/chevrons-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_increase_5min.setIcon(icon)
        self.btn_increase_5min.setIconSize(QSize(30, 30))

        self.verticalLayout_8.addWidget(self.btn_increase_5min)

        self.label_2 = QLabel(self.grp_time_remain)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)

        self.btn_decrease_5min = QPushButton(self.grp_time_remain)
        self.btn_decrease_5min.setObjectName(u"btn_decrease_5min")
        self.btn_decrease_5min.setEnabled(False)
        self.btn_decrease_5min.setMinimumSize(QSize(30, 50))
        icon1 = QIcon()
        icon1.addFile(u":/app_icons/icons/chevrons-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_decrease_5min.setIcon(icon1)
        self.btn_decrease_5min.setIconSize(QSize(30, 30))

        self.verticalLayout_8.addWidget(self.btn_decrease_5min)


        self.horizontalLayout_10.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.btn_increase_1min = QPushButton(self.grp_time_remain)
        self.btn_increase_1min.setObjectName(u"btn_increase_1min")
        self.btn_increase_1min.setEnabled(False)
        self.btn_increase_1min.setMinimumSize(QSize(30, 50))
        icon2 = QIcon()
        icon2.addFile(u":/app_icons/icons/chevron-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_increase_1min.setIcon(icon2)
        self.btn_increase_1min.setIconSize(QSize(30, 30))

        self.verticalLayout_9.addWidget(self.btn_increase_1min)

        self.label_3 = QLabel(self.grp_time_remain)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_3)

        self.btn_decrease_1min = QPushButton(self.grp_time_remain)
        self.btn_decrease_1min.setObjectName(u"btn_decrease_1min")
        self.btn_decrease_1min.setEnabled(False)
        self.btn_decrease_1min.setMinimumSize(QSize(30, 50))
        icon3 = QIcon()
        icon3.addFile(u":/app_icons/icons/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_decrease_1min.setIcon(icon3)
        self.btn_decrease_1min.setIconSize(QSize(30, 30))

        self.verticalLayout_9.addWidget(self.btn_decrease_1min)


        self.horizontalLayout_10.addLayout(self.verticalLayout_9)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.lbl_time_remain = QLabel(self.grp_time_remain)
        self.lbl_time_remain.setObjectName(u"lbl_time_remain")
        self.lbl_time_remain.setMinimumSize(QSize(300, 0))
        font4 = QFont()
        font4.setFamilies([u"Tahoma"])
        font4.setPointSize(48)
        self.lbl_time_remain.setFont(font4)
        self.lbl_time_remain.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_time_remain)

        self.lbl_timer_set = QLabel(self.grp_time_remain)
        self.lbl_timer_set.setObjectName(u"lbl_timer_set")
        self.lbl_timer_set.setFont(font2)
        self.lbl_timer_set.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.lbl_timer_set)


        self.horizontalLayout_10.addLayout(self.verticalLayout_4)

        self.horizontalLayout_10.setStretch(2, 1)

        self.horizontalLayout_4.addWidget(self.grp_time_remain)

        self.grp_time_current = QGroupBox(self.widget)
        self.grp_time_current.setObjectName(u"grp_time_current")
        self.verticalLayout_5 = QVBoxLayout(self.grp_time_current)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_current_time = QLabel(self.grp_time_current)
        self.lbl_current_time.setObjectName(u"lbl_current_time")
        self.lbl_current_time.setFont(font4)
        self.lbl_current_time.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lbl_current_time)

        self.lbl_eta = QLabel(self.grp_time_current)
        self.lbl_eta.setObjectName(u"lbl_eta")
        self.lbl_eta.setFont(font2)
        self.lbl_eta.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.lbl_eta)


        self.horizontalLayout_4.addWidget(self.grp_time_current)

        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.layout_presets = QVBoxLayout(self.groupBox)
        self.layout_presets.setObjectName(u"layout_presets")
        self.layout_presets.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_5 = QGroupBox(self.widget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_start_timer = QPushButton(self.groupBox_5)
        self.btn_start_timer.setObjectName(u"btn_start_timer")
        self.btn_start_timer.setMinimumSize(QSize(100, 100))
        self.btn_start_timer.setMaximumSize(QSize(100, 100))
        font5 = QFont()
        font5.setPointSize(26)
        self.btn_start_timer.setFont(font5)

        self.horizontalLayout_9.addWidget(self.btn_start_timer)

        self.btn_reset_timer = QPushButton(self.groupBox_5)
        self.btn_reset_timer.setObjectName(u"btn_reset_timer")
        self.btn_reset_timer.setMinimumSize(QSize(100, 100))
        self.btn_reset_timer.setMaximumSize(QSize(100, 100))
        self.btn_reset_timer.setFont(font5)

        self.horizontalLayout_9.addWidget(self.btn_reset_timer)

        self.btn_pause_timer = QPushButton(self.groupBox_5)
        self.btn_pause_timer.setObjectName(u"btn_pause_timer")
        self.btn_pause_timer.setEnabled(False)
        self.btn_pause_timer.setMinimumSize(QSize(100, 100))
        self.btn_pause_timer.setMaximumSize(QSize(100, 100))
        self.btn_pause_timer.setFont(font5)

        self.horizontalLayout_9.addWidget(self.btn_pause_timer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.widget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(300, 0))
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_change_view_timer = QPushButton(self.groupBox_6)
        self.btn_change_view_timer.setObjectName(u"btn_change_view_timer")
        self.btn_change_view_timer.setFont(font2)
        self.btn_change_view_timer.setCheckable(True)
        self.btn_change_view_timer.setChecked(True)
        self.btn_change_view_timer.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.btn_change_view_timer)

        self.btn_change_view_clock = QPushButton(self.groupBox_6)
        self.btn_change_view_clock.setObjectName(u"btn_change_view_clock")
        self.btn_change_view_clock.setFont(font2)
        self.btn_change_view_clock.setCheckable(True)
        self.btn_change_view_clock.setChecked(False)
        self.btn_change_view_clock.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.btn_change_view_clock)

        self.btn_change_view_black = QPushButton(self.groupBox_6)
        self.btn_change_view_black.setObjectName(u"btn_change_view_black")
        self.btn_change_view_black.setFont(font2)
        self.btn_change_view_black.setCheckable(True)
        self.btn_change_view_black.setChecked(False)
        self.btn_change_view_black.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.btn_change_view_black)

        self.verticalSpacer_5 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.label_4 = QLabel(self.groupBox_6)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.btn_move_presenter_view = QPushButton(self.groupBox_6)
        self.btn_move_presenter_view.setObjectName(u"btn_move_presenter_view")

        self.horizontalLayout_5.addWidget(self.btn_move_presenter_view)

        self.select_screen = QComboBox(self.groupBox_6)
        self.select_screen.setObjectName(u"select_screen")

        self.horizontalLayout_5.addWidget(self.select_screen)

        self.btn_refresh_screeens = QPushButton(self.groupBox_6)
        self.btn_refresh_screeens.setObjectName(u"btn_refresh_screeens")

        self.horizontalLayout_5.addWidget(self.btn_refresh_screeens)

        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.horizontalLayout.addWidget(self.groupBox_6)

        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.txt_message = QTextEdit(self.groupBox_2)
        self.txt_message.setObjectName(u"txt_message")
        self.txt_message.setMinimumSize(QSize(0, 100))
        self.txt_message.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout_6.addWidget(self.txt_message)

        self.btn_message_send = QPushButton(self.groupBox_2)
        self.btn_message_send.setObjectName(u"btn_message_send")
        self.btn_message_send.setEnabled(True)
        self.btn_message_send.setMinimumSize(QSize(100, 100))
        self.btn_message_send.setMaximumSize(QSize(100, 100))
        self.btn_message_send.setFont(font2)
        self.btn_message_send.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.btn_message_send)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.lbl_message_hint = QLabel(self.groupBox_2)
        self.lbl_message_hint.setObjectName(u"lbl_message_hint")

        self.verticalLayout_10.addWidget(self.lbl_message_hint)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.StatusBar = QLabel(self.widget)
        self.StatusBar.setObjectName(u"StatusBar")
        self.StatusBar.setMinimumSize(QSize(0, 25))
        self.StatusBar.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout.addWidget(self.StatusBar)


        self.gridLayout.addWidget(self.widget, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Chroninberg", None))
        self.WindowTitle.setText(QCoreApplication.translate("MainWindow", u"Chroninberg Time Machine", None))
        self.grp_time_timer.setTitle(QCoreApplication.translate("MainWindow", u"Set duration", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Minutes", None))
        self.btn_set.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.grp_time_remain.setTitle(QCoreApplication.translate("MainWindow", u"Time remaining", None))
        self.btn_increase_5min.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"5min", None))
        self.btn_decrease_5min.setText("")
        self.btn_increase_1min.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"1min", None))
        self.btn_decrease_1min.setText("")
        self.lbl_time_remain.setText(QCoreApplication.translate("MainWindow", u"Remain", None))
        self.lbl_timer_set.setText(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.grp_time_current.setTitle(QCoreApplication.translate("MainWindow", u"Current time", None))
        self.lbl_current_time.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.lbl_eta.setText(QCoreApplication.translate("MainWindow", u"ETA", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Presets minutes", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Timer controls", None))
        self.btn_start_timer.setText("")
        self.btn_reset_timer.setText("")
        self.btn_pause_timer.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"View control", None))
        self.btn_change_view_timer.setText(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.btn_change_view_clock.setText(QCoreApplication.translate("MainWindow", u"Clock", None))
        self.btn_change_view_black.setText(QCoreApplication.translate("MainWindow", u"Black", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Screen selection", None))
        self.btn_move_presenter_view.setText(QCoreApplication.translate("MainWindow", u"Move to", None))
        self.btn_refresh_screeens.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_message_send.setText("")
        self.lbl_message_hint.setText(QCoreApplication.translate("MainWindow", u"Multiple lines can be invisible with different screen resolutions", None))
        self.StatusBar.setText(QCoreApplication.translate("MainWindow", u"StatusBar IP", None))
    # retranslateUi

