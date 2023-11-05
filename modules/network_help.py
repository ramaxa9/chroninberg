from PySide6.QtCore import Qt
from qframelesswindow import FramelessWindow, StandardTitleBar

from UI.NetworkHelp import Ui_network_help


class NetworkHelpDialog(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_network_help()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setStyleSheet(self.styleSheet() + "#network_help{ background-color: grey; border:1 solid black ; "
                                               "border-radius: 25px;}")

        self.setTitleBar(StandardTitleBar(self))
        self.titleBar.raise_()

