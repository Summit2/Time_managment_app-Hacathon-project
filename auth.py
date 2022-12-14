import json

from PySide6.QtCore import QSize, Signal, Qt
from PySide6.QtWidgets import QMainWindow, QLineEdit, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QPushButton


DARK_GREEN = '#61892F'
LIGHT_GREEN = '#86C232'
BLACK = '#222629'
DARK_GREY = '#474B4F'
LIGHT_GREY = '#6B6E70'


WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


class AuthWindow(QMainWindow):
    passed = Signal(str, dict)

    def __init__(self):
        super().__init__()
        # Параметры окна
        self.setMinimumSize(QSize(480, 320))
        self.setWindowTitle('Авторизация')

        # Добавление надписи
        self.title = QLabel('Введите имя пользователя')
        self.title.setAlignment(Qt.AlignCenter)
        # Добавление поля для ввода пароля
        self.login = QLineEdit()
        self.login.editingFinished.connect(self.check)
        # Добавление кнопки создания нового пользователя
        self.add_button = QPushButton('Добавить нового пользователя')
        self.add_button.clicked.connect(self.creteData)
        self.add_button.hide()
        self.login.textChanged.connect(self.hide_button)

        # Расположение всех элементов вертикально
        self.setCentralWidget(QWidget())
        self.layout = QVBoxLayout()
        self.layout.addStretch(1)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.login)
        self.layout.addWidget(self.add_button)
        self.layout.addStretch(1)

        # Добавление отступов побокам
        self.centering = QHBoxLayout(self.centralWidget())
        self.centering.addStretch(1)
        self.centering.addLayout(self.layout, 2)
        self.centering.addStretch(1)

        # Применение стилей
        self.setStyleSheet(
            f'''AuthWindow {{
                background-color: {BLACK}; 
                padding 20px
            }}
            QLabel {{
                background-color: {BLACK}; 
                color: white;
                padding: 6px;
                border-radius: 10px;
            }}
            QLineEdit {{
                background-color: {DARK_GREY}; 
                color: white;
                padding: 6px;
                border-radius: 10px;
            }}
            QPushButton {{
                background-color: {DARK_GREY}; 
                color: white;
                padding: 6px;
                border-radius: 10px;
            }}''')

    def check(self):
        """
        Проверка существования пользователя.\n
        Если пользователь существует откроется его записи.\n
        Если пользователя нет, то появится кнопка добавления пользователя.
        """
        try:
            file_name = "data/"+self.login.text()+".json"
            f = open(file_name)
            data = json.load(f)
            self.passed.emit(file_name, data)
            self.hide()
        except IOError:
            self.add_button.show()

    def creteData(self):
        """Добавление нового пользователя"""
        data = dict()
        data['Notes'] = dict()
        data['Schedule'] = {day: {'Odd': [], 'Even': []} for day in WEEKDAYS}
        file_name = "data/"+self.login.text()+".json"
        self.passed.emit(file_name, data)
        self.hide()

    def hide_button(self, *args):
        """Скрытие кнопки добавления пользователя при продолжении ввода логина"""
        self.add_button.hide()