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

def Selected_data(date):
    '''
    Функция возвращает кортеж из 2 значений:
    дата и ее четность (числитель или знаменатель)
    '''
    print(QDate.currentDate(),Is_Week_Even_Or_Odd(date))


class CalendarWindow(QCalendarWidget):


    def __init__(self):
        super().__init__()

        self.setWindowTitle("Календарь. Для создания заметок нажмите на соответствующую дату")
        self.setGeometry(640, 480, 480, 480)

        self.activated.connect(Selected_data)







    def keyPressEvent(self, e):
        # when escape key is pressed

        if e.key() == Qt.Key_Escape:
            # show the present date
            #self.showToday()
            print("Нажат esc")





if __name__ == "__main__":

    calendar = QApplication(sys.argv)
    main_window = CalendarWindow()
    main_window.show()
    sys.exit(calendar.exec())
