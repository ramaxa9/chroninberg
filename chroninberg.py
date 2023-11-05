import socket
import sys

from PySide6.QtWidgets import QApplication

from UI.AbstractMainWindow import AbstractMainWindow
from modules.web_control import CommandHandler, ServerThread


class MainWindow(AbstractMainWindow):
    def __init__(self):
        super().__init__()

        self.command_handler = CommandHandler()
        self.server_thread = ServerThread(self.command_handler)
        self.server_thread.started.connect(self.on_server_started)
        self.server_thread.finished.connect(self.on_server_finished)

        # Web control
        self.command_handler.signal_handler.cmd_start.connect(self.time_remain.timer_start)
        self.command_handler.signal_handler.cmd_reset.connect(self.time_remain.timer_reset)
        self.command_handler.signal_handler.cmd_setTime.connect(self.time_remain.set_timer)

    def on_server_started(self):
        self.ui.lbl_network_status.setText('OK')
        self.ui.lbl_network_status.setStyleSheet('color: #90ff94;')

        self.ui.lbl_ipaddr.setStyleSheet('color: #90ff94;')
        ip_addr = socket.gethostbyname(socket.gethostname())

        print(f"[NETWORK] Server started {ip_addr}")
        self.ui.lbl_ipaddr.setText(f'http://{ip_addr}:5000/[command]')

    def on_server_finished(self):
        print("[NETWORK] Server stopped")
        self.ui.lbl_network_status.setText('Down')
        self.ui.lbl_network_status.setStyleSheet('color: #ff5040;')

    def closeEvent(self, event):
        self.command_handler.stop_server()
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # Start server
    window.server_thread.start()

    sys.exit(app.exec())
