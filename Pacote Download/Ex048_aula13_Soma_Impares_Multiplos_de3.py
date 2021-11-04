# Faça um programa que calcule a soma entre todos os números
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1   #um contador sempre conta + 1
        s += c      #um acumulador sempre vai acumulando os resultados e somando a ele
print('A soma de todos os {} valores solicitados é: {}'.format(cont, s))
