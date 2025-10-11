from quicksort import quick_sort

people = input().replace(' ', '').split(',')

num = len(people)

people = quick_sort(people)

for i in range