from project import *
from Third_win import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QApplication

class Second_window(QWidget):

    #Выполнение всех ниже прописанных методов(кроме super.__init__(он экспортирует методы из QWidgets) и метода show)
    def __init__(self):
        super().__init__()
        self.set_appear(name_pril, wight, height, x, y)
        self.initUI(rules)
        self.connects()
        self.show()

    #Стандартный метод и настройки окна
    def set_appear(self, name_pril, widht, height, x, y):
        self.setWindowTitle(name_pril)
        self.resize(widht,height)
        self.move(x,y)

    #Содержание второго окна
    def initUI(self, rules):
        self.training = QLabel(rules)
        self.button_next = QPushButton('Далее')

        self.Line = QVBoxLayout()

        self.Line.addWidget(self.training, alignment = Qt.AlignCenter)
        self.Line.addWidget(self.button_next, alignment = Qt.AlignCenter)

        self.setLayout(self.Line)

    #Метод реагирования на кнопку
    def connects(self):
        self.button_next.clicked.connect(self.next_click)

    #Метод перехода на другой экран
    def next_click(self):
        self.hide()
        self.tw = Third_window()
        
        