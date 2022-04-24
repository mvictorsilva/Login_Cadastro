import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

window = QApplication(sys.argv)
main_window = QWidget()

teste = QPushButton('teste', main_window)
teste.setStyleSheet(
    'display: inline-block;'
    'color: #ffffff'
    'text-decoration: none;'
    'padding: 3px solid #3c67e3;'
    'border-radius: 10px;'
)

main_window.show()
window.exec()
