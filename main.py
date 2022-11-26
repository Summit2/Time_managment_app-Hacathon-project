import sys
import json

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication

from manager import Manager
from Calendar import CalendarWindow
from auth import AuthWindow


DARK_GREEN = '#61892F'
LIGHT_GREEN = '#86C232'
BLACK = '#222629'
DARK_GREY = '#474B4F'
LIGHT_GREY = '#6B6E70'


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(480, 320))
        self.resize(QSize(960, 640))
        self.setWindowTitle('Заметки')
        self.data = {}

        self.auth = AuthWindow()
        self.auth.passed.connect(self.start)
        self.auth.show()

        self.calendar = CalendarWindow()
        self.calendar.date_selected.connect(self.changeDay)

        self.c_button = QPushButton('Календарь')
        self.c_button.setStyleSheet(
            f'''QPushButton {{
                    background-color: {DARK_GREY}; 
                    color: white; 
                    border-radius: 10px;
                    padding: 5px;
                }}''')
        self.c_button.clicked.connect(self.calendar.show)

        self.manager = Manager()

        self.setCentralWidget(QWidget())
        self.layout = QVBoxLayout(self.centralWidget())
        self.layout.addWidget(self.c_button)
        self.layout.addWidget(self.manager)
        self.setStyleSheet(f'MainWindow {{background-color: {BLACK};}}')

    def closeEvent(self, event):
        """Сохранение данных при закрытии"""
        with open('data.json', 'w', encoding='UTF-8') as f:
            json.dump(self.data, f)

    def changeDay(self, date, day_of_the_week, even):
        """Обновить данные для указанного дня"""
        schedule = self.data['Schedule'][day_of_the_week][even]
        if self.data['Notes'].get(date) is None:
            self.data['Notes'][date] = dict()
        notes = self.data['Notes'][date]
        self.manager.chageRecords(schedule, notes)

    def start(self, data):
        self.data = data
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
