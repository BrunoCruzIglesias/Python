#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

comp = randint(0, 11)
print('-=-' * 19)
print('Vou pensar em um número entre 0 e 10, tente advinhar...')
print('-=-' * 19)
num = int(input('Agora digite o número que eu pensei: '))
print('PROCESSANDO...')
sleep(2)
contador = 0
while num != comp:
    num = int(input('Ainda não acertou, tente novamente: '))
    contador += 1
    sleep(0.5)
    if num == comp:
        print(f'Eu escolhi o número {comp}, Parabens!! Você Acertou com {contador} tentativas =)')
print('Fim')
