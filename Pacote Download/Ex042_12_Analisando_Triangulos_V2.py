# Refaça o desafio dos triangulos da aula 35 e acrescente
# o recurso pra mostrar o tipo de triangulo que ele é:
#   Equilátero = todos os lados iguais
#   Isósceles = dois lados iguais
#   Escaleno = todos os lados diferentes

# r1 = float(input('Digite o primeiro segmento de reta: '))
# r2 = float(input('Digite o segundo segmento de reta: '))
# r3 = float(input('Digite o terceiro segmento de reta: '))
#
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:  #aqui faz o teste se o triangulo pode existir, se ele n puder ele nem faz o bloco abaixo
#     print('Os segmentos acima podem formar um triangulo')
#     if r1 == r2 and r1 == r3:   #esse IF só acontece se o triangulo existir, aqui ele diz qual a categoria do triangulo
#         print('Este é um triângulo Equilátero, pois possui todos os lados iguais')
#     elif (r1 == r2 and r1 and r2 != r3) or (r1 == r3 and r1 and r3 != r2) or (r2 == r3 and r2 and r3 != r1):
#         print('Este é um triângulo Isósceles, pois possui dois lados iguais e um diferente')
#     elif r1 != r2 and r1 != r3 and r2 != r3:
#         print('Este é um triângulo Escaleno, pois possui todos os lados diferentes.')
# else:
#     print('Os segmentos acima NÃO podem formar triangulo')

#jeito do professor
r1 = float(input('Digite o primeiro segmento de reta: '))
r2 = float(input('Digite o segundo segmento de reta: '))
r3 = float(input('Digite o terceiro segmento de reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:  #aqui faz o teste se o triangulo pode existir, se ele n puder ele nem faz o bloco abaixo
    print('Os segmentos acima podem formar um triangulo')
    if r1 == r2 == r3:
        print('Este é um triângulo Equilátero, pois possui todos os lados iguais')
    elif r1 != r2 != r3 != r1:
        print('Este é um triângulo Escaleno, pois possui todos os lados diferentes.')
    else:
        print('Este é um triângulo Isósceles, pois possui dois lados iguais e um diferente')
else:
    print('Os segmentos acima NÃO podem formar triangulo')

