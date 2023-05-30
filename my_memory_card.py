
'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QRadioButton, QMessageBox, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QButtonGroup
from random import shuffle, randint


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
q1 = Question('Государственный язык Бразилии','Португальский','Бразильский','Латинский','Финский')
question_list.append(q1)
q2 = Question('Какого цвета нет на флаге России?', 'Зеленый', 'Красный', 'Синий', 'Белый')
question_list.append(q2)
q3 = Question('Национальная хижина якутов','Ураса','Юрта','Иглу','Хата')
question_list.append(q3)
q4 = Question('Сколько было пилотируемых высадок на Луну?','Шесть','Восемь','Пять','Три')
question_list.append(q4)
q5 = Question('Как долго длилась Столетняя война?','116 лет','100 лет','110 лет','101 год')
question_list.append(q5)
q6 = Question('Что является столицей Австралии?','Канберра','Аделаида','Сидней','Мельбурн')
question_list.append(q6)


app = QApplication([])

window = QWidget()
window.setWindowTitle('Memory Card')


#window.cur_question = -1






def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_quest.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()



def show_result():
    RgB.hide()
    ansgroupbox.show()
    bth_ok.setText('Следующий вопрос')

def show_question():
    RgB.show()
    ansgroupbox.hide()
    bth_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbth_1.setChecked(False)
    rbth_2.setChecked(False)
    rbth_3.setChecked(False)
    rbth_4.setChecked(False)
    RadioGroup.setExclusive(True)





def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window_score += 1
        print('Статистика\n Всего вопросов:',window_total ,'\nПравильных ответов:',window_score)
        print('Рейтинг:',(window_score/window_total * 100),'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг:',(window_score/window_total * 100),'%')


bth_ok = QPushButton('Ответить')
lb_quest = QLabel('Самый сложный вопрос в мире!')

RgB = QGroupBox('Варианты ответов')

rbth_1 = QRadioButton('Вариант 1')
rbth_2 = QRadioButton('Вариант 2')
rbth_3 = QRadioButton('Вариант 3')
rbth_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbth_1)
RadioGroup.addButton(rbth_2)
RadioGroup.addButton(rbth_3)
RadioGroup.addButton(rbth_4)

layout_ans_hor = QHBoxLayout()
layout_ans_var1 = QVBoxLayout()
layout_ans_var2 = QVBoxLayout()
layout_ans_var1.addWidget(rbth_1)
layout_ans_var1.addWidget(rbth_2)
layout_ans_var2.addWidget(rbth_3)
layout_ans_var2.addWidget(rbth_4)

layout_ans_hor.addLayout(layout_ans_var1)
layout_ans_hor.addLayout(layout_ans_var2)

RgB.setLayout(layout_ans_hor)

answers = [rbth_1, rbth_2, rbth_3, rbth_4]

ansgroupbox = QGroupBox('Результат теста')
lb_result = QLabel('прав ты или нет?')
lb_correct = QLabel('ответ будет тут!')

layout_re = QVBoxLayout()
layout_re.addWidget(lb_result, alignment= (Qt.AlignLeft | Qt.AlignTop))

layout_re.addWidget(lb_correct, stretch=1)
ansgroupbox.setLayout(layout_re)

layout_l1 = QHBoxLayout()
layout_l2 = QHBoxLayout()
layout_l3 = QHBoxLayout()

layout_l1.addWidget(lb_quest, alignment= (Qt.AlignHCenter))

layout_l2.addWidget(RgB)
layout_l2.addWidget(ansgroupbox)

ansgroupbox.hide()

layout_l3.addWidget(bth_ok, stretch=8)
layout_l3.addStretch(3)

layout_card = QVBoxLayout()

layout_card.addStretch(1)
layout_card.addLayout(layout_l1)
layout_card.addStretch(1)

layout_card.addLayout(layout_l2, stretch=8)

layout_card.addStretch(1)

layout_card.addLayout(layout_l3)
layout_card.addStretch(1)

window.setLayout(layout_card)

def next_question():
    
    #window.cur_question = window.cur_question + 1

    window_total += 1
    print('Статистика\n Всего вопросов:',window_total ,'\nПравильных ответов:',window_score)  
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)
    

def click_ok():
    if bth_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()



window_score = 0
window_total = 0

bth_ok.clicked.connect(click_ok)
next_question()
window.resize(400, 300)
window.show()
app.exec()
'''

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import randint, shuffle ###


class Question():
    ''' содержит вопрос, правильный ответ и три неправильных'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions_list = [] 
questions_list.append(
        Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(
        Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(
        Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
questions_list.append(
        Question('Сколько было пилотируемых высадок на Луну?','Шесть','Восемь','Пять','Три'))
questions_list.append(
        Question('Как долго длилась Столетняя война?','116 лет','100 лет','110 лет','101 год'))
questions_list.append(
        Question('Что является столицей Австралии?','Канберра','Аделаида','Сидней','Мельбурн'))

app = QApplication([])


btn_OK = QPushButton('Ответить') # кнопка ответа
lb_Question = QLabel('Самый сложный вопрос в мире!') # текст вопроса


RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами


rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')


RadioGroup = QButtonGroup() # это для группировки переключателей, чтобы управлять их поведением
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans_hor = QHBoxLayout()   
layout_ans_ver1 = QVBoxLayout()
layout_ans_ver2 = QVBoxLayout()
layout_ans_ver1.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans_ver1.addWidget(rbtn_2)
layout_ans_ver2.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans_ver2.addWidget(rbtn_4)


layout_ans_hor.addLayout(layout_ans_ver1)
layout_ans_hor.addLayout(layout_ans_ver2)


RadioGroupBox.setLayout(layout_ans_hor)


AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()   


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)


layout_card = QVBoxLayout()

layout_card.addStretch(1)
layout_card.addLayout(layout_line1)
layout_card.addStretch(1)

layout_card.addLayout(layout_line2, stretch=8)

layout_card.addStretch(1)
layout_card.addLayout(layout_line3)
layout_card.addStretch(1)

def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers) # перемешали список из кнопок, теперь на первом месте списка какая-то непредсказуемая кнопка
    answers[0].setText(q.right_answer) # первый элемент списка заполним правильным ответом, остальные - неверными
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # вопрос
    lb_Correct.setText(q.right_answer) # ответ 
    show_question() # показываем панель вопросов 


def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()


def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        # правильный ответ!
        show_correct('Правильно!')
        window.score += 1  ###
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)   ###
        print('Рейтинг: ', (window.score/window.total*100), '%')    ###
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # неправильный ответ!
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')    ###
    


def next_question():  ###
    ''' задает случайный вопрос из списка '''
    window.total += 1   ###
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)   ###
    cur_question = randint(0, len(questions_list) - 1)  # нам не нужно старое значение, 
                                                        # поэтому можно использовать локальную переменную! 
            # случайно взяли вопрос в пределах списка
            # если внести около сотни слов, то редко будет повторяться
    q = questions_list[cur_question] # взяли вопрос
    ask(q) # спросили


def click_OK():
    ''' определяет, надо ли показывать другой вопрос либо проверить ответ на этот '''
    if btn_OK.text() == 'Ответить':
        check_answer() # проверка ответа
    else:
        next_question() # следующий вопрос




window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')


btn_OK.clicked.connect(click_OK) # по нажатии на кнопку выбираем, что конкретно происходит


window.score = 0   ###
window.total = 0   ###
next_question()
window.resize(400, 300)
window.show()
app.exec()