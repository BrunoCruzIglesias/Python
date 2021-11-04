# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('-=' * 8)
print('GERADOR DE P.A')
print('-=' * 8)
num = int(input('1º termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
termo = num
contador = 1
while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    contador += 1
print('FIM')
