# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NetworkHelp.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QSpacerItem, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_network_help(object):
    def setupUi(self, network_help):
        if not network_help.objectName():
            network_help.setObjectName(u"network_help")
        network_help.resize(600, 727)
        network_help.setMinimumSize(QSize(600, 0))
        network_help.setMaximumSize(QSize(600, 16777215))
        icon = QIcon(QIcon.fromTheme(u"help-about"))
        network_help.setWindowIcon(icon)
        network_help.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(network_help)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.textBrowser = QTextBrowser(network_help)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)


        self.retranslateUi(network_help)

        QMetaObject.connectSlotsByName(network_help)
    # setupUi

    def retranslateUi(self, network_help):
        network_help.setWindowTitle(QCoreApplication.translate("network_help", u"Network commands", None))
        self.textBrowser.setHtml(QCoreApplication.translate("network_help", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Use </span><span style=\" font-size:14pt; font-weight:700;\">Generic: HTTP Requests</span><span style=\" font-size:14pt;\"> module in </span><span style=\" font-size:14pt; font-weight:700;\">Bitfocus Companion</span><span style=\" font-size:14pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; tex"
                        "t-indent:0px;\"><span style=\" font-size:14pt;\">Create new button and select </span><span style=\" font-size:14pt; color:#2d45c8;\">HTTP</span><span style=\" font-size:14pt;\"> &gt; </span><span style=\" font-size:14pt; color:#2d45c8;\">POST</span><span style=\" font-size:14pt;\"> for press action and paste command in to URL field</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Commands:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">[start timer]</span><span style=\" font-size:12pt;\"> http://127.0.0.1:5000/start</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; marg"
                        "in-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">[reset timer]</span><span style=\" font-size:12pt;\"> http://127.0.0.1:5000/reset</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">[set timer]</span><span style=\" font-size:12pt;\"> http://127.0.0.1:5000/set_timer?time=</span><span style=\" font-size:12pt; color:#5ca8cb;\">[time in minutes]</span></p></body></html>", None))
    # retranslateUi

