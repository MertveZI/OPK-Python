s = input('\nВведите строку: ')
def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False   
print(s, 'is a', is_palindrome(s), 'palindrome')