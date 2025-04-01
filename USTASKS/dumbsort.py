import random as rd
import time



def is_sorted(array):
    '''Функция проверки на отсортированность'''
    temp_num = array[0]
    for elem in array[1:]:
        if elem < temp_num:
            return False
        temp_num = elem
    return True


def dumbsort(array):
    '''Функция олучает на вход массив, сортирует его по-тупому'''
    length = len(array)
    while is_sorted(array) is False:
        array = rd.sample(array, length)
    return array


# Пример использования
if __name__ == "__main__":
    # Приветственное сообщение и снятиеп данных
    length = int(input('\n Программа тупой сортировки\
                            \n Введите дину массива: '))
    rd_list = [rd.randint(0,100) for x in range(length)]
    start_time = time.time()
    print(rd_list, "- исходный массив") # Вывод ответа
    rd_list = dumbsort(rd_list)
    print(rd_list, "- сортированный массив")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"The task took {elapsed_time:.2f} seconds to complete.")
else:
    print('Скрипт импортирован!') # Вывод сообщения об импортированности скрипта

