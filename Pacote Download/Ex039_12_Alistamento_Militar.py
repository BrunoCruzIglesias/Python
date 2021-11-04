#programa que leia o ano de nascimento de um jovem e informe:
# Se ele ainda vai se alistar no serviço militar
# Se é a hora de se alistar
# Se já passou o tempo do alistamento
# O programa tb deverá mostrar o tempo que falta ou tempo q passou para o alistamento
import datetime
# from datetime import date
# ano_nasc = int(input('Digite o ano do seu nascimento (Ex: 1988): '))
# ano_atual = date.today().year
# calculo = ano_atual - ano_nasc
# if ano_atual - ano_nasc == 18:
#     print('Você está com {} anos, está no tempo certo de se alistar'.format(calculo))
# elif ano_atual - ano_nasc < 18:
#     print('Você está com {} anos, ainda falta(m) {} ano(s) para o alistamento.'.format(calculo, (18 - calculo)))
# elif ano_atual - ano_nasc > 18:
#     print('Você está com {} anos, já passou/passaram  {} ano(s) do alistamento'.format(calculo, (calculo - 18)))

#Jeito do professor
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta(m) {} ano(s) para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} ano(s).'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
