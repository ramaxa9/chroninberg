import os.path
import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QWidget, QApplication

from UI.AbstractMainWindow import AbstractMainWindow
from UI.MainWindow import Ui_MainWindow
from modules.clock import Clock, TimeRemaining

import qtawesome as qta
from qframelesswindow import FramelessWindow, StandardTitleBar

from modules.presenter import PresenterView


class MainWindow(AbstractMainWindow):
    def __init__(self):
        super().__init__()

    def closeEvent(self, event):
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())
