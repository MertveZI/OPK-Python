# Задача «Номер дня в году» ОПК ФФ НГУ
# Стерлягов Сергей, 24310, 2025г

import datetime


def day_num(day, month, year):
    """ Получает на вход дату, находит по ней номер дня в году. """
    try: # Проверка на корректность ввода
        day = int(day)
        month = int(month)
        year = int(year)
        date = datetime.date(year, month, day)
    except ValueError:
        return 'Некорректная дата!' # В случае если неправильный формат даты или дне в месяце не существует
    except Exception:
        return 'Непредвиденная ошибка!' # Сообщение о непредвиденной ошибке
    result = (date - datetime.date(year,1,1)).days + 1 # Вычисление разницы в днях
    return result # Вывод результата работы функции


# Пример использования
if __name__ == "__main__":
    # Приветственное сообщение и снятие данных
    day, month, year = input('\n Программа вычисления номера дня в году\
                            \n Введите дату в формате дд.мм.гггг: ').split('.')
    print(day, month,year, '-', day_num(day, month, year), 'день года') # Вывод ответа

else:
    print('Скрипт импортирован!') # Вывод сообщения об импортированности скрипта