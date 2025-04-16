# Задача «Сортировка выбором» ОПК ФФ НГУ
# Стерлягов Сергей, 24310, 2025г


def id_min_elem(array):
    """ Получает на вход массив, находит в нем минимальный элемент """
    if not array:
        return 'Массив пуст!'  # Обработка пустого массива, если требуется
    min_id = 0 
    min_elem = array[0]
    for i in range(len(array)):
        try:
            if array[i] < min_elem:  
                min_id = i
                min_elem = array[i]
        except TypeError:
            return 'В массиве разные типы данных!'
    return min_id


def selection_sort(array):
    """ Получает на вход несортированный массив. Сортирует его выбором. """
    length = len(array)
    if length > 1: 
        for i in range(length - 1): 
            # "Встаем" на элемент массива
            min_id = i 
            # Находим индекс минимального элемента в оставшейся части массива
            min_id = id_min_elem(array[i::])
            # Меняем найденный минимальный элемент с текущим
            array[i], array[i + min_id] = array[i + min_id], array[i]


# Пример использования
if __name__ == "__main__": # Проверка на импортированность
    # Приветственное сообщение и снятие данных
    array = list(map(int, input('\n Программа сортировки выбором\
                                \n Введите массив через запятую: ').replace(' ', '').split(',')))
    selection_sort(array)
    print('Отсортированнный массив: ', array) # Вывод ответа
else:
    print('Скрипт импортирован!') # Вывод сообщения об импортированности скрипта