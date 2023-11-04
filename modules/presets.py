from PySide6.QtWidgets import QWidget, QLabel

from UI.Presets import Ui_Presets


class PresetsWidget(QWidget, Ui_Presets):
    def __init__(self, label: QLabel):
        super().__init__()
        self.setupUi(self)

        self.lbl_timer = label

        self.btn_preset_1.clicked.connect(lambda: self.set_timer(5))
        self.btn_preset_2.clicked.connect(lambda: self.set_timer(10))
        self.btn_preset_3.clicked.connect(lambda: self.set_timer(15))
        self.btn_preset_4.clicked.connect(lambda: self.set_timer(20))
        self.btn_preset_5.clicked.connect(lambda: self.set_timer(25))
        self.btn_preset_6.clicked.connect(lambda: self.set_timer(30))
        self.btn_preset_7.clicked.connect(lambda: self.set_timer(35))
        self.btn_preset_8.clicked.connect(lambda: self.set_timer(40))
        self.btn_preset_9.clicked.connect(lambda: self.set_timer(45))
        self.btn_preset_10.clicked.connect(lambda: self.set_timer(50))
        self.btn_preset_11.clicked.connect(lambda: self.set_timer(55))
        self.btn_preset_12.clicked.connect(lambda: self.set_timer(60))

    def set_timer(self, m: int):
        timer = f'{m}:00'
        self.lbl_timer.setText(timer)
