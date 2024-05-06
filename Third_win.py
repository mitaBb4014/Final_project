from project import *
from Fourth_win import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QApplication, QHBoxLayout

class Third_window(QWidget):
    def __init__(self):

        #Выполнение всех ниже прописанных методов(кроме super.__init__(он экспортирует методы из QWidgets) и метода show)
        super().__init__()
        self.set_appear(name_pril, wight, height, x, y)
        self.initUI()
        self.connects()
        self.show()

    #Стандартный метод и настройки окна
    def set_appear(self, name_pril, widht, height, x, y):
        self.setWindowTitle(name_pril)
        self.resize(widht,height)
        self.move(x,y)

    #Метод реагирования на кнопку
    def connects(self):
        self.button_yes.clicked.connect(self.next_click)

    #Метод перехода на другой экран
    def next_click(self):
        self.hide()
        self.tw = Fourth_window(why)

    #Содержание третьего окна
    def initUI(self):
        self.vopros = QLabel('Вы готовы начать?')
        self.button_yes = QPushButton('Да')
        self.button_no = QPushButton('Нет')

        self.Hline = QHBoxLayout()
        self.Hline.addWidget(self.button_yes, alignment = Qt.AlignCenter)
        self.Hline.addWidget(self.button_no, alignment = Qt.AlignCenter)

        self.Vline = QVBoxLayout()
        self.Vline.addWidget(self.vopros, alignment = Qt.AlignCenter)
        self.Vline.addLayout(self.Hline)

        self.setLayout(self.Vline)
        
