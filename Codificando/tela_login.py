import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import mysql.connector


#con = mysql.connector.connect(host='project-kivia.cobnqddvfwys.us-east-1.rds.amazonaws.com',
#database='dev_uiq',
#user='mvictordb',
#password='Victor2004')


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
        self.window.resize(500, 600)
        self.window.setWindowIcon(QIcon('codificando/imgs/login.png'))
        self.window.setWindowTitle('Login and registration')

    def create_funcitions(self):
        self.button_login = QPushButton('Login', self.window)
        self.button_login.setStyleSheet('background-color:blue; color:white; border-radius:6; font-size: 15px')
        self.button_login.setGeometry(100, 100, 100, 50)

FrontEnd()
