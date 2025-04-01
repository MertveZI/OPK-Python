# Задача «Счастливые билеты (продвинутая версия)» ОПК ФФ НГУ
# Стерлягов Сергей, 24310, 2025г

from collections import defaultdict
import itertools
import math as m


# Функция вычисления доли счасливых билетов от их длины
def lucky_tickets_frac(length):
    try:
        length = int(length)
    except ValueError:
        raise Exception('Введено не число!') # Проверка на то, что length число
    except Exception:
        raise Exception('Непредвиденная ошибка!') # Непредвиденная ошибка
    if length % 2 != 0:
        raise Exception('Введено нечетное число!') # Проверка на четность
    elif length > 32:
        raise Exception('Введено число болше 32!') # Проверка на ограничение по длине
    L_half = length//2
    result = 0 # Переменная под ответ
    Fact = m.factorial(L_half) # Константа факториала
    sums = defaultdict(lambda: 0) # Словарь с суммами
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # Список цифр
    # Создание списка всех возможных комбинаций
    kombs = list(itertools.combinations_with_replacement(nums, L_half)) 
    # Заполнение словаря сумм значениями
    for elem in kombs:
        s = sum(elem) # Нахождение суммы комбинации
        uniq_nums = list(set(elem)) # Нахождение уникальных элементов
        # Вычисление количества перестановок
        permutations = Fact 
        for i in uniq_nums:
            permutations = permutations // m.factorial(elem.count(i))
        # Добавление количества перестановок к значению  в словаре
        sums[s] = sums[s] + permutations
    # Итоговое ссуммирование
    for i in range((9*L_half) + 1):
        result += sums[i] ** 2
    # Вычисление доли
    fraction = result / (10 ** length)
    # Вывод ответа
    return fraction


# Пример использования
if __name__ == "__main__": # Проверка на импортированность
    # Приветственное сообщение и снятие данных
    length = input('\n Программа вычисления доли счастливых билетов\
                    \n Введите длину билета(четное число <= 32): ')
    print("Доля счастливых билетов:", lucky_tickets_frac(length)) # Вывод ответа
else:
    print('Скрипт импортирован!') # Вывод импортированности скрипта
