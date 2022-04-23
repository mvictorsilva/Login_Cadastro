import sys
from PyQt6.QtWidgets import QApplication, QWidget

class FrontEnd():
    def __init__(self):
        super().__init__()
        self.create_window()

    def create_window(self):
        self.application(sys.argv)
        self.windows = QWidget()
        self.windows.resizable(500, 400)
        self.setWindowTitle('Login')
        self.window.show()
        self.application.exec()

FrontEnd()
