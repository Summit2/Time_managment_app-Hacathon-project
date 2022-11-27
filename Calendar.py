import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import *
import PySide6.QtGui
from PySide6.QtWidgets import QCalendarWidget,QApplication, QPushButton
import datetime


def Is_Week_Even_Or_Odd(date):
    '''
    Функция возвращает четность или нечетность недели
    (числитель (Odd) или знаменатель (Even))
    :return:
    '''
    september=datetime.date(QDate.year(date),9,1).isocalendar()[1]
    even_or_odd=september%2 #если september четная, то 0, иначе 1
    result = abs(september-Week_Number(date))%2  # 0 если недели совпадают по четности, иначе 1
    if result==1:
        return ('Odd','Even')[even_or_odd]
    else:
        return ('Even','Odd')[even_or_odd]

def Week_Number(date):
    '''
    Функция возвращает номер недели, к которой относится date
    \ndate должна быть типа QCalendarWidget
    '''
    return (datetime.date( QDate.year(date), QDate.month(date),QDate.day(date)).isocalendar()[1])


class CalendarWindow(QCalendarWidget):
    date_selected = Signal(str, str, str)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Календарь. Для создания заметок нажмите на соответствующую дату")
        self.setGeometry(640, 480, 480, 480)
        self.setStyleSheet(" background-color: #474b4f")

        self.activated.connect(self.Selected_data)

        #self.setStyleSheet("QLineEdit { background-color: yellow }")
    def Selected_data(self, date):
        '''
        Функция возвращает кортеж из 3 значений:
        дата, день недели, четность недели (числитель или знаменатель)
        '''
        days_of_week = {1: 'Monday',
                        2: 'Tuesday',
                        3: 'Wednesday',
                        4: 'Thursday',
                        5: 'Friday',
                        6: 'Saturday',
                        7: 'Sunday'}
        self.hide()

        self.date_selected.emit(f'{QDate.day(date)}.{QDate.month(date)}.{QDate.year(date)}',
                                days_of_week[QDate.dayOfWeek(date)], Is_Week_Even_Or_Odd(date))

    def keyPressEvent(self, e):
        # when escape key is pressed

        if e.key() == Qt.Key_Escape:
            # show the present date
            #self.showToday()
            print("Нажат esc")


    def paintCell(self, painter, rect, date):
        QtWidgets.QCalendarWidget.paintCell(self, painter, rect, date)
        if date == date.currentDate():
            painter.setBrush(QtGui.QColor(0, 50, 2000, 50))
            painter.setPen(QtGui.QColor(0, 0, 0, 0))
            painter.drawRect(rect)

if __name__ == "__main__":

    calendar = QApplication(sys.argv)
    main_window = CalendarWindow()
    main_window.show()
    sys.exit(calendar.exec())
