from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o Computador jogou {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!')
            v += 1
        else:
            print('Você PERDEU! =(')
            break
    elif tipo == 'I':
        if total != 0:
            print('Você Venceu!! =)')
            v += 1
        else:
            print('Você Perdeu =( !')
            break
    print('Vamos jogar novamente')
print(f'Você conseguiu um total de {v} Vitória(s), Parabéns!')
