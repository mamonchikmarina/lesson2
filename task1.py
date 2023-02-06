"""Задача 10
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все
монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество
монет, которые нужно перевернуть.
"""

from random import randint
coin_num = int(input('Введите количество монет: '))
heads, tails = 0, 0
for _ in range(coin_num):
    temp = randint(0, 1)
    print(temp, end=' ')
    if temp > 0:
        heads += 1
    else:
        tails += 1
print()
if heads > tails:
    print(f'Необходимо перевернуть {tails} монет')
else:
    print(f'Необходимо перевернуть {heads} монет')
