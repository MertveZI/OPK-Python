# Задача «Баланс скобок(продвинутая версия)» ОПК ФФ НГУ
# Стерлягов Сергей, 24310, 2025г

def bracket_balance(stroke):
    """ Получает на вход строку. Если скобки в ней сбалансированы, выводит True. В ином случае выводит False"""

    # Убираем из строки все кроме скобок
    clear_stroke = [x for x in stroke if x in '({[]})']
    stroke = ''.join(clear_stroke)
    del clear_stroke

    mid = len(stroke) // 2

    # Проверяем половины на соответствие
    if stroke[:mid] == stroke[mid:][::-1].replace(')','(').replace('}','{').replace(']','['):
        return True
    else:
        return False


# Пример использования
if __name__ == "__main__":
    # Приветственное сообщение и снятие данных
    stroke = input('\n Программа баланс скобок\
                                \n Введите строку: ')
    # Вывод ответа
    if bracket_balance(stroke):
        print('Все отлично!') 
    else: 
        print('Скобки не отбалансированы!')
else:
    print('Скрипт импортирован!') # Вывод сообщения об импортированности скрипта