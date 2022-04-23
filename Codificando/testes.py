import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt

class FrontEnd():
    def __init__(self):
        super().__init__()
        self.create_window()
        self.create_funcitions()
        
        self.window.show()
        self.main_window.exec()

    def create_window(self):
        self.main_window = QApplication(sys.argv)
        self.window = QWidget()
        self.window.resize(400, 500)
        self.window.setWindowIcon(QIcon('codificando/imgs/login.png'))
        self.window.setWindowTitle('Login and registration')
        self.window.setStyleSheet(
            'background-color: qlineargradient(spread:pad, x1:0.484, y1:0, x2:0.521, y2:1, stop:0 rgba(0, 170, 250, 255), stop:1 rgba(0, 232, 254, 255));'
        )

    def primery_frame_login(self):
        