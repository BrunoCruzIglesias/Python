# Programa que calcule o valor a ser pago por um produto, considerando seu preço normal
#  e condição de pagamento:
# à vista dinheiro ou cheque ganha 10% de desconto
# à vista no crédito ganha 5% de desconto
# em até 2x no cartao preço normal (sem juros)
#  em 3x ou mais acréscimo de 20% de juros

valor_produto = float(input('Qual o valor do produto? R$'))
print('Digite: 1 para dinheiro/cheque --- ou --- 2 para cartão de crédito')
pagamento = int(input())
if pagamento == 1:
    desconto = valor_produto * 10 / 100
    valor_desconto = valor_produto - desconto
    print('Você ganhou 10% de desconto, o total a ser pago será R${:.2f}'.format(valor_desconto))

if pagamento == 2:
    print('Você selecionou a opção crédito! \nPara crédito à vista digite 1\nPara crédito parcelado digite 2')
    parcela = int(input())
    if parcela == 1:
        desconto = valor_produto * 5 / 100
        valor_desconto = valor_produto - desconto
        print('Você ganhou 5% de desconto, o total a ser pago será R${:.2f}'.format(valor_desconto))
    elif parcela == 2:
        print('Em quantas vezes você deseja parcelar?')
        parc = int(input())
        if parc == 2:
            print('Você vai pagar R${:.2f} em {} parcelas de R${:.2f} cada'.format(valor_produto, parc, valor_produto / parc))
        elif parc > 3:
            acrescimo = valor_produto * 20 / 100
            valor_acrescimo = valor_produto + acrescimo
            print('Você vai pagar R${:.2f} em {} parcelas de R${:.2f} cada'.format(valor_acrescimo, parc, valor_acrescimo / parc))
