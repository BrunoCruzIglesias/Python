#Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    num = int(input('Digite um número para saber sua tabuada: '))
    if num < 0:
        break
    print('_' * 15)
    for mult in range(1, 11):
        print(f'{num} x {mult:2} = {num * mult:<}')
    print('_' * 15)
print('--=--' * 10)
print('Programa TABUADA encerrado. Volte sempre!')



#outra SOLUÇÃO
# print('TABUADA')
# while True:
#     n = int(input('digite um número: '))
#     if n < 0:
#         break
#     d = 1
#     while d <= 10:
#         print(f'{n} x {d} = {n*d}')
#         d += 1
# print('FIM')