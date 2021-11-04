# Desenvolva um programa que leia seis números inteiros e
# mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite {}º valor: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
        #print(s)
    else:
        print('\033[31m Esse número é ímpar, não entra na contagem\033[m')
print('A soma de {} número(s) par(es) digitado(s) é: {}'.format(cont, soma))
