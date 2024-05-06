from project import*
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget , QVBoxLayout,QPushButton, QLabel, QApplication


#Класс финального окна
class final_window(QWidget):
    def __init__(self,go):
        self.go = go
        super().__init__()
        self.set_appear(name_pril,wight,height,x,y)
        self.initUI()
        self.show()
#Параметры окна
    def set_appear(self,name_pril,wight,height,x,y):
        self.setWindowTitle(name_pril)
        self.resize(wight,height)
        self.move(x,y)
#Параметры интерфейса
    def initUI(self):
        self.gen1 = QLabel('Ваш персонаж это:')
        self.gen = QLabel(self.go)
        
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.gen1, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.gen, alignment = Qt.AlignCenter)

        self.setLayout(self.layout)