# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
print('=' * 20)
print('Os 10 Termos da PA')
print('=' * 20)
termo = int(input('Digite o 1º termo da PA: '))
intervalo = int(input('Digite o intervalo para a razão: '))
décimo = termo + (10 - 1) * intervalo
for cont in range(termo, décimo + intervalo, intervalo):
    print(cont, end='-> ')
print('Fim')
