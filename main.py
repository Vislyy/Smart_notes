#Імпортування бібліотек
from PyQt5.QtWidgets import *
from file_manager import *

#Головний словник для заміток
notes = read_from_file()
#Створення вікна з програмою
write_in_file(notes)
app = QApplication([])
window = QWidget()

#Створення ліній
mainline = QHBoxLayout()
v1 = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()

#Створення всіх віджетів
text_area = QTextEdit()
notes_list = QListWidget()
notes_list_lbl = QLabel("Список заміток")
tags_list = QListWidget()
tags_list_lbl = QLabel("Список тегів")
save_note = QPushButton('Зберегти замітку')
create_note = QPushButton('Створити замітку')
delete_note = QPushButton('Видалити замітку')
search_tag = QPushButton('Шукати замітки по тегу')
add_tag = QPushButton('Додати до замітки')
delete_tag = QPushButton('Відкріпити від замітки')
search_tag_area = QLineEdit('Введіть тег...')
#Підтягування всіх заміток та тегів
notes_list.addItems(notes)
#Додавання всіх віджетів на лінії
v1.addWidget(notes_list_lbl)
v1.addWidget(notes_list)
v1.addLayout(h1)
h1.addWidget(create_note)
h1.addWidget(delete_note)
v1.addWidget(save_note)
v1.addWidget(tags_list_lbl)
v1.addWidget(tags_list)
v1.addWidget(search_tag_area)
v1.addLayout(h2)
h2.addWidget(add_tag)
h2.addWidget(delete_tag)
v1.addWidget(search_tag)

#Створення функцій
def show_note():
    key = notes_list.currentItem().text()
    text_area.setText(notes[key]["текст"])
    tags_list.clear()
    tags_list.addItems(notes[key]["теги"])

def add_note():
    notes_list.addItems("Замітка")
def save_note():
    notes[notes_list.currentItem().text()] = {
        
    }
    write_in_file(notes)

#Прив'язка функцій до кнопок
notes_list.itemClicked.connect(show_note)
save_note.clicked.connect(save_note)

#Додавання основи на головну лінію
mainline.addWidget(text_area)

#Додавання ліній на головну лінію та запуск вікна з програмою
mainline.addLayout(v1)
window.setLayout(mainline)
window.show()
app.exec()