# Задача «Быстрая сортировка» ОПК ФФ НГУ
# Стерлягов Сергей, 24310, 2025г

def quick_sort(array, low=0, high= -1):
    """ Получает на вход несортированный массив. Сортирует его алгоритмом Хоара. """
    if high == -1:
        high = len(array) - 1  #Только при первом вызове
    
    if low < high:
        # Разделение массива и получение индекса разделения
        base_id = hoare_partition(array, low, high)
        
        # Рекурсивная сортировка левой и правой частей
        quick_sort(array, low, base_id)
        quick_sort(array, base_id + 1, high)

def hoare_partition(array, low, high):
    """Разделение массива по схеме Хоара."""
    # Выбираем опорный элемент (середина)
    base = array[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        # идем справа
        i += 1
        while array[i] < base:
            i += 1
        # идем слева
        j -= 1
        while array[j] > base:
            j -= 1
        # сошлись
        if i >= j:
            return j
        # Меняем местами элементы, нарушающие порядок
        array[i], array[j] = array[j], array[i]

def test_1():
    arr = []
    expected_result = []
    quick_sort(arr)
    assert arr == expected_result

def test_2():
    arr = [1]
    expected_result = [1]
    quick_sort(arr)
    assert arr == expected_result

def test_3():
    arr = [2, 1]
    expected_result = [1, 2]
    quick_sort(arr)
    assert arr == expected_result

# Пример использования
if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    # array = list(map(int, input('\nПрограмма быстрой сортировки' \
    # '\nВведите массив через запятую: ').replace(' ', '').split(',')))
    # quick_sort(array)
    # print('Отсортированный массив:', array)