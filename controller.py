import text
import view
import model


def start():
    my_nb = model.Notebook()
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                try:
                    my_nb.open()
                    view.print_message(text.load_successful)
                except FileNotFoundError:
                    view.print_message(text.if_FileNotFoundError)
            case 2:
                nb = my_nb.load()
                answer_sort = input(text.ask_how_to_sort_or_filter)
                if answer_sort == "AS":
                    notes_list_1 = sorted(nb, key=lambda i: i['timestamp'])
                    view.print_note(notes_list_1, text.load_error)
                if answer_sort == "DE":
                    notes_list_2 = sorted(nb, key=lambda i: i['timestamp'], reverse = True)
                    view.print_note(notes_list_2, text.load_error)
                if answer_sort == "FI":
                    date_to_find = view.ask_date(text.ask_year, text.ask_month, text.ask_day, text.input_date_error,text.cancel_input)
                    # print(date_to_find)
                    if date_to_find is None:
                        print(view.print_message(text.not_searching_date))
                    else:
                        list_found_date = list(filter(lambda x: x['timestamp'][:-16] == date_to_find, nb))
                        view.print_note(list_found_date, text.load_error)
                        if len(list_found_date) == 0:
                            view.print_message(text.unsuccessful_search_date)
            

            case 3:
                nb = my_nb.load()
                view.print_note(nb, text.load_error)

            case 4:
                note = view.input_note(text.new_note, text.cancel_input)
                # print(note)
                flag = True

                if len(note) < 2:
                    view.print_message(text.not_saving)
                    flag = False

                for key, value in note.items():
                    semicolon = value.find(';')
                    if semicolon != -1:
                        flag = False
                        view.print_message(text.not_saving_semicolon)
                        break

                if flag:
                    title = my_nb.add(note)
                    view.print_message(text.new_note_successful(title))
                    my_nb.save()
                
                    

            case 5:

                title_to_find = view.ask_what_title_to_find(text.what_title_to_find)
                if len(title_to_find) == 0:
                    view.print_message(text.cancel_input)
                else:
                    list_lost_and_found = my_nb.find(title_to_find)
                    if len(list_lost_and_found) == 0:
                        view.print_message(text.unsuccessful_search)
                    else:
                        # print(list_lost_and_found)
                        view.print_message(text.prepare_lost_and_found)
                        list_for_user = view.show_lost_and_found(list_lost_and_found)
                        for i,item in enumerate(list_for_user, 1):
                            print(i, '.', item)

            case 6:
                print(text.warning_about_changing_deletion)
                answer = input(text.ask_about_continuation)
                if answer == 'ДА':
                    nb = my_nb.load()
                    position = view.input_position(text.index_change_note, nb, text.load_error)
                    if position is None:
                        view.print_message(text.nothing_to_change)
                    else:
                        the_newest_note = view.input_edited_note(text.edited_note, text.cancel_input)
                        
                        # print(the_newest_note)
                        flag = True
                        if len(the_newest_note) < 2:
                            view.print_message(text.not_saving)
                            flag = False
                        for key,value in the_newest_note.items():
                            semicolon = value.find(';')
                            if semicolon != -1:
                                flag = False
                                view.print_message(text.not_saving_semicolon)
                                break
                        if flag:
                            title_of_the_newest_note = my_nb.change_note(position, the_newest_note)
                            view.print_message(text.change_note(title_of_the_newest_note))
                            my_nb.save_when_changed(position,the_newest_note)

            case 7:
                print(text.warning_about_changing_deletion)
                answer = input(text.ask_about_continuation)
                if answer == 'ДА':
                    nb = my_nb.load()
                    index_del = view.input_index(text.index_del_note, nb, text.load_error)
                    if index_del is None:
                        view.print_message(text.nothing_to_delete)
                    else:
                        title_to_delete = my_nb.del_note(index_del)
                        view.print_message(text.del_note(title_to_delete))
                        my_nb.save_when_deleted()

            case 8:
                break
                    

                
                    
                    


