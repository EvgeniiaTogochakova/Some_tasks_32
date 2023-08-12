import text


def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def print_message(message: str):
    print('\n' + '_' * len(message))
    print(message)
    print('_' * len(message + '\n'))


def input_note(message: str, cancel: str) -> dict:
    note = {}
    print(message)
    for key, value in text.input_note.items():
        info = ' '.join([i for i in input(value).split()])
        if info:
            note[key] = info
        else:
            print_message(cancel)
    return note


def print_note(nb: list[dict[str, str]], error: str):
    if nb:
        print('\n' + '_' * 115)
        for i, note in enumerate(nb, 1):
            if note.get("timestamp") is None:
                note["timestamp"] = text.you_did_not_save
            print(
                f'{i:>3}. Заголовок: {note.get("title"):<30} Дата последнего изменения: {note.get("timestamp")}')
            print('_' * 115 + '\n')
        dig = input(text.want_to_open_body)
        if dig == '1':
            try:
                id = int(input(text.note_to_read))
                flag = False
                for i, note in enumerate(nb, 1):
                    if id == i:
                        print_message('Печатаю содержимое заметки...')
                        print('\n' + '_' * 150)
                        print(f'{note.get("body"):<150}')
                        print('\n' + '_' * 150)
                        flag = True
                        break
                if not flag:
                    print(text.wrong_id)
            except ValueError:
                print(text.wrong_id_with_string)

    else:
        print_message(error)


def ask_what_title_to_find(question: str) -> str:
    str_input = input(question)
    return str_input


def show_lost_and_found(list_found: list[dict[str, str]]) -> list:
    list_for_user = []
    sublist = ''
    for note in list_found:
        for key, value in note.items():
            sublist += value + "|"
        list_for_user.append(sublist)
        sublist = ''
    return list_for_user


def input_index(message: str, nb: list, error: str) -> int:
    confirmation = input(text.deletion_confirmation)
    if confirmation == 'ДА':
        print_note(nb, error)
        index = input(message)
        if index.isdigit() and 0 < int(index) < len(nb) + 1:
            return int(index)


def input_position(message: str, nb: list, error: str) -> int:
    print_note(nb, error)
    position = input(message)
    if position.isdigit() and 0 < int(position) < len(nb) + 1:
        return int(position)


def input_edited_note(message: str, cancel: str) -> dict:
    newest_note = {}
    print(message)
    for key, value in text.input_edited_note.items():
        info = ' '.join([i for i in input(value).split()])
        if info:
            newest_note[key] = info
        else:
            print_message(cancel)
    return newest_note


def ask_date(question1: str, question2: str, question3: str, error: str, cancel: str) -> str:
    search_str = ''
    year = input(question1)
    if year:
        if year.isdigit() and 1900 < int(year) < 2024:
            search_str += year
            month = input(question2)
            if month:
                if month.isdigit() and 0 < int(month) < 13:
                    if len(month)<2:
                        search_str += f'-0{month}'
                    else:
                        search_str += f'-{month}'
                    day = input(question3)

                    if day:
                        if day.isdigit() and 0 < int(day) < 32:
                            if len(day)<2:
                                search_str += f'-0{day}'
                            else:
                                search_str += f'-{day}'
                            return search_str
                        
                        else:
                            print_message(error)
                    else:
                        print_message(cancel)

                else:
                    print_message(text.input_date_error)

            else:
                print_message(cancel)

        else:
            print_message(text.input_date_error)
    else:
        print_message(cancel)

    
