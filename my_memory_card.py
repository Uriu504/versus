from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QRadioButton,  QGroupBox, QButtonGroup

questions = [
                {'question':'Какой национальности не существует?', 
                'answer1':'Смурфы',
                'answer2':'Эннцы',
                'answer3':'Чулымцы',
                'answer4':'Алеуты',
                },
]

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.setFixedSize(250, 200)
Btn_ok = QPushButton('Ответить:')
question = QLabel('?')
group_answers = QGroupBox('Ответить')

class Question():
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

ans_1 = QRadioButton('')
ans_2 = QRadioButton('')
ans_3 = QRadioButton('')
ans_4 = QRadioButton('')

ans_layout1 = QVBoxLayout()
ans_layout1.setSpacing(20)
ans_layout1.addWidget(ans_1, alignment=Qt.AlignCenter)
ans_layout1.addWidget(ans_2, alignment=Qt.AlignCenter)

ans_layout2 = QVBoxLayout()
ans_layout2.setSpacing(20)
ans_layout2.addWidget(ans_3, alignment=Qt.AlignCenter)
ans_layout2.addWidget(ans_4, alignment=Qt.AlignCenter)
ans_layout = QHBoxLayout()
ans_layout.addLayout(ans_layout1)
ans_layout.addLayout(ans_layout2)
group_answers.setLayout(ans_layout)

def show_result():
    if Btn_ok.text() == 'Ответить':
        for ans in (ans_1, ans_2, ans_3, ans_4):
            if ans.isChecked():
                Btn_ok.setText('Следующий вопрос')
                group_answers.show()
                group_answers.hide()
