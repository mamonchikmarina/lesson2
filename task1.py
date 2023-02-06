from random import randint
days_num = int(input('Введите количество дней: '))
warm_days, max_warms_days = 0, 0
for _ in range(days_num):
    temp = randint(-50, 50)
    print(temp, end=' ')
    if temp > 0:
        warm_days += 1
    else:
        if warm_days > max_warms_days:
            max_warms_days = warm_days
        warm_days = 0
print()
if warm_days > max_warms_days:
    max_warms_days = warm_days
print(f'Самая длинная оттепель длилась {max_warms_days} дня/дней')