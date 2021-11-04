# Ler dois números inteiros e compare eles
# mostrando na tela a mensagem:
# - o primeiro valor é maior
# - o segundo valor é maior
# não existe valor maior, os dois são iguais

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro número é maior')
elif n2 > n1:
    print('O segundo número é maior')
else:
    print('Ambos os números são iguais')
