import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


DARK_GREEN = '#61892F'
LIGHT_GREEN = '#86C232'
BLACK = '#222629'
DARK_GREY = '#474B4F'
LIGHT_GREY = '#6B6E70'


class Color(QAbstractButton):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, DARK_GREY)
        self.setPalette(palette)


class Lesson(QWidget):
    def __init__(self, data):
        super().__init__()
        self.time_layout = QHBoxLayout()
        self.time_layout.addWidget(QLabel(data['time']))
        self.time_layout.addStretch(1)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(QLabel(data['name']))
        self.v_layout.addLayout(self.time_layout)
        self.v_layout.addStretch(1)

        self.h_layout = QHBoxLayout(self)
        self.h_layout.addLayout(self.v_layout)
        self.h_layout.addWidget(QLabel(data['text']), 10)

        # self.setAutoFillBackground(True)
        # palette = self.palette()
        # palette.setColor(QPalette.ColorRole.Window, DARK_GREY)
        # self.setPalette(palette)


class Schedule(QWidget):
    def __init__(self, schedule):
        super().__init__()
        self.lessons = QVBoxLayout(self)
        for lesson in schedule:
            self.lessons.addWidget(Lesson(lesson))

        self.setStyleSheet(
            f'''QLabel {{
            background-color: {DARK_GREY}; 
            color: white;
            padding: 6px;
            border-radius: 10px;
            }}''')
