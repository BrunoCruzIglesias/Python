from random import randint

tupla = tuple(randint(i + 1, 9) for i in range(1, 5))
print(tupla)
print(f'O menor valor na Tupla é {min(tupla)}')
print(f'O maior valor na Tupla é {max(tupla)}')

