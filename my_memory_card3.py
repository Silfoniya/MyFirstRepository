from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel,
QMessageBox, QRadioButton, QGroupBox, QButtonGroup)
import random

#класс Question
class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

#создание виджетного окна
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory card')
main_win.setFixedWidth(250)
main_win.setFixedHeight(150)

main_win.setStyleSheet("""
        QGroupBox { background-color: rgb(128, 128, 128);
        } """)

questions = list()
questions.append(Question('Государственный язык Бразилии', 'Португальский', 'Испанский', 'Итальянский', 'Бразильский'))
questions.append(Question('Год основания Древней Руси', '882', '862', '982', '1000'))
questions.append(Question('Государственный язык Италии', 'Итальянский', 'Португальский', 'Испанский', 'Бразильский'))
global cur_q
cur_q = randint(0, len(questions)-1)

question = QLabel()
answer = QLabel()



#ntn = ['Португальский', 'Испанский', 'Итальянский', 'Бразильский']
btn_answers = []

button_group = QGroupBox('Варианты ответов')
answer_group = QGroupBox('Правильно!')
button_next = QPushButton('Ответить')

answer_group.hide()

#for i in range(4):
q = questions[cur_q]
question.setText(q.question)
btn = QRadioButton(str(q.right_answer))
btn_answers.append(btn)
btn.clicked.connect(lambda ch, btn=btn: show_win(btn))
btn = QRadioButton(str(q.wrong1))
btn_answers.append(btn)
btn.clicked.connect(lambda ch, btn=btn: show_win(btn))
btn = QRadioButton(str(q.wrong2))
btn_answers.append(btn)
btn.clicked.connect(lambda ch, btn=btn: show_win(btn))
btn = QRadioButton(str(q.wrong3))
btn_answers.append(btn)
btn.clicked.connect(lambda ch, btn=btn: show_win(btn))

def show_result():
    if button_next.text() == 'Ответить':
        button_group.hide()
        answer_group.show()
        button_next.setText('Следующий вопрос')
    else:
        button_group.show()
        answer_group.hide()
        button_next.setText('Ответить')
        cur = random.randint(0, len(questions) - 1)
        global cur_q
        cur_q = cur
        next_question(cur)

button_next.clicked.connect(show_result)

#обработка нажатий на переключатели
def show_win(button: QRadioButton):
    global cur_q
    q = questions[cur_q]
    if button.text() == q.right_answer:
        answer_group.setTitle('Правильно')
    else:
        answer_group.setTitle('Неправильно')
    #button_group.hide()
    #answer_group.show()
    button.setAutoExclusive(False)
    button.setChecked(False)
    button.setAutoExclusive(True)
    show_result()

def show_question():
    #label.setText(text_steps[0])
    #btn_next.setText(btn_next[0])

    widget.btns.hide()
    widget.answer.hide()
    next_question()

def show_answer():
    widget.answer.show()

def start_test():
    if button_next() == 'Ответить':
        return show_result()
    elif button_next() == 'Следующий вопрос':
        return show_question()


def check_answer():
    if button_next() == answers[0]:
        return show_correct()
    else:
        return show_correct()


def next_question(cur):
    #cur_question = -1
    ask(questions[cur])

def ask(q: Question):
    shuffle(answers)
    question.setText(q.question)
    btn_answers[0].setText(q.right_answer)
    btn_answers[2].setText(q.wrong2)
    btn_answers[1].setText(q.wrong1)
    btn_answers[3].setText(q.wrong3)
    Ib_Question.setText(q.question)
    Ib_Correct.setText(q.right_answer)
    show_question()


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')



#отображение окна приложения
layout_main = QVBoxLayout()
horizontal1 = QHBoxLayout()
horizontal1.addWidget(question)

horizontal2 = QHBoxLayout()
horizontal2.addWidget(button_group)
horizontal2.addWidget(answer_group)

vbox = QVBoxLayout()
hor1 = QHBoxLayout()
hor1.addWidget(btn_answers[0])
hor1.addWidget(btn_answers[1])

hor2 = QHBoxLayout()
hor2.addWidget(btn_answers[2])
hor2.addWidget(btn_answers[3])

vbox.addLayout(hor1)
vbox.addLayout(hor2)
button_group.setLayout(vbox)

hor3 = QHBoxLayout()
hor3.addWidget(answer)
answer_group.setLayout(hor3)

horizontal3 = QHBoxLayout()
horizontal3.addWidget(button_next)

#расположение виджетов по лэйаутам
layout_main.addLayout(horizontal1)
layout_main.addLayout(horizontal2)
layout_main.addLayout(horizontal3)

window.show()

window.score = 0
window.total = 0

next_question()
main_win.setLayout(layout_main)
main_win.show()
app.exec()