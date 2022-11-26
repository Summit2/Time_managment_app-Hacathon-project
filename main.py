import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from schedule import Lesson, Schedule


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(480, 320))
        self.setBaseSize(QSize(960, 640))
        self.setCentralWidget(Schedule())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
