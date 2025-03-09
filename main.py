#Імпортування бібліотек
from PyQt6.QtWidgets import *
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
save_note_btn = QPushButton('Зберегти замітку')
create_note = QPushButton('Створити замітку')
delete_note_btn = QPushButton('Видалити замітку')
search_tag = QPushButton('Шукати замітки по тегу')
add_tag_btn = QPushButton('Додати до замітки')
delete_tag = QPushButton('Відкріпити від замітки')
search_tag_area = QLineEdit('Введіть тег...')
#Підтягування всіх заміток та тегів
notes_list.addItems(notes)
#Додавання всіх віджетів на лінії
v1.addWidget(notes_list_lbl)
v1.addWidget(notes_list)
v1.addLayout(h1)
h1.addWidget(create_note)
h1.addWidget(delete_note_btn)
v1.addWidget(save_note_btn)
v1.addWidget(tags_list_lbl)
v1.addWidget(tags_list)
v1.addWidget(search_tag_area)
v1.addLayout(h2)
h2.addWidget(add_tag_btn)
h2.addWidget(delete_tag)
v1.addWidget(search_tag)

#Створення функцій
def show_note():
    key = notes_list.currentItem().text()
    text_status = len(text_area.toPlainText())
    if text_status >= 1:
        text_area.setText(notes[key]["текст"])
        tags_list.clear()
        tags_list.addItems(notes[key]["теги"])
    else:
        notes[key]["текст"] = "Немає тексту"
        text_area.setText(notes[key]["текст"])
        tags_list.clear()
        tags_list.addItems(notes[key]["теги"])
def add_note():
    note_name, ok = QInputDialog.getText(window, "Нова нотатка", "Введіть назву нотатки")
    if ok == True:
        notes[note_name] = {
            "текст": "",
            "теги": [

            ]
        }
        notes_list.clear()
        notes_list.addItems(notes)
        write_in_file(notes)
def save_note():
    notes[notes_list.currentItem().text()]["текст"] = text_area.toPlainText()
    write_in_file(notes)

def delete_note():
    key = notes_list.currentItem().text()
    notes.pop(key)
    notes_list.clear()
    notes_list.addItems(notes)
    write_in_file(notes)
def add_tag():
    tag_name, ok = QInputDialog.getText(window, "Новий тег", "Введіть назву тегу")
    if ok == True:
        notes[notes_list.currentItem().text()]["теги"].append(tag_name)
        notes_list.clear()
        notes_list.addItems(notes)
        tags_list.clear()
        tags_list.addItems(notes[notes_list.currentItem().text()]["теги"])
        write_in_file(notes)
#Прив'язка функцій до кнопок
notes_list.itemClicked.connect(show_note)
save_note_btn.clicked.connect(save_note)
create_note.clicked.connect(add_note)
delete_note_btn.clicked.connect(delete_note)
add_tag_btn.clicked.connect(add_tag)

#Додавання основи на головну лінію
mainline.addWidget(text_area)

#Додавання ліній на головну лінію та запуск вікна з програмою
mainline.addLayout(v1)
window.setLayout(mainline)
window.show()
app.exec()