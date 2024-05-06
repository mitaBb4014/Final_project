from project import *
from final_win import *
from random import randint 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QApplication, QHBoxLayout

class Fourth_window(QWidget):

    #Выполнение всех ниже прописанных методов(кроме super.__init__(он экспортирует методы из QWidgets) и метода show)
    def __init__(self,why):
        self.why = why
        self.pers = pers
        super().__init__()
        self.set_appear(name_pril, wight, height, x, y)
        self.initUI(why)
        self.connects()
        self.show()
        

    #Стандартный метод и настройки окна
    def set_appear(self, name_pril, widht, height, x, y):
        self.setWindowTitle(name_pril)
        self.resize(widht,height)
        self.move(x,y)

    #Условие при нажатии на кнопку "Да"
    def condition_yes(self):

        #Переход с первого на второй вопрос
        if self.why == slovar_1['v_1']:
            
            self.rand = randint(1,2)

            if self.rand == 1:
                self.why = slovar_2['v_2']
            else:
                self.why = slovar_2['v_2_1']
        
        elif self.why == slovar_1['v_1_2']:
            self.why = slovar_2['v_2_2']

    #Переход со второго на третий вопрос
        elif self.why == slovar_2['v_2_2']:
            #Положительный не из Конохи
            self.why = slovar_3['v_3']

        elif self.why == slovar_2['v_2']:
            #Герой Конохи
            self.why = slovar_3['v_31']

        elif self.why == slovar_2['v_2_1']:
            #Дефолт Конохи
            self.why = slovar_3['v_32']

        #Талантливый, положительный не из конохи
        elif self.why == slovar_3['v_3']:
            self.why = slovar_4['v_4_31']

        elif self.why == slovar_3['v_31']:
            self.why = slovar_4['v_4']

        elif self.why == slovar_3['v_32']:
            self.why = slovar_4['v_41']

        elif self.why == slovar_3['v_33']:
            self.why = slovar_4['v_42']

        elif self.why == slovar_3['v_34']:
            self.why = slovar_4['v_43']

        elif self.why == slovar_3['v_3_1']:
            self.why = slovar_4['v_4_5']

    #Переход с четвёртого вопроса на пятый
        #Либо Гаара либо Темари
        elif self.why == slovar_4['v_4_31']:
            self.why = slovar_5['v_5_9']

        #Либо Сай либо Ямато
        elif self.why == slovar_4['v_4']:
            self.why = slovar_5['v_5_1'] 
            
        #Либо Фуу либо Торуне
        elif self.why == slovar_4['v_41']:
            self.why = slovar_5['v_5_6']

        #Либо Фуу либо Торуне
        elif self.why == slovar_4['v_42']:
            self.why = slovar_5['v_5_6'] 

        elif self.why == slovar_4['v_4_1']:
            self.why = slovar_5['v_5_7']

        elif self.why == slovar_4['v_4_22']:
            self.why = slovar_5['v_5_2']

        elif self.why == slovar_4['v_4_3']:
            self.why = slovar_5['v_5_17']

        elif self.why == slovar_4['v_4_5']:
            self.why = slovar_5['v_5_21']

        elif self.why == slovar_4['v_4_4']:
            self.why = slovar_5['v_5_13']

    #Переход на персонажа

        elif self.why == slovar_5['v_5_13']:
            self.hide()
            self.tw = final_window('Эй')

        elif self.why == slovar_5['v_5_21']:
            self.hide()
            self.tw = final_window('Хидан')

        elif self.why == slovar_5['v_5_17']:
            self.hide()
            self.tw = final_window('Суйгецу')

        elif self.why == slovar_5['v_5_9']:
            self.hide()
            self.tw = final_window('Гаара')

        elif self.why == slovar_5['v_5_2']:
            self.hide()
            self.tw = final_window('Наруто')

        elif self.why == slovar_5['v_5_3']:
            self.hide()
            self.tw = final_window('Майто Гай')

        elif self.why == slovar_5['v_5_1']:
            self.hide()
            self.tw = final_window('Ямато')

        elif self.why == slovar_5['v_5_4']:
            self.hide()
            self.tw = final_window('Какаши')

        elif self.why == slovar_5['v_5_6']:
            self.hide()
            self.tw = final_window('Торуне')

        elif self.why == slovar_5['v_5_7']:
            self.hide()
            self.tw = final_window('Мадара')

        elif self.why == slovar_5['v_5_8']:
            self.hide()
            self.tw = final_window('Шикамару')

        elif self.why == slovar_5['v_5']:
            self.hide()
            self.tw = final_window('Итачи') 

        elif self.why == slovar_5['v_5_11']:
            self.hide()
            self.tw = final_window('Нагато')

        elif self.why == slovar_5['v_5_19']:
            self.hide()
            self.tw = final_window('Райга')

        elif self.why == slovar_5['v_5_23']:
            self.hide()
            self.tw = final_window('Пейн')

        elif self.why == slovar_5['v_5_15']:
            self.hide()
            self.tw = final_window('Кабуто')

        self.vopros.setText(self.why)

    #Условие при нажитии на кнопку "Нет"
    def condition_no(self):

        #Переход с первого на второй вопрос
        if self.why == slovar_1['v_1']:
            self.why = slovar_2['v_2_2']
        
        elif self.why == slovar_1['v_1_2']:
            
            self.rand = randint(1,2)

            if self.rand == 1:
                self.why = slovar_2['v_2']
            else:
                self.why = slovar_2['v_2_1']

    #Переход со второго на третий вопрос
        #Отрицательный не из Конохи
        elif self.why == slovar_2['v_2_2']:
            self.why = slovar_3['v_3_1']

        #Дефолт Конохи
        elif self.why == slovar_2['v_2']:
            self.why = slovar_3['v_33']
        
        #Герой Конохи
        elif self.why == slovar_2['v_2_1']:
            self.why = slovar_3['v_34']

    #Переход с третьего на четвёртый вопрос
        #Плохой из 7 мечников 
        elif self.why == slovar_3['v_3_1']:
            self.why = slovar_4['v_4_3']

        #Просто силач Конохи
        elif self.why == slovar_3['v_33']:
            self.rand = randint(1,2)
            if self.rand == 1:
                self.why = slovar_4['v_4_1']
            else:
                self.why = slovar_4['v_4_2']

        #Герой и просто силач Конохи
        elif self.why == slovar_3['v_34']:
            self.why = slovar_4['v_4_21']

        #Силач, положительный не из конохи
        elif self.why == slovar_3['v_3']:
            self.why = slovar_4['v_4_4']

        #Не талантливый Герой Конохи
        elif self.why == slovar_3['v_31']:
            self.why = slovar_4['v_4_22']


    #Переход с четвёртого вопроса на пятый

        elif self.why == slovar_4['v_4_22']:
            self.why = slovar_5['v_5_3']

        elif self.why == slovar_4['v_4']:
            self.why = slovar_5['v_5']

        elif self.why == slovar_4['v_43']:
            self.why = slovar_5['v_5']

        elif self.why == slovar_4['v_4_3']:
            self.why = slovar_5['v_5_19']

        elif self.why == slovar_4['v_4_1']:
            self.why = slovar_5['v_5_8']

        elif self.why == slovar_4['v_42']:
            self.why = slovar_5['v_5_4']

        elif self.why == slovar_4['v_41']:
            self.why = slovar_5['v_5_4']

        elif self.why == slovar_4['v_4_31']:
            self.why = slovar_5['v_5_11']

        elif self.why == slovar_4['v_4_5']:
            self.why = slovar_5['v_5_23']

        elif self.why == slovar_4['v_4_4']:
            self.why = slovar_5['v_5_15']

    #Переход с пятого вопроса на персонажа

        elif self.why == slovar_5['v_5_15']:
            self.hide()
            self.tw = final_window('Джуго')

        elif self.why == slovar_5['v_5_23']:
            self.hide()
            self.tw = final_window('Сасори')

        elif self.why == slovar_5['v_5_19']:
            self.hide()
            self.tw = final_window('Забузу')

        elif self.why == slovar_5['v_5_21']:
            self.hide()
            self.tw = final_window('Какузу')

        elif self.why == slovar_5['v_5_11']:
            self.hide()
            self.tw = final_window('Конан')

        elif self.why == slovar_5['v_5_9']:
            self.hide()
            self.tw = final_window('Темари')

        elif self.why == slovar_5['v_5_2']:
            self.hide()
            self.tw = final_window('Саске')

        elif self.why == slovar_5['v_5_3']:
            self.hide()
            self.tw = final_window('Майто Дай')

        elif self.why == slovar_5['v_5_1']:
            self.hide()
            self.tw = final_window('Сай')

        elif self.why == slovar_5['v_5_4']:
            self.hide()
            self.tw = final_window('Конохомару')

        elif self.why == slovar_5['v_5_6']:
            self.hide()
            self.tw = final_window('Фуу')

        elif self.why == slovar_5['v_5_7']:
            self.hide()
            self.tw = final_window('Изуна')

        elif self.why == slovar_5['v_5_8']:
            self.hide()
            self.tw = final_window('Сакура')

        elif self.why == slovar_5['v_5']:
            self.hide()
            self.tw = final_window('Шисуи')

        elif self.why == slovar_5['v_5_17']:
            self.hide()
            self.tw = final_window('Шизума')

        elif self.why == slovar_5['v_5_13']:
            self.hide()
            self.tw = final_window('Ооноке')

        self.vopros.setText(self.why)  

    #Содержание четвёртого окна
    def initUI(self,why):
        self.vopros = QLabel(self.why)
        self.button__yes = QPushButton('Да')
        self.button__no = QPushButton('Нет')

        self.Hline = QHBoxLayout()
        self.Hline.addWidget(self.button__yes, alignment = Qt.AlignCenter)
        self.Hline.addWidget(self.button__no, alignment = Qt.AlignCenter)

        self.Vline = QVBoxLayout()
        self.Vline.addWidget(self.vopros, alignment = Qt.AlignCenter)
        self.Vline.addLayout(self.Hline)

        self.setLayout(self.Vline)

    #Метод реагирования на кнопки
    def connects(self):
        self.button__yes.clicked.connect(self.condition_yes)
        self.button__no.clicked.connect(self.condition_no)
    
        