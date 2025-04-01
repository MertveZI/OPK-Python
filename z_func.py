# Задача «Поиск подстроки в строке» ОПК ФФ НГУ
# Стерлягов Сергей, 24310, 2025г

def zfunc(stroke):

    length = len(stroke)

    # Создаем список из нулей, длиной как и строка
    z_list = [0] * length

    left_id, right_id = 0, 0

    for i in range(length):
        if i > right_id:
            left_id = right_id = 1
            while right_id < length and stroke[right_id - left_id] == stroke[right_id]:
                right_id += 1
            z_list[i] = right_id - left_id

    return z_list






# Пример использования
if __name__ == "__main__": # Проверка на импортированность
    # Приветственное сообщение и снятие данных
    day, month, year = input('\n Программа вычисления номера дня в году\
                            \n Введите дату в формате дд.мм.гггг: ')
    print(day, month,year, '-', zfunc(day, month, year), 'день года') # Вывод ответа

else:
    print('Скрипт импортирован!') # Вывод сообщения об импортированности скрипта
