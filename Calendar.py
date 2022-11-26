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
    print( ("Even", "Odd")[Week_Number(date) % 2])

def Week_Number(date):
    '''
    Функция выдает номер недели, к которой относится date
    \ndate должна быть типа QCalendarWidget
    '''


    return (datetime.date( QDate.year(date), QDate.month(date),QDate.day(date)).isocalendar()[1])



class CalendarWindow(QCalendarWidget):


    def __init__(self):
        super().__init__()

        self.setWindowTitle("Календарь. Для создания заметок нажмите на соответствующую дату")
        self.setGeometry(640, 480, 480, 480)

        self.activated.connect(Is_Week_Even_Or_Odd)







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
