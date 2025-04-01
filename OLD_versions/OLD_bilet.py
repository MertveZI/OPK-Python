import itertools
import math as m



start = input('\n Программа вычисления доли счастливых билетов \n Нажмите любую кнопку для старта:')
ans = 0 # Переменная под ответ
f16 = m.factorial(16) # Для удобства
sums = {} # Словарь с возможными суммами
for i in range(145): # Заполнение этого словаря ключами
    sums[i]=0
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # Список цифр
kombs = list(itertools.combinations_with_replacement(nums, 16)) # Создание списка всех возможных комбинаций
# Заполнение словаря сумм значениями
for elem in kombs:
    s = sum(elem)
    a = list(set(elem))
    p = f16
    for i in a:
        p = p // m.factorial(elem.count(i))
    sums[s] = sums[s] + p
# Итоговое ссуммирование
for i in range(145):
    ans += sums[i] ** 2
# Вычисление доли
fraction = ans / (10 ** 32)
# Вывод ответа
print("Доля счастливых билетов:", fraction)
