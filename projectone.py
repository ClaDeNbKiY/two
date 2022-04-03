from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
import json

app = QApplication([])

#Параметры окна приложения

notes_win = QWidget()
notes_win.setWindowTitle('Умная шняга,а ты тупой)))))')
notes_win.resize(900,600)

#виджеты окна приложения
list_notes = QListWidget()
list_notes_label = QLabel('Список твоих бесполезных заметок')

button_note_create = QPushButton("Создам тебе заметку")
button_note_del = QPushButton("Удалю твою заметку")
button_note_save = QPushButton("Сохраню твою заметку")

#Тэги
field_tag = QLineEdit("")
field_tag.setPlaceholderText("Введите тег..")
field_text = QTextEdit()
button_tag_add = QPushButton("Добавить к заметке")
button_tag_del = QPushButton("Открепить от заметки")
button_tag_search = QPushButton("Искать заметки по тегу")
list_tags = QListWidget()
list_tags_label = QLabel("Список тегов")

#Расположение лайотов
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1)
layout_notes.addLayout(col_2)
notes_win.setLayout(layout_notes)
#функционал приложения
def add_note():
    note_name, ok = QInputDialog.getText(notes_win,"Добавить заметку","название заметки:")
    if ok and note_name != "":
        notes[note_name] = {"текст" : "", "теги" : []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]["теги"])
        print(notes)
def show_note():
    key = list_notes.selectedItems ()[0].text()
    print(key)
    field_text.setText(notes[key]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[key]["теги"])

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["текст"] = field_text.toPlainText()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Заметка для сохранениря не выбрана")

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Идиот выберт что мне надо удалить!")
 #Теги
def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
        with open("notes_data.json", "w")as file:
            json.dump(notes, file, sort_keys=True, ensure_askii=False)
        print(notes)
    else:
        print("Ты не выбрал заметку для добавления тега!")
#обработка событий
button_note_create.clicked.connect(add_note)
button_note_save.clicked.connect(save_note)
button_note_del.clicked.connect(del_note)
#запуск приложения
list_notes.itemClicked.connect(show_note)
notes_win.show()

with open("notes_data.json","r") as file:
    notes = json.load(file)
list_notes.addItems(notes)
app.exec_()
