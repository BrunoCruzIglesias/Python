#ler um numero inteiro qualquer e pedir ao usuario que escolha
#qual será a base de conversão:
# 1 - Binário
# 2 - octal
# 3 - hexadecimal

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para converção:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é: {}'.format(num, bin(num)[2:])) #esse [2:] significa q eu quero q pegue do segundo algarismo em diante.
elif opção == 2:
    print('{} convertido para OCTAL é: {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é: {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida!! Tente novamente.')
