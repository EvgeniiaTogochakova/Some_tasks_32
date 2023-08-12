main_menu = '''\n Главное меню Handy notebook:
1.Открыть файл (ВАША ТОЧКА СТАРТА! Пользуйтесь один раз при входе в приложение!)
2.Показать список заметок, отсортированный по дате и времени последнего изменения
  Отфильтровать заметки по дате изменения
  Опция: просмотр содержимого заметки
3.Показать список заметок в порядке добавления (с датой и временем последнего изменения) 
  Опция: просмотр содержимого заметки
4.Добавить заметку
5.Найти заметку по заголовку
6.Отредактировать заметку 
7.Удалить заметку
8.Выход\n'''

input_choice = 'Выберите пункт меню: '
load_successful = 'Файл с заметками успешно открыт'
save_successful = 'Заметки успешно сохранены'
you_did_not_save = 'появится при повторном входе в приложение'
if_FileNotFoundError = 'Файла пока нет, т.к. нет заметок. Самое время создать свою первую заметку!'
input_note = {'title': 'Введите заголовок заметки: ',
              'body': 'Введите текст (тело) самой заметки: '}
new_note = 'Введите данные для новой заметки (пустое поле для отмены): '
cancel_input = 'Отмена ввода'
note_content = 'Печатаю содержимое заметки. Читайте внизу'
not_saving = 'Извините, в вашей заметке не хватает данных. Сохранение такой заметки невозможно'
not_saving_semicolon = 'Извините, но использовать ";" в тексте заголовка или тела заметки нельзя'
load_error = 'Заметок, доступных для показа, нет либо файл с заметками не открыт.'
note_to_read = 'Укажите, пожалуйста, номер заметки, которую необходимо раскрыть: '
wrong_id = 'Неправильный номер заметки, будьте повнимательнее!'
wrong_id_with_string = 'Вы ввели не число, будьте повнимательнее!'
want_to_open_body = 'Если вы хотите открыть полный текст какой-либо заметки, нажмите 1. Не хотите - напишите любое другое число или слово. Итак: '
prepare_lost_and_found = ('Вывожу список найденных заметок (заголовок и содержимое, дата последнего изменения), \n'
                          'где номер - не идентификатор заметки, а ее номер в списке находок: ')
unsuccessful_search = 'Поиск не дал результатов. Кстати, убедитесь, что вы на старте приложения загружали файл с заметками (пункт 1 меню)'
index_del_note = 'Введите номер заметки, которую вы хотите удалить: '
deletion_confirmation = ('Этот процесс необратим. Вы точно уверены, что хотите продолжать? Напишите "ДА" (заглавными буквами), если это так.\n'
                         'Если не уверены, введите любое число или слово. Итак, ваш выбор: ')
nothing_to_delete = 'Ничего не удалено'
nothing_to_change = 'Ничего не изменено'
index_change_note = 'Введите номер заметки, которую вы хотите изменить: '
edited_note = 'Введите данные для обновленной заметки (пустое поле для отмены): '
input_edited_note = {'title': 'Введите обновленный заголовок заметки: ',
                     'body': 'Введите обновленное содержимое самой заметки: '}


def new_note_successful(title: str) -> str:
    return f'Заметка под заголовком "{title}" успешно добавлена!'


what_title_to_find = ('Убедитесь, что файл с заметками открыт (пункт 1 меню). Если передумали искать, введите пустое поле для отмены.\n'
                      'Либо все же впишите заголовок заметки или часть заголовка - ту, что помните наверняка: ')


def del_note(title: str):
    return f'Заметка с заголовком "{title}" успешно удалена!'


def change_note(title: str):
    return f'Заметка с заголовком "{title}" успешно заняла место прежней заметки!'


warning_about_changing_deletion = 'Если в этом сеансе вы добавляли или редактировали заметки и время их последнего изменения пока не отображается (пункт 2 или 3 меню),\nубедительно просим ПЕРЕД РЕДАКТИРОВАНИЕМ И УДАЛЕНИЕМ заметок выйти и снова зайти в приложение\n во избежание потери временных меток у новых/измененных заметок'

ask_about_continuation = 'Если вы хотите продолжать, напишите ДА (заглавными буквами): '

ask_how_to_sort_or_filter = 'Если вы хотите отсортировать заметки по дате и времени последнего изменения в порядке возрастания, введите "AS"(заглавными буквами),\nесли в порядке убывания - "DE",\nесли ввыбрать заметки по дате последнго изменения - "FI": '

ask_year = 'Для поиска заметок по определенной дате используйте числовой формат. Введите, пожалуйста, год: '
ask_month = 'Введите месяц: '
ask_day = 'Введите день (число месяца): '
input_date_error = 'Искать что-либо по этим входным данным невозможно'
not_searching_date = 'Валидных данных для поиска заметок по дате изменения не поступило. Попробуйте снова'
unsuccessful_search_date = 'Заметок с такой датой не найдено. Кстати, проверьте, что вы в начале сеанса загружали файл с заметками (пункт 1 меню)'
