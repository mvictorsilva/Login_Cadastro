import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import mysql.connector


class BackEnd():
    def connecting_db(self):
        self.connect = mysql.connector.connect(
        )
        self.cursor = self.connect.cursor()
    
    def disconnecting_db(self):
        self.connect.close()

    def clear_editext_register(self):
        self.user_registration.clear()
        self.email_registration.clear()
        self.password_registration.clear()

    def variables(self):
        self.user = self.user_registration.text()
        self.email = self.email_registration.text()
        self.password = self.password_registration.text()

    def new_account(self):
        self.connecting_db()
        self.variables()

        if self.user == '':
            self.insert_something = QLabel('Please enter a username.', self.register)
            self.insert_something.setStyleSheet(
                'background-color: #01E1FD;'
                'color: #4F4F4F;'
                'font-size: 15px;'
            )
            self.insert_something.setGeometry(90, 430, 250, 30)
            self.insert_something.show()

        elif self.email == '':
            self.insert_something_i = QLabel('Please enter a valid email address.', self.register)
            self.insert_something_i.setStyleSheet(
                'background-color: #01E1FD;'
                'color: #4F4F4F;'
                'font-size: 15px;'
            )
            self.insert_something_i.setGeometry(90, 430, 250, 30)
            self.insert_something_i.show()

        elif self.password == '':
            self.insert_something_ii = QLabel('Please enter a password.', self.register)
            self.insert_something_ii.setStyleSheet(
                'background-color: #01E1FD;'
                'color: #4F4F4F;'
                'font-size: 15px;'
            )
            self.insert_something_ii.setGeometry(90, 430, 250, 30)
            self.insert_something_ii.show()

        else:

            self.cursor.execute("""
                insert into cadastrados(usuario, email, senha)
                values (%s, %s, %s)
                """,
                (
                    self.user,
                    self.email,
                    self.password
                )
            )
            self.connect.commit(),
            self.clear_editext_register()
            self.disconnecting_db()
            
            self.confirmation = QLabel('✔️ Registered user!', self.register)
            self.confirmation.setStyleSheet(
                'background-color: #01E1FD;'
                'color: #4F4F4F;'
                'font-size: 15px;'
            )
            self.confirmation.setGeometry(90, 430, 210, 30)
            self.confirmation.show()

            self.sigin_registred = QPushButton('Sig Up', self.register)
            self.sigin_registred.setStyleSheet(
                'border: none;'
                'background-color: #01E1FD;'
                'color: white;'
                'font: "Helvetica";'
                'font-size: 15px;'
            )
            self.sigin_registred.setGeometry(220, 431, 100, 30)
            self.sigin_registred.clicked.connect(lambda: self.register.close())
            self.sigin_registred.show()

    def frame_confirmation(self):
        self.confirmation_login = QFrame(self.window)
        self.confirmation_login.resize(400, 500)
        self.confirmation_login.setStyleSheet('background-color: qlineargradient(spread:pad, x1:0.484, y1:0, x2:0.521, y2:1, stop:0 rgba(0, 170, 250, 255), stop:1 rgba(0, 232, 254, 255));')
        self.confirmation_login.show()

        self.verific = QLabel('Congratulations', self.confirmation_login)
        self.verific.setStyleSheet(
            'background-color: none;'
            'color: #E0FFFF;'
            'font-size: 25px;'
            'font: Regular "Times New Roman";'
        )
        self.verific.setGeometry(120, 70, 160, 50)
        self.verific.show()

    def validate_user(self):
        self.connecting_db()
        self.user_typed = self.user_login.text()
        self.password_typed = self.password_login.text()

        if self.user_typed == '':
            print('digite')
        elif self.password_typed == '':
            print('digite')
        else:
            try:
                self.cursor.execute(f"""
                        select senha from cadastrados where usuario = '{self.user_typed}'
                    """)
                self.password_db = self.cursor.fetchall()

                if self.password_typed == self.password_db[0][0]:
                    self.frame_confirmation()
                else:
                    print('error')
            except:
                self.incorret = QLabel('Incorrect password or username', self.window)
                self.incorret.setStyleSheet(
                    'background-color: none;'
                    'color: red;'
                    'border-radius: 20px;'
                    'font-size: 15px;'
                )
                self.incorret.setGeometry(95, 110, 250, 50)
                self.incorret.show()

            self.disconnecting_db()

class FrontEnd(BackEnd):
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
        self.window.setFixedSize(400, 500)
        self.window.setWindowIcon(QIcon('codificando/imgs/login.png'))
        self.window.setWindowTitle('Login and registration')
        self.window.setStyleSheet('background-color: qlineargradient(spread:pad, x1:0.484, y1:0, x2:0.521, y2:1, stop:0 rgba(0, 170, 250, 255), stop:1 rgba(0, 232, 254, 255));')

    def frame_register(self):
        self.register = QFrame(self.window)
        self.register.resize(400, 500)
        self.register.setStyleSheet('background-color:qlineargradient(spread:pad, x1:0.484, y1:0, x2:0.521, y2:1,stop:0 rgba(0, 170, 250, 255), stop:1 rgba(0, 232, 254, 255));')
        self.register.show()

        self.title_register = QLabel('R E G I S T E R', self.register)
        self.title_register.setStyleSheet(
            'background-color: none;'
            'color: #E0FFFF;'
            'font-size: 25px;'
            'font: Regular "Times New Roman";'
        )
        self.title_register.setGeometry(120, 70, 160, 50)
        self.title_register.show()

        self.user_registration = QLineEdit('', self.register)
        self.user_registration.setStyleSheet(
            'background-color: white;'
            'color: gray;'
            'border-radius: 20px;'
            'font: "Times New Roman";'
            'font-size: 17px;')
        self.user_registration.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.user_registration.setPlaceholderText('Create a user')
        self.user_registration.setMaxLength(10)
        self.user_registration.setGeometry(50, 150, 300, 40)
        self.user_registration.show()

        self.email_registration = QLineEdit('', self.register)
        self.email_registration.setStyleSheet(
            'background-color: white;'
            'color: gray;'
            'border-radius: 20px;'
            'font: "Times New Roman";'
            'font-size: 17px;')
        self.email_registration.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.email_registration.setPlaceholderText('E-mail')
        self.email_registration.setGeometry(50, 220, 300, 40)
        self.email_registration.show()

        self.password_registration = QLineEdit('', self.register)
        self.password_registration.setStyleSheet(
            'background-color: white;'
            'color: gray;'
            'border-radius: 20px;'
            'font: "Times New Roman";'
            'font-size: 17px;')
        self.password_registration.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password_registration.setPlaceholderText('Password')
        self.password_registration.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_registration.setMaxLength(8)
        self.password_registration.setGeometry(50, 290, 300, 40)
        self.password_registration.show()

        self.create_user = QPushButton('C R E A T E', self.register)
        self.create_user.setStyleSheet(
            'background-color: #00FF00;'
            'color: #ffffff;' 
            'border-radius: 6px;'
            'font: bold "Verdana";' 
            'font-size: 15px'

        )
        self.create_user.setGeometry(150, 360, 100, 40)
        self.create_user.clicked.connect(self.new_account)
        self.create_user.show()

    def frame_login(self):
        ##title
        self.title = QLabel('W E L C O M E', self.window)
        self.title.setStyleSheet(
            'background-color: none;'
            'color: #E0FFFF;'
            'font-size: 25px;'
            'font: Regular "Times New Roman";'
        )
        self.title.setGeometry(120, 70, 160, 50)

        #Receive the email
        self.user_login = QLineEdit('', self.window)
        self.user_login.setStyleSheet(
            'background-color: #ffffff;'
            'color: gray;'
            'border-radius: 20px;'
            'font: "Times New Roman";'
            'font-size: 17px;')
        self.user_login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.user_login.setPlaceholderText('User')
        self.user_login.setMaxLength(10)
        self.user_login.setGeometry(50, 150, 300, 40)

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
        self.password_login.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_login.setMaxLength(8)
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
        self.button_login.clicked.connect(self.validate_user)
        self.button_login.setGeometry(70, 310, 100, 40)

        #No account label and button
        self.register_label = QLabel('No account?', self.window)
        self.register_label.setStyleSheet(
            'color: #4F4F4F;'
            'font-size: 15px;'
            'font: "Helvetica";'
            'background-color: none;'
        )
        self.register_label.setGeometry(190, 305, 100, 50)

        self.register_button = QPushButton('Sig up', self.window)
        self.register_button.setStyleSheet(
            'border: none;'
            'background-color: none;'
            'color: white;'
            'font: "Helvetica";'
            'font-size: 15px;'
        )
        self.register_button.setGeometry(270, 315, 60, 30)
        self.register_button.clicked.connect(self.frame_register)

        """ self.remember = QCheckBox('Remember user', self.window)
        self.remember.setStyleSheet(
            'background-color: none;'
            'font: "Helvetica";'
            'font-size: 15px;'
            'color: #4F4F4F'
        )
        self.remember.setGeometry(60, 260, 160, 50) """

FrontEnd()
