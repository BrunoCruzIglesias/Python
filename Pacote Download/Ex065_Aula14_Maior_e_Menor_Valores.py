#Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
soma = quantidade = media = maior = menor = 0   #se todoas as variaveis forem receber o mesmo valor, elas podem
while resp in 'Ss':                             #ser colocadas uma ao lado da outra dizendo que todas elas recebem zero
    n = int(input('Digite um número: '))
    soma += n
    quantidade += 1
    if quantidade == 1:     #aqui ele testa q se ele receber o primeiro numero ele será ao mesmo tempo:
        maior = menor = n   #maior e menor pq é o primeiro numero digitado ocupando a quantidade = 1
    else:
        if n > maior:       #aqui ele vai se basear no primeiro IF, onde se segundo numero digitado for maior que o anterior
            maior = n       #aí a variavel maior vai receber o valor do numero que no caso será o maior
        if n < menor:       #aqui ele vai fazer o mesmo teste de cima mas pegando o menor numero
            menor = n       #a variável menor vai recebe o menor valor digitado (mesmo q ele tenha sido o primeiro valor)
    resp = str(input('Quer continuar [S/N]? ')).strip().upper()
media = soma / quantidade
print('A média dos {} valores é {}'.format(quantidade, media))
print('O maior numero digitado é {}, e o menor digitado é {}'.format(maior, menor))
