#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
anoatual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input('Digite o {}º ano de nascimento: '.format(c)))
    calc = anoatual - nasc
    if calc > 17:
        totmaior += 1
    else:
        totmenor += 1
print('{} pessoa(s), já atingiu/atingiram a maior idade'.format(totmaior))
print('{} pessoa(s), é/são menore(s) de idade'.format(totmenor))
