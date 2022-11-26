import json

from PySide6.QtCore import QSize, Signal
from PySide6.QtWidgets import QMainWindow, QLineEdit, QLabel, QVBoxLayout, QWidget


DARK_GREEN = '#61892F'
LIGHT_GREEN = '#86C232'
BLACK = '#222629'
DARK_GREY = '#474B4F'
LIGHT_GREY = '#6B6E70'


class AuthWindow(QMainWindow):
    passed = Signal(dict)

    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(480, 320))
        self.setWindowTitle('Авторизация')

        self.title = QLabel('Введите имя пользователя')
        self.login = QLineEdit()
        self.login.returnPressed.connect(self.check)

        self.setCentralWidget(QWidget())
        self.layout = QVBoxLayout(self.centralWidget())
        self.layout.addStretch(1)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.login)
        self.layout.addStretch(1)

        self.setStyleSheet(f'MainWindow {{background-color: {BLACK}; padding 20px}}')

    def check(self):
        try:
            file_name = "data/"+self.login.text()+".json"
            f = open(file_name)
            data = json.load(f)
            self.passed.emit(data)
            self.hide()
        except IOError:
            self.login.clear()

