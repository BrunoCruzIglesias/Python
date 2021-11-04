#calcular o valor da prestação mensal, sendo que o valor nao pode
#exceder 30% do salario senao o emprestimo será negado
valor_casa = float(input('Qual o valor da casa que deseja comprar? R$'))
salário = float(input('Qual o seu salário? R$ '))
parcela = int(input('Em quantos anos você pretende pagar? '))
prestação = valor_casa / (parcela * 12)
empréstimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(valor_casa, parcela, prestação))
if prestação >= empréstimo:
    print('Infelizmente sua solicitação foi negada devido ao valor da parcela exceder 30% do seu salário')
else:
    print('Empréstimo concedido!')