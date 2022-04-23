import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
import mysql.connector


#con = mysql.connector.connect(host='project-kivia.cobnqddvfwys.us-east-1.rds.amazonaws.com',
#database='dev_uiq',
#user='mvictordb',
#password='Victor2004')


class FrontEnd():
    def __init__(self):
        super().__init__()
        self.create_window()
        self.frame_login()
        
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

    def frame_login(self):
        ##title
        self.title = QLabel('W E L C O M E', self.window)
        self.title.setStyleSheet(
            'background-color: none;'
            'color: #E0FFFF;'
            'font-size: 25px;'
            'font: "Times New Roman";'
        )
        self.title.setGeometry(120, 70, 160, 50)

        #Receive the email
        self.email_login = QLineEdit('', self.window)
        self.email_login.setStyleSheet(
            'background-color: white;'
            'color: gray;'
            'border-radius: 20px;'
            'font: "Times New Roman";'
            'font-size: 17px;')
        self.email_login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.email_login.setPlaceholderText('E-mail')
        self.email_login.setGeometry(50, 150, 300, 40)

        #Receive the password
        self.password_login = QLineEdit('', self.window)
        self.password_login.setStyleSheet(
            'background-color: white;'
            'color: gray;'
            'border-radius: 20px;'
            'font: "Times New Roman";'
            'font-size: 17px;')
        self.password_login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password_login.setPlaceholderText('Password')
        self.password_login.setGeometry(50, 220, 300, 40)

        #login
        self.button_login = QPushButton('L O G I N', self.window)
        self.button_login.setStyleSheet(
            'background-color: #00FF00;'
            'color: #ffffff;' 
            'border-radius: 6px;'
            'font: bold "Verdana";' 
            'font-size: 15px'
        )
        self.button_login.setGeometry(70, 330, 100, 50)

        #No account label and button
        self.register_label = QLabel('No account?', self.window)
        self.register_label.setStyleSheet(
            'color: #4F4F4F;'
            'font-size: 15px;'
            'font: "Helvetica";'
            'background-color: none;'
        )
        self.register_label.setGeometry(190, 330, 100, 50)

        self.register_button = QPushButton('Sig up', self.window)
        self.register_button.setStyleSheet(
            'border: none;'
            'background-color: none;'
            'color: white;'
            'font: "Helvetica";'
            'font-size: 15px;'
        )
        self.register_button.setGeometry(270, 340, 60, 30)

        self.remember = QCheckBox('Remember user', self.window)
        self.remember.setStyleSheet(
            'background-color: none;'
            'font: "Helvetica";'
            'font-size: 15px;'
            'color: #4F4F4F'
        )
        self.remember.setGeometry(60, 260, 160, 50)

FrontEnd()
