# Функция номер дня в году
def day_num(day, month, year):
    # Проверка на корректность ввода
    try:
        d = int(day)
        m = int(month)
        y = int(year)
    except ValueError:
        return 'невозможный'
    except Exception:
        return 'невозможный'
    else:
        # Проверка на високосность
        if y < 0:
            return 'невозможный'
        elif int('00' + str(year)[-2:]) % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            months = [31, 29, 31, 30, 31, 30, 31, 31, 30,31, 30, 31]
        else:
            months = [31, 28, 31, 30, 31, 30, 31, 31, 30,31, 30, 31]
        # Проверка на то, что такой день в месяце есть
        if m > months[m-1]:
            return 'невозможный'
        # else:
        ans = d
        for i in range(m-1):
            ans += months[i]
        return ans
        
# Снятие данных и вывод ответа       
day, month, year = input('Введите дату в формате дд.мм.гггг: ').split('.')
print(day, month,year, '-', day_num(day, month, year), 'день года')
#Реальзовать через datetime