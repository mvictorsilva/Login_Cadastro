import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt

def teste():
    variable = user_registration.text()

    print(variable)

    user_registration.close()

window = QApplication(sys.argv)
main_window = QWidget()

user_registration = QLineEdit('', main_window)
user_registration.setStyleSheet(
    'background-color: white;'
    'color: gray;'
    'border-radius: 20px;'
    'font: "Times New Roman";'
    'font-size: 17px;')
user_registration.setAlignment(Qt.AlignmentFlag.AlignCenter)
user_registration.setPlaceholderText('Create a user')
user_registration.setMaxLength(10)
user_registration.setGeometry(50, 150, 300, 40)

button_login = QPushButton('L O G I N', main_window)
button_login.setStyleSheet(
    'background-color: #00FF00;'
    'color: #ffffff;' 
    'border-radius: 6px;'
    'font: bold "Verdana";' 
    'font-size: 15px'
)
button_login.clicked.connect(teste)
button_login.setGeometry(70, 330, 100, 40)

main_window.show()
window.exec()
