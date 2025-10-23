# Задача «Номер дня в году» ОПК ФФ НГУ
# Стерлягов Сергей, 24310, 2025г

import datetime


def day_num(day, month, year):
    """ Получает на вход дату, находит по ней номер дня в году. """
    try: 
        day = int(day)
        month = int(month)
        year = int(year)
        date = datetime.date(year, month, day)
    except ValueError:
        return 'Некорректная дата!'
    except Exception:
        return 'Непредвиденная ошибка!'
    result = (date - datetime.date(year,1,1)).days + 1 # Вычисление разницы в днях
    return result


# Пример использования
if __name__ == "__main__":
    day, month, year = input('\n Программа вычисления номера дня в году\
                            \n Введите дату в формате дд.мм.гггг: ').split('.')
    print(day, month,year, '-', day_num(day, month, year), 'день года') # Вывод ответа
