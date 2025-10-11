class DynamicStack:
    '''Динамический стек'''
    def __init__(self):
        self.items = []

    def display(self):
        '''Возвращает все элементы стека для просмотра'''
        return '\n'.join(self.items)

    def peek(self):
        '''Возвращает элемент с вершины стека без удаления'''
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.items[-1] 
    
    def size(self):
        '''Возвращает количество элементов в стеке'''
        return len(self.items)
    
    def is_empty(self):
        '''Проверяет, пуст ли стек'''
        if self.size() == 0:
            return True
        else:
            return False  
    
    def append(self, item):
        '''Добавляет элемент на вершину стека'''
        self.items.append(item)
    
    def pop(self):
        '''Удаляет и возвращает элемент с вершины стека'''
        if self.is_empty():
            raise IndexError('Stack is empty!')
        return self.items.pop()
    

