# Задача «Сортировка слиянием» ОПК ФФ НГУ
# Стерлягов Сергей, 24310, 2025г

def merge_sort(array):
    """ Получает на фход несортированный массив. Сортирует его слиянием. """
    length = len(array)
    if length > 1:
        # Находим середину массива
        mid = length // 2
        
        # Делим массив на две половины
        left_half = array[:mid]
        right_half = array[mid:]
        
        # Рекурсивно сортируем каждую половину
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Переменные итерации
        i = j = k = 0
        
        # Сравниваем элементы из левой и правой половины и добавляем их в исходный массив
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1
        
        # Если в левой половине остались элементы, добавляем их в массив
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
        
        # Если в правой половине остались элементы, добавляем их в массив
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

# Пример использования
if __name__ == "__main__":
    array = list(map(int, input('\n Программа сортировки слиянием\
                                \n Введите массив через запятую: ').replace(' ', '').split(',')))
    merge_sort(array)
    print('Отсортированнный массив: ', array)