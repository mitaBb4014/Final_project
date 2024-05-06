#Импортирование нужных библиотек (project - файл с переменными),(second_win - отвечает за второе окно) и (остальное отвечает за использование PyQt5 в проекте)
from project import *
from second_win import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QApplication

class Akinator_Naruto(QWidget):
    #Выполнение всех ниже прописанных методов(кроме super.__init__(он экспортирует методы из QWidgets) и метода show)
    def __init__(self):
        super().__init__()
        self.set_appear(name_pril, wight, height, x, y)
        self.initUI(introduction)
        self.connects()
        self.show()

    #Стандартный метод и настройки окна
    def set_appear(self, name_pril, wight, height, x, y):
        self.setWindowTitle(name_pril)
        self.resize(wight,height)
        self.move(x,y)

    #Содержание первого окна
    def initUI(self, introduction):
        self.greetings = QLabel(introduction)
        self.button_start = QPushButton('Начать')
        
        self.V_Line = QVBoxLayout()

        self.V_Line.addWidget(self.greetings, alignment = Qt.AlignCenter)
        self.V_Line.addWidget(self.button_start, alignment = Qt.AlignCenter)

        self.setLayout(self.V_Line)

    #Метод реагирования на кнопку
    def connects(self):
        self.button_start.clicked.connect(self.next_click)

    #Метод перехода на другой экран
    def next_click(self):
        self.hide()
        self.tw = Second_window()

#Создание приложения и экземпляра класса , а также удержание их в открытом состоянии
Main = QApplication([])
Main_go = Akinator_Naruto()

Main.exec_()