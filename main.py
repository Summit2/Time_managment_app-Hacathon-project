import sys
import json

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from schedule import Lesson, Schedule


DARK_GREEN = '#61892F'
LIGHT_GREEN = '#86C232'
BLACK = '#222629'
DARK_GREY = '#474B4F'
LIGHT_GREY = '#6B6E70'


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(480, 320))
        self.setBaseSize(QSize(960, 640))
        with open('schedule.json') as f:
            schedule = json.load(f)
        schedule = schedule['Monday']
        self.setCentralWidget(Schedule(schedule))
        self.setStyleSheet(f'MainWindow {{background-color: {BLACK};}}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
