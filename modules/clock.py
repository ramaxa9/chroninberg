from PySide6.QtCore import QTimer, QTime, Slot, QObject
from PySide6.QtGui import Qt, QPalette, QColor
from PySide6.QtWidgets import QLabel, QWidget, QHBoxLayout, QSpinBox, QVBoxLayout, QPushButton

from modules.presenter import PresenterView


class TimeDisplayWidget(QLabel):
    def __init__(self):
        super().__init__()

        # self.resize(250, 60)
        # self.setMinimumSize(250, 60)

        self.setStyleSheet("TimeDisplayWidget {color: gray;\nfont: 48pt 'Tahoma';}")
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)


class Clock(QObject):
    def __init__(self, label: QLabel, presenter_view: PresenterView):
        super().__init__()

        self.label = label
        self.presenter_view = presenter_view
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)

        self.show_time()

    @Slot()
    def show_time(self):
        time = QTime.currentTime()
        text = time.toString("hh:mm:ss")
        #
        # # Blinking effect
        # if (time.second() % 2) == 0:
        #     text = text.replace(":", " ")
        self.presenter_view.view_timer.lbl_clock.setText(text)
        self.presenter_view.view_clock.lbl_clock.setText(text)
        self.label.setText(text)


class TimeRemaining(QWidget):
    def __init__(self, lbl_time_remain: QLabel, lbl_time_eta: QLabel, lbl_timer_set: QLabel, timer, presenter_view: PresenterView):
        super().__init__()

        self.lbl_time_remain = lbl_time_remain
        self.lbl_time_eta = lbl_time_eta
        self.lbl_timer_set = lbl_timer_set
        self.presenter_view = presenter_view

        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_update)
        # self.timer.timeout()
        self.finish_time = QTime()

        self.extra_timer = QTimer()
        self.extra_timer.timeout.connect(self.timer_extra_update)
        self.extra_time = QTime()

        self.paused = True
        self.set_timer(timer)

    def set_timer(self, timer):
        if type(timer) == int:
            timer = f'{timer}:00'
        self.lbl_time_remain.setText(timer)
        self.lbl_timer_set.setText(timer)
        self.presenter_view.view_timer.lbl_timer.setText(timer)

        value = timer.split(':')
        seconds = int(value[0]) * 60
        self.presenter_view.view_timer.timer_progress.setMinimum(0)
        self.presenter_view.view_timer.timer_progress.setMaximum(seconds)
        self.presenter_view.view_timer.timer_progress.setValue(seconds)

    def timer_start(self):
        minutes = int(self.lbl_timer_set.text().split(':')[0])

        # h = int(new_value[0]) // 60
        # m = int(new_value[1]) % 60
        self.finish_time = QTime.currentTime().addSecs(minutes * 60)  # Calculate finish time
        timer = '{m}:00'.format(m=minutes)
        eta = f'ETA: {self.finish_time.toString()}'

        self.lbl_time_remain.setText(timer)
        self.presenter_view.view_timer.lbl_timer.setText(timer)

        self.lbl_time_eta.setText(eta)
        self.presenter_view.view_timer.lbl_eta.setText(eta)

        self.presenter_view.view_timer.lbl_message.setText('')

        self.timer.start(1000)
        self.paused = False

    def timer_pause(self):
        if self.paused:
            self.timer.start(1000)
            self.finish_time = QTime.currentTime().addSecs(self.timer.remainingTime() // 1000)
            self.lbl_time_eta.setText(f'ETA: {self.finish_time.toString()}')
            self.extra_timer.stop()
        else:
            self.timer.stop()
            if self.finish_time > QTime.currentTime():
                self.extra_time = QTime(0, 0)
                self.extra_timer.start(1000)
        self.paused = not self.paused

    def timer_reset(self):
        self.timer.stop()
        self.extra_timer.stop()
        self.lbl_time_remain.setPalette(self.lbl_time_eta.palette())
        self.presenter_view.view_timer.lbl_timer.setStyleSheet('color: rgb(0, 255, 0);')
        self.paused = False

        self.set_timer(self.lbl_timer_set.text())
        self.lbl_time_eta.setText('ETA: N/A')
        self.presenter_view.view_timer.lbl_eta.setText('ETA: N/A')

    def timer_update(self):
        # Update the timer
        remaining_time = self.lbl_time_remain.text().split(':')
        minutes = int(remaining_time[0])
        seconds = int(remaining_time[1])

        if seconds == 0:
            if minutes == 0:
                self.timer.stop()
                self.extra_time = QTime(0, 0)
                self.extra_timer.start(1000)
                return
            minutes -= 1
            seconds = 59
        else:
            seconds -= 1

        timer = f'{minutes:02d}:{seconds:02d}'

        self.lbl_time_remain.setText(timer)
        self.presenter_view.view_timer.lbl_timer.setText(timer)
        maximum = self.presenter_view.view_timer.timer_progress.maximum()
        # seconds = minutes * 60
        seconds = minutes * 60 + seconds
        left = maximum - (maximum - seconds)
        self.presenter_view.view_timer.timer_progress.setValue(left)

    def timer_extra_update(self):
        # Update the extra timer after main timer ends
        self.extra_time = self.extra_time.addSecs(1)
        self.lbl_time_remain.setText(f'-{self.extra_time.toString()}')
        palette = QPalette()
        palette.setColor(QPalette.WindowText, QColor("red"))
        self.presenter_view.view_timer.lbl_timer.setStyleSheet('color: red;')
        self.lbl_time_remain.setPalette(palette)


class TSpinBox(QSpinBox):
    def __init__(self):
        super().__init__()

        self.setStyleSheet('TSpinBox { font-size: 24pt }')
        self.setMaximum(60)

        self.valueChanged.connect(self.zeroing)

    def zeroing(self):
        if self.value() == 60:
            self.setValue(0)


class Timer(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        layout.addLayout(layout1)
        layout.addLayout(layout2)

        self.setLayout(layout)
        self.h = TSpinBox()
        self.m = TSpinBox()
        self.m.setValue(15)

        self.btn_set_time = QPushButton('Set')
        layout.addWidget(self.btn_set_time)

        layout1.addWidget(QLabel('Hours'))
        layout1.addWidget(QLabel('Minutes'))

        layout2.addWidget(self.h)
        layout2.addWidget(self.m)

        self.h.valueChanged.connect(self.new_value)
        self.m.valueChanged.connect(self.new_value)

    def new_value(self):
        new_value = self.h.value() * 60 + self.m.value()

        h = new_value // 60
        m = new_value % 60
        to_string = '{h}:{m}'.format(h=h, m=m)

        return new_value, to_string
