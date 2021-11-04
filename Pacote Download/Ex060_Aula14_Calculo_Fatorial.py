# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#
# 5! = 5 x 4 x 3 x 2 x 1 = 120
from math import factorial
numero = int(input('Digite um número: '))
calculo = factorial(numero)
print('O fatorial de {} é {}'.format(numero, calculo))
print('\n')
#######################################################
n = int(input('Digite um numero: '))
c = n
f = 1 #para obter uma multiplicacao limpa o valor tem q começar em 1.. pq o numero * 1 é ele proprio
print('Calculado {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
    f *= c
print('{}'.format(f))
