from PySide6.QtWidgets import QWidget, QTextEdit, QLabel, QVBoxLayout, QHBoxLayout


DARK_GREEN = '#61892F'
LIGHT_GREEN = '#86C232'
BLACK = '#222629'
DARK_GREY = '#474B4F'
LIGHT_GREY = '#6B6E70'


class Lesson(QWidget):
    def __init__(self, index, name, time, notes):
        super().__init__()
        self.index = index
        self.notes = notes

        # Добавление надписи с названием предмета
        self.time = QLabel(time)
        self.time.setWordWrap(True)
        self.time_layout = QHBoxLayout()
        self.time_layout.addWidget(self.time)
        self.time_layout.addStretch(0)

        # Добавление надписи с временем занятия
        self.v_layout = QVBoxLayout()
        self.name = QLabel(name)
        self.name.setWordWrap(True)
        self.v_layout.addWidget(self.name)
        self.v_layout.addLayout(self.time_layout)
        self.v_layout.addStretch(0)

        # Добавление Поля под заметки
        self.text = QTextEdit(notes.get(index, ''))
        self.text.textChanged.connect(self.Changed)
        self.h_layout = QHBoxLayout(self)
        self.h_layout.addLayout(self.v_layout, 1)
        self.h_layout.addWidget(self.text, 3)

    def Changed(self):
        self.notes[self.index] = self.text.toPlainText()


class Manager(QWidget):
    def __init__(self):
        super().__init__()

        self.lessons = QVBoxLayout(self)

        style = f'''
                background-color: {DARK_GREY}; 
                color: white;
                padding: 6px;
                border-radius: 10px;
            '''
        self.setStyleSheet(
            f'''Manager {{
                padding: 0px;
            }}
            QLabel {{{style}}}
            QTextEdit {{{style}}}''')

    def chageRecords(self, schedule, notes):
        """Обновляет рассписание и заметки"""
        # Удаление старых записей
        for i in range(self.lessons.count() - 1, -1, -1):
            self.lessons.itemAt(i).widget().deleteLater()

        # Добавление новый записей
        for rec in schedule:
            self.lessons.addWidget(Lesson(str(rec['index']), rec['name'], rec['time'], notes))