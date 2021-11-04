#Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#
# A) qual é o total gasto na compra.
#
# B) quantos produtos custam mais de R$1000.
#
# C) qual é o nome do produto mais barato.
total = totmil = 0
menor = 0 #menor pra saber qual o menor produto
cont = 0 #contador pra saber quantos produtos tem
barato = '' #essa variavel vai receber o nome do produto
while True:
    produto = str(input('Nome do Produto: ')).strip().upper()
    preço = float(input('Digite o valor do Produto R$ '))
    cont += 1 #aqui ele vai armazenar o primeiro produto
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:       #se contador for o primeiro produto:
        menor = preço   #entao menor recebe o preço do primeiro produto
        barato = produto
    else:
        if preço < menor:   #se o preço do proximo produto for menor que o que ja foi armazenado na variavel 'menor'
            menor = preço   #entao a variavel 'menor' recebe o novo preço menor.
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer adicionar mais produtos [S/N]? ')).strip().upper()[0]
    if resp in 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total gasto na compra é R${total:.2f}')
print(f'{totmil} produtos custaram mais de mil reais')
print(f'O produto mais barato é o/a {barato} que custou R${menor:.2f}')

# if cont == 1 or preço < menor:    simplificando a condicao do MENOR PREÇO:
#     menor = preço
#     barato = produto
