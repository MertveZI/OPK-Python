from DynStack import DynamicStack


stack = DynamicStack()
while True:
    command = input()
    if command == 'stop':
        break
    elif command == 'help':
        print('Список команд:\n' \
        'stop - выход из примера использования\n' \
        'display - вывод всех элементов стека\n' \
        'peek - вывод первого элемента стека\n' \
        'size - вывод количества элементов стека\n' \
        'is_empty - возвращает True, если стек пустой, иначе False\n' \
        'append - добавляет элемент в стек\n' \
        'pop - убирает верхний элемент стека\n')
    elif command == 'display':
        print(stack.display())
    elif command == 'peek':
        print(stack.peek())
    elif command == 'size':
        print(stack.size())
    elif command == 'is_empty':
        print(stack.is_empty())
    elif command == 'append':
        elem = input('Введите новый элемент: ')
        stack.append(elem)
    elif command == 'pop':
        stack.pop()
        print('Элемент удален')
    else:
        print('Неизвестная команда, введите help для вывода всех команд')
