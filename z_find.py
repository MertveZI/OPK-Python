# Задача «Счастливые билеты (продвинутая версия)» ОПК ФФ НГУ
# Стерлягов Сергей, 24310, 2025г


def prefix_calc(part, pattern):
    '''Вычисляет максимальную длину общего фрагмента'''
    result = 0
    # Ищем соответствия
    for i, j in zip(part, pattern):
        if i != j:
            break
        result += 1
    return result


def z_find(stroke, pattern):
    '''Ищет все вхождения подстроки в строку с помощью Z-функции'''
    result = []
    str_len = len(stroke)
    pref = [0 for i in range(str_len)]
    pat_len = len(pattern)
    cur_pref = 0
    start, end = 0, 0
    for i in range(str_len):
        if i < end: #если конец фрагмента больше i
            if i + pref[i - start] < end: #если не вылезает за границы фрагмента
                cur_pref = pref[i-start]
            else: #если вылезает, то прощаем подсчет
                cur_pref = end - i + prefix_calc(stroke[end:], pattern[end-i:])
                if i + cur_pref > end:
                    start, end = i, i + cur_pref
        else: # Считаем префикс
            cur_pref = prefix_calc(stroke[i:], pattern)
            start, end = i, i + cur_pref
        pref[i] = cur_pref
        if cur_pref == pat_len:
            result.append(i)
    return result


# Пример использования
if __name__ == "__main__":  # Проверка на импортированность
    # Приветственное сообщение и снятие данных
    stroke = input('\n Программа вычисления индексов вхождения подстроки в строку\
                    \n Введите строку: ')
    pattern = input('Введите подстроку: ')
    print("Индексы вхождения:", z_find(stroke, pattern))
else:
    print('Скрипт импортирован!')  # Вывод импортированности скрипта