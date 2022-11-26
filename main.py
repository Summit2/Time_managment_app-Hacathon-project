import sys
import json

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication

from manager import Manager
from Calendar import CalendarWindow


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
        self.setWindowTitle('Заметки')

        with open('data.json', encoding="UTF-8") as f:
            self.data = json.load(f)

        self.calendar = CalendarWindow()

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

        self.changeDay('22.11.2022', 'Odd')

    def closeEvent(self, event):
        """Сохранение данных при закрытии"""
        with open('data.json', 'w', encoding='UTF-8') as f:
            json.dump(self.data, f)

    def changeDay(self, date, even):
        """Обновить данные для указанного дня"""
        day_of_the_week = "Tuesday"

        schedule = self.data['Schedule'][day_of_the_week][even]
        if self.data['Notes'].get(date) is None:
            self.data['Notes'][date] = dict()
        notes = self.data['Notes'][date]
        self.manager.chageRecords(schedule, notes)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
