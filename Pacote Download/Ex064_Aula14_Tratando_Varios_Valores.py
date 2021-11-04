# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = 0
soma = 0
cont = 0
while num != 999:
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if num == 999:
        print('Fim do Programa')
print('A soma dos {} números digitados é {}'.format(cont -1, soma - 999))
print('\n')
#///////////////////////////////////////////////////
num = cont = soma = 0
num = int(input('Digite um número: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número: '))
    if num == 999:
        print('Fim do Programa')
print('A soma dos {} números digitados é {}'.format(cont, soma))
