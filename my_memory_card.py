#создай приложение для запоминания информации




from  PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication ,QWidget , QPushButton , QLabel , QVBoxLayout , QGroupBox ,QMessageBox ,QHBoxLayout, QRadioButton, QButtonGroup
from random import randint, shuffle


def sohw_result():
    RadioGroupBox.hide()#временное скрытие окна
    AnsGroupBox.show()
    button.setText('Следующий вопрос')





class Question():
    def __init__(self, question, right_answer , wrong1 , wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3





def sohw_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup = QButtonGroup() 
    RadioGroup.addButton(rbtn_1)
    RadioGroup.addButton(rbtn_2)
    RadioGroup.addButton(rbtn_3)
    RadioGroup.addButton(rbtn_4)
    RadioGroup.setExclusive(False)#снять ограничения на колличество ответов
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def test():
    if 'Ответить' == button.text():
        sohw_result()
    else:
        sohw_question()


def show_correct(res):
    result.setText(res)
    sohw_result()
























app = QApplication([])
main_win = QWidget() 
main_win.resize(600 , 400) # размер окна
main_win.setWindowTitle('Memory Card') #имя окна

button = QPushButton('Ответить') # кнопка

text = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox('Варианты ответов') # надпись
rbtn_1 = QRadioButton('Энцы')#варианты ответов:
rbtn_2 = QRadioButton('Манты')
rbtn_3 = QRadioButton('Чеченцы')
rbtn_4 = QRadioButton('Египтяне')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 =QVBoxLayout()



layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)



 
AnsGroupBox = QGroupBox('результат теста')
result = QLabel('Правильно\неправильно')
itog = QLabel('верный ответ')


layout_res = QVBoxLayout()
layout_res.addWidget(result)
layout_res.addWidget( itog, alignment=(Qt.AlignCenter | Qt.AlignVCenter))
AnsGroupBox.setLayout(layout_res)








answer = [rbtn_1 , rbtn_2 , rbtn_3 , rbtn_4]#список ответов
def ask(q:Question):#вопрос , ответ , неверные ответы(3)
    shuffle(answer)#перемешать варианты ответов
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    text.setText(q.question)
    itog.setText(q.right_answer) # итог с правильным ответом  
    sohw_question()# позвать функцию схов квешон

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно')
        main_win.score +=1
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверное!')



main_win.cur_question = -1#циферка вопроса
def next_question():
    main_win.cur_question += 1#переход к слудющему вопросу
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0#обнулили спсок
    q = question_list[main_win.cur_question]
    ask(q)
    main_win.total+= 1

def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()






line1 = QHBoxLayout()
line1.addWidget(text , alignment=(Qt.AlignCenter | Qt.AlignVCenter))
line2 = QHBoxLayout()
line2.addWidget(RadioGroupBox)
line2.addWidget(AnsGroupBox)
line3 = QHBoxLayout()
line3.addWidget(button, alignment=(Qt.AlignCenter | Qt.AlignVCenter))


glav = QVBoxLayout()
glav.addLayout(line1)
glav.addLayout(line2)
glav.addLayout(line3)

main_win.setLayout(glav)
AnsGroupBox.hide()
button.clicked.connect(click_ok)


# layout = QVBoxLayout() # хранение эдлементов
# line.addWidget(text , alignment = Qt.AlignCenter) # добавление  виджета
# line.addWidget(winner , alignment = Qt.AlignCenter)
# line.addWidget(button , alignment = Qt.AlignCenter)

# main_win.setLayout(layout) # добовление элементов в окно 

# button.clicked.connect(sohw_winner)
question_list = []
q = Question('Какой национальности не существует?', 'Манты','Энцы','Чеченцы','Египтяне' )
question_list.append(q)
q1 = Question('Кто проживает на дне океана?','губка боб', 'бананы','бобры','белки')
question_list.append(q1)
q2 = Question('Какой мой любимый цвет?', 'чёрный', 'белый','синий','жёлтый')
question_list.append(q2)
q3 = Question('Когда началась 1 мировая война?' ,'1914' , '1939' , '1918', '1940')
question_list.append(q3)
q4 = Question('Сколько секунд в сутка?', '86400' , '36200', '24000', '12000')
question_list.append(q4)
q5 = Question('сколько видов птиц в мире?', '9700', '3600', ' 2400', '1200')
question_list.append(q5)
q6 = Question('Когда вымерли динозавры?', '65 миллионов лет назад', '55 миллионов лет назад','25 миллионов лет назад','42 миллиона лет назад')
question_list.append(q6)
q7 = Question('Когда появился ютуб?', '2004 год', '2005 год','2007 год','2009 год')
question_list.append(q7)
q8 = Question('Когда появился майнкрафт?', '2009 год','2006 год','2002 год','2001 год',)
question_list.append(q8)
q9 = Question('Когда отменили крепостоное право?', '1861', '1851','1824','1831')
question_list.append(q9)
q10 = Question('Какой дом самй лучший ','банановый','ананасовый','ореховый','чёрный')
question_list.append(q10)















next_question()









main_win.show() 
app.exec_() 