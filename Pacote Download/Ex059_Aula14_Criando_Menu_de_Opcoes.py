# #Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
#
# [ 2 ] multiplicar
#
# [ 3 ] maior
#
# [ 4 ] novos números
#
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
print('''Menu:
        [ 1 ] SOMAR
        [ 2 ] SUBTRAIR
        [ 3 ] MULTIPLICAR
        [ 4 ] DIVIDIR
        [ 5 ] SAIR''')
soma = 0
multiplicacao = 0
divisao = 0
substracao = 0
escolha = 0
while escolha != 5:
    escolha = int(input('Qual a sua opção? '))
    if escolha == 1:
        soma = n1 + n2
        print('A soma dos valores digitados é: {}'.format(soma))
    if escolha == 2:
        substracao = n1 - n2
        print('A subtração dos valores digitados é: {}'.format(substracao))
    if escolha == 3:
        multiplicacao = n1 * n2
        print('A multiplicação dos valores digitados é: {}'.format(multiplicacao))
    if escolha == 4:
        divisao = n1 / n2
        print('A divisão dos valores digitados é: {}'.format(divisao))
print('Fim do Cálculo')
