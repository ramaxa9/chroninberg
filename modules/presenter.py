from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QStackedWidget, QWidget

from UI.BlackView import Ui_BlackView
from UI.ClockView import Ui_ClockView
from UI.TimerView import Ui_TimerView


class ClockView(QWidget, Ui_ClockView):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class TimerView(QWidget, Ui_TimerView):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class BlackView(QWidget, Ui_BlackView):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class PresenterView(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle('Presenter view')

        palette = QPalette(Qt.black)

        self.setPalette(palette)

        self.layout().setSpacing(0)

        self.view_timer = TimerView()
        self.view_clock = ClockView()
        self.view_black = BlackView()

        self.addWidget(self.view_timer)
        self.addWidget(self.view_clock)
        self.addWidget(self.view_black)

    def update_timer(self, value):
        self.view_timer.lbl_timer.setText(value)

    def update_eta(self, value):
        self.view_timer.lbl_eta.setText(value)

    def update_clock(self, value):
        self.view_timer.lbl_clock.setText(value)
        self.view_clock.lbl_clock.setText(value)
