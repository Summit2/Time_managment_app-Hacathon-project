import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


DARK_GREEN = '#61892F'
LIGHT_GREEN = '#86C232'
BLACK = '#222629'
DARK_GREY = '#474B4F'
LIGHT_GREY = '#6B6E70'


class Lesson(QWidget):
    noteChanged = Signal(str, str)

    def __init__(self, index, name, time, notes):
        super().__init__()
        self.index = index
        self.notes = notes

        self.time = QLabel(time)
        self.time.setWordWrap(True)
        self.time_layout = QHBoxLayout()
        self.time_layout.addWidget(self.time)
        self.time_layout.addStretch(0)

        self.v_layout = QVBoxLayout()
        self.name = QLabel(name)
        self.name.setWordWrap(True)
        self.v_layout.addWidget(self.name)
        self.v_layout.addLayout(self.time_layout)
        self.v_layout.addStretch(0)

        self.text = QTextEdit(notes.get(index, ''))
        self.text.textChanged.connect(self.Changed)
        # self.text.setWordWrap(True)
        self.h_layout = QHBoxLayout(self)
        self.h_layout.addLayout(self.v_layout, 1)
        self.h_layout.addWidget(self.text, 3)

        # self.setAutoFillBackground(True)
        # palette = self.palette()
        # palette.setColor(QPalette.ColorRole.Window, DARK_GREY)
        # self.setPalette(palette)

    def Changed(self):
        self.notes[self.index] = self.text.toPlainText()


class Manager(QWidget):
    def __init__(self, schedule, notes):
        super().__init__()

        self.lessons = QVBoxLayout(self)
        for rec in schedule:
            self.lessons.addWidget(Lesson(str(rec['index']), rec['name'], rec['time'], notes))

        self.setStyleSheet(
            f'''QLabel {{
            background-color: {DARK_GREY}; 
            color: white;
            padding: 6px;
            border-radius: 10px;
            }}
            QTextEdit {{
            background-color: {DARK_GREY}; 
            color: white;
            padding: 6px;
            border-radius: 10px;
            }}''')
