#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
print('Super Gerador de PA')
print('--*' * 8)
numero = int(input('Termo da PA: '))
razao = int(input('Intervalo: '))
termo = numero
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} --> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais voce quer mostrar? '))
print('Sessao finalizada com {} termos mostrados'.format(total))
print('FIM')