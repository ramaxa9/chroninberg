import os.path

import qtawesome as qta
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication
from qframelesswindow import FramelessWindow, StandardTitleBar

from UI.MainWindow import Ui_MainWindow
from modules.clock import Clock, TimeRemaining
from modules.network_help import NetworkHelpDialog
from modules.presenter import PresenterView
from modules.presets import PresetsWidget


class AbstractMainWindow(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setTitleBar(StandardTitleBar(self))
        self.titleBar.raise_()
        self.resize(1000, 650)

        qss = open(os.path.join('UI', 'Dark.qss')).read()
        self.setStyleSheet(qss)

        self.network_help_dialog = NetworkHelpDialog()

        self.presenter_view = PresenterView()
        self.presenter_view.showMaximized()

        self.grp_presets = PresetsWidget(self.ui.lbl_timer_set)
        self.ui.layout_presets.addWidget(self.grp_presets)

        self.ui.lbl_time_remain.setText('15:00')
        self.ui.lbl_timer_set.setText('15:00')

        self.clock = Clock(self.ui.lbl_current_time, self.presenter_view)
        self.time_remain = TimeRemaining(self.ui.lbl_time_remain, self.ui.lbl_eta, self.ui.lbl_timer_set, self.ui.lbl_timer_set.text(), self.presenter_view)

        self.ui.btn_refresh_screeens.setIcon(qta.icon('mdi6.reload', color='white'))
        self.ui.btn_refresh_screeens.setIconSize(QSize(24, 24))
        self.ui.btn_refresh_screeens.setMaximumSize(30, 30)

        self.ui.btn_increase_1min.setIcon(qta.icon('mdi6.chevron-up', color='white'))
        self.ui.btn_increase_1min.setIconSize(QSize(24, 24))
        self.ui.btn_increase_1min.setMaximumSize(30, 30)
        self.ui.btn_increase_1min.setMinimumSize(30, 30)

        self.ui.btn_decrease_1min.setIcon(qta.icon('mdi6.chevron-down', color='white'))
        self.ui.btn_decrease_1min.setIconSize(QSize(24, 24))
        self.ui.btn_decrease_1min.setMaximumSize(30, 30)
        self.ui.btn_decrease_1min.setMinimumSize(30, 30)

        self.ui.btn_increase_5min.setIcon(qta.icon('mdi6.chevron-triple-up', color='white'))
        self.ui.btn_increase_5min.setIconSize(QSize(24, 24))
        self.ui.btn_increase_5min.setMaximumSize(30, 30)
        self.ui.btn_increase_5min.setMinimumSize(30, 30)

        self.ui.btn_decrease_5min.setIcon(qta.icon('mdi6.chevron-triple-down', color='white'))
        self.ui.btn_decrease_5min.setIconSize(QSize(24, 24))
        self.ui.btn_decrease_5min.setMaximumSize(30, 30)
        self.ui.btn_decrease_5min.setMinimumSize(30, 30)

        self.ui.btn_start_timer.setIcon(qta.icon('mdi6.play', color='white'))
        self.ui.btn_start_timer.setIconSize(QSize(64, 64))

        self.ui.btn_reset_timer.setIcon(qta.icon('mdi6.reload', color='white'))
        self.ui.btn_reset_timer.setIconSize(QSize(64, 64))

        self.ui.btn_pause_timer.setIcon(qta.icon('mdi6.pause', color='white'))
        self.ui.btn_pause_timer.setIconSize(QSize(64, 64))

        self.ui.btn_message_send.setIcon(qta.icon('fa.send', color='white'))
        self.ui.btn_message_send.setIconSize(QSize(64, 64))

        # self.ui.btn_decrease_5min.setMaximumSize(30, 30)
        # self.ui.btn_decrease_5min.setMinimumSize(30, 30)

        self.get_screens()

        self.move_presenter_view(1)

        # SIGNALS
        self.ui.btn_start_timer.clicked.connect(self.time_remain.timer_start)
        self.ui.btn_pause_timer.clicked.connect(self.time_remain.timer_pause)
        self.ui.btn_reset_timer.clicked.connect(self.time_remain.timer_reset)
        self.ui.btn_set.clicked.connect(lambda: self.time_remain.set_timer(f'{self.ui.minutes.value()}:00'))

        self.ui.btn_change_view_timer.clicked.connect(lambda: self.presenter_view.setCurrentIndex(0))
        self.ui.btn_change_view_clock.clicked.connect(lambda: self.presenter_view.setCurrentIndex(1))
        self.ui.btn_change_view_black.clicked.connect(lambda: self.presenter_view.setCurrentIndex(2))
        self.ui.btn_move_presenter_view.clicked.connect(self.move_presenter_view)
        self.ui.btn_refresh_screeens.clicked.connect(self.get_screens)
        self.ui.btn_message_send.clicked.connect(self.send_message)
        self.ui.btn_network_help.clicked.connect(self.show_network_help)

        # Presenter view update
        # self.ui.lbl_current_time.textChanged.connect(lambda: self.presenter_view.update_clock(self.ui.lbl_current_time.text()))

    def show_network_help(self):
        self.network_help_dialog.show()

    def send_message(self):
        if not self.ui.btn_message_send.isChecked():
            self.presenter_view.view_timer.lbl_message.clear()
        else:
            self.presenter_view.view_timer.lbl_message.setText(self.ui.txt_message.toPlainText())

    def get_screens(self):
        self.ui.select_screen.clear()
        screens = QApplication.screens()
        for screen in screens:
            self.ui.select_screen.addItem(screen.name())

    def move_presenter_view(self, monitor: int = None):
        if monitor:
            screen = monitor
            self.ui.select_screen.setCurrentIndex(screen)
        else:
            screen = self.ui.select_screen.currentIndex()

        self.presenter_view.showNormal()
        screenGeometry = QApplication.screens()[screen].geometry()

        self.presenter_view.move(screenGeometry.left(), screenGeometry.top())
        self.presenter_view.showMaximized()
