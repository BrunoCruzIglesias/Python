print('Escolha um número de 0 a 20 quando for pedido')
while True:
    n1 = int(input('Digite um número: '))
    while n1 < 0 or n1 > 20:
        n1 = int(input('Digite novamente o primeiro número: '))
    n2 = int(input('Digite outro número: '))
    while n2 < 0 or n2 > 20:
        n2 = int(input('Digite novamente o segundo número: '))
    n3 = int(input('Digite mais um número: '))
    while n3 < 0 or n3 > 20:
        n3 = int(input('Digite novamente o terceiro número: '))
    n4 = int(input('Digite o último número: '))
    while n4 < 0 or n4 > 20:
        n4 = int(input('Digite novamente o último número: '))

    tup = (n1, n2, n3, n4)
    break
print(tup)
print(type(tup))


