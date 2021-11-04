# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
sequencia = [] #cria uma lista vazia
for conta in range(1,6):
    peso = float(input('Digite o {}º peso: '.format(conta)))
    sequencia.append(peso) #armazena os valores digitados no peso dentro da lista
    pesomax = max(sequencia) #armazena o numero maior dentro da lista
    pesomin = min(sequencia) #armazena o menor numero dentro da lista
print('O peso maior digitado foi {} Kg '.format(pesomax))
print('O peso maior digitado foi {} Kg '.format(pesomin))


#Feito pelo professor
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Digite o {}º peso: '.format(p)))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior
            maior = peso
        if peso < menor
            menor = peso
print('O peso maior digitado foi {} Kg '.format(maior))
print('O peso maior digitado foi {} Kg '.format(menorx''))


