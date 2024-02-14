import csv
import easygui
from datetime import datetime

def save_notes(notes):
    with open('notes.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['ID', 'Title', 'Body', 'Date/Time'])

        for note in notes:
            writer.writerow([note['id'], note['title'], note['body'], note['date_time']])
    easygui.msgbox('Заметки успешно сохранены', title='Успех')
    
def read_notes():
    notes = []
    try:
        with open('notes.csv', 'r') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)
            for row in reader:
                note = {'id': row[0], 'title': row[1], 'body': row[2], 'date_time': row[3]}
                notes.append(note)
    except FileNotFoundError:
        pass
    return notes

def show_notes(notes):
    if (len(notes) != 0):
        for note in notes:
            print(f"ID: {note['id']} - {note['title']} ({note['date_time']})")
            print(note['body'])
            print()
    else:
        print('Спиоск заметок пуст')
              
def add_note():
    title = easygui.enterbox('Введите имя заметки:', title='Добавление заметки')
    body = easygui.enterbox('Введите текст заметки:', title='Добавление заметки')
    date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {'id': str(len(notes) + 1), 'title': title, 'body': body, 'date_time': date_time}

def edit_note(note):
    title = easygui.enterbox('Новое имя заметки:', title='Редактирование заметки', default=note['title'])
    body = easygui.enterbox('Новая заметка:', title='Редактирование заметки', default=note['body'])
    note['title'] = title
    note['body'] = body
    note['date_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return note

def delete_note():
    id = easygui.enterbox('Введите номер заметки (ID):', title='Удаление заметки')
    for note in notes:
        if note['id'] == id:
            notes.remove(note)
            easygui.msgbox(f'Заметка с номером {id} удалена', title='Успех')
            return
    easygui.msgbox('Заметка не найдена', title='Ошибка')

notes = read_notes()

while True:
    userChoice = easygui.buttonbox('Выберите действие:', choices=['Добавить заметку', 
                                                              'Редактировать заметку', 
                                                              'Сохранить заметки', 
                                                              'Показать все заметки', 
                                                              'Удалить заметку',
                                                              'Выход'], title='Заметочник')

    if userChoice == 'Добавить заметку':
        note = add_note()
        notes.append(note)
    elif userChoice == 'Редактировать заметку':
        id = easygui.enterbox('Введите номер заметки (ID):', title='Редактирование заметки')
        for note in notes:
            if note['id'] == id:
                edited_note = edit_note(note)
                notes.remove(note)
                notes.append(edited_note)
                break
        else:
            easygui.msgbox('Заметка не найдена', title='Ошибка')
    elif userChoice == 'Удалить заметку':
        delete_note()
    elif userChoice == 'Сохранить заметки':
        save_notes(notes)
    elif userChoice == 'Показать все заметки':
        show_notes(notes)
    else:
        break