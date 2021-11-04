# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print('-=' * 20)
print('Vamos Jogar Par ou Ímpar')
print('-=' * 20)
cont = 0
while True:
    numjogador = int(input('Digite um número: '))
    escolha = str(input('Você quer par ou ímpar [P/I]? ')).strip().upper()[0]
    print('-' * 32)
    comp = randint(0, 10)
    soma = numjogador + comp
    print(f'Você escolheu o {numjogador} e o Computador escolheu o {comp} que somados dá {soma} e é ', end='')
    print('Par' if soma % 2 == 0 else 'Ímpar')
    if (soma % 2) == 0 and escolha in 'Pp':
        cont += 1
        print('Você Ganhou!')
    if (soma % 2) != 0 and escolha in 'Ii':
        cont += 1
        print('Você GanhoU!!')
    if (soma % 2) != 0 and escolha in 'Pp':
        print('Você PerdeU')
        break
    if (soma % 2) == 0 and escolha in 'Ii':
        print('Você PerdEU')
        break
print(f'voce ganhou {cont} vezes consecutivas')
