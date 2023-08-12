import os
from datetime import datetime


class Notebook:
    def __init__(self, path: str = 'notebook.csv'):
        self.note_book: list[dict[str, str]] = []
        self.path = path

    def open(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            info = file.readlines()
            for note in info:
                note = [i.strip() for i in note.split(';')]
                if len(note) == 3:
                    self.note_book.append({'title': note[0], 'body': note[1], 'timestamp': note[2]})

    def add(self, note: dict[str, str]):
        self.note_book.append(note)
        return note.get('title')

    def save(self):
        info = []
        with open(self.path, 'a', encoding='utf-8') as file:
            for note in self.note_book:
                note = ';'.join([value for value in note.values()])
            info.append(note)
            module_time = ';'.join([str(datetime.fromtimestamp(os.path.getmtime(self.path)))])
            info.append(module_time)
            file.write(';'.join(info))
            file.write('\n')

    def save_when_changed(self, position: int, updated_note: [dict[str, str]]):
        info = []
        with open(self.path, 'w', encoding='utf-8') as file:
            for note in self.note_book:
                note = ';'.join([value for value in note.values()])
                info.append(note)
            info.pop(position - 1)
            module_time = str(datetime.fromtimestamp(os.path.getmtime(self.path)))
            updated_note_to_string = ';'.join(updated_note.values())
            info.insert(position - 1, updated_note_to_string + ';' + module_time)
            file.write('\n'.join(info))

    def save_when_deleted(self):
        info = []
        with open(self.path, 'w', encoding='utf-8') as file:
            for note in self.note_book:
                note = ';'.join([value for value in note.values()])
                info.append(note)
            file.write('\n'.join(info))

    def load(self) -> list[dict[str, str]]:
        return self.note_book

    def find(self, title: str) -> list[dict[str, str]]:
        lost_and_found = []
        for note in self.note_book:
            for value in note.values():
                if title.lower() in value.lower() or title.lower == value.lower:
                    lost_and_found.append(note)
                break

        return lost_and_found

    def del_note(self, index: int):
        return self.note_book.pop(index - 1).get('title')

    def change_note(self, position: int, newest_note: dict) -> str:
        self.note_book.pop(position - 1)
        self.note_book.insert(position - 1, newest_note)
        return newest_note.get('title')
