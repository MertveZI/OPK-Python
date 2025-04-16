# Задача «Быстрая сортировка» ОПК ФФ НГУ
# Стерлягов Сергей, 24310, 2025г

def quick_sort(array):
    """ Получает на фход несортированный массив. Сортирует его по алогритму Хоара. """

    length = len(array)

    # Проверяем, что длина массива больше 1
    if length > 1: 

        # Выбираем опорный элемент(здесь - средний)
        base = array[length // 2]
        
        # Разделяем массив на три части:
        left = 0
        for i in range(length):
            if array[i]< base:
                temp = array[left]
                array[left] = array[i]
                array[i] = temp 
                left += 1
        mid = left
        for i in range(left, length):
            if array[i] == base:
                temp = array[mid]
                array[mid] = array[i]
                array[i] = temp
                mid += 1 
        array = quick_sort(array[:left+1]) + array[left:mid+1] + quick_sort(array[mid:])

# Пример использования
if __name__ == "__main__": # Проверка на импортированность
    # Приветственное сообщение и снятие данных
    array = list(map(int, input('\n Программа сортировки слиянием\
                                \n Введите массив через запятую: ').replace(' ', '').split(',')))
    quick_sort(array)
    print('Отсортированнный массив: ', array) # Вывод ответа
else:
    print('Скрипт импортирован!') # Вывод сообщения об импортированности скрипта



#Сделать меньше памяти