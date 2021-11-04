# jogo de pedra, papel e tesoura
from random import choice
from time import sleep
escolha = str(input('Escolha Pedra, Papel ou Tesoura: ')).capitalize().strip().title()
print('Você: {}'.format(escolha))
lista = ['Pedra', 'Papel', 'Tesoura']
cpu = choice(lista)
sleep(1)
print('Computador: {}'.format(cpu))
if escolha == 'Pedra' and cpu == 'Pedra':
    print('Empatou')
elif escolha == 'Pedra' and cpu == 'Papel':
    print('Computador ganhou!')
elif escolha == 'Pedra' and cpu == 'Tesoura':
    print('Você ganhou!')

if escolha == 'Papel' and cpu == 'Pedra':
    print('Você Ganhou!!')
elif escolha == 'Papel' and cpu == 'Papel':
    print('Empatou!!')
elif escolha == 'Papel' and cpu == 'Tesoura':
    print('Você Perdeu!')

if escolha == 'Tesoura' and cpu == 'Pedra':
    print('Você Perdeu!!')
elif escolha == 'Tesoura' and cpu == 'Papel':
    print('Você Ganhou!!')
elif escolha == 'Tesoura' and cpu == 'Tesoura':
    print('Empatou!')

