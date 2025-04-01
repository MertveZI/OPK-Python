


def bracket_balance(stroke):
    """ Получает на вход строку. Если скобки в ней сбалансированы, выводит True. В ином случае выводит False"""
    aok = True; bok = True; cok = True 
    strokesk = ''
    for elem in stroke:
        if elem in '({[]})':
            strokesk += elem
    Len = len(strokesk)
    if Len % 2 == 1:
            print('AAA')
            if strokesk[Len//2 +1] == '(':
                aok = False
            elif strokesk[Len//2 +1] == '[':
                bok = False
            elif strokesk[Len//2 +1] == '{':
                cok = False
            strokesk.pop(Len//2 +1)
    for num in range(Len//2):
        if strokesk[(-num)-1] + strokesk[num] == ')(' or strokesk[(-num)-1] + strokesk[num] == '][' or strokesk[(-num)-1] + strokesk[num] == "}{":
            pass
        else:
            if strokesk[num] == '(':
                aok = False
            elif strokesk[num] == '[':
                bok = False
            elif strokesk[num] == '{':
                cok = False
    if aok == bok == cok == True:
        print('OK')
    else:
        if aok == False:
            print("проблемы с круглыми скобками")
        if bok == False:
            print("проблемы с квадратными скобками")
        if cok == False:
            print("проблемы с фигурными скобками")

stroke = input("введите строку: ")
        