import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class Lesson(QWidget):
    def __init__(self):
        super().__init__()
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(Color('blue'))
        self.v_layout.addWidget(Color('green'))

        self.h_layout = QHBoxLayout(self)
        self.h_layout.addLayout(self.v_layout)
        self.h_layout.addWidget(Color('red'))


class Schedule(QWidget):
    def __init__(self):
        super().__init__()
        self.lessons = QVBoxLayout(self)
        for i in range(5):
            self.lessons.addWidget(Lesson())
