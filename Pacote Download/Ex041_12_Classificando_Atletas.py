# Equipe de natação quer um programa que leia o ano que o atleta nasceu
#   e diga qual categoria ele se encaixa:
#       até 9 anos: mirim
#       até 14 anos: infantil
#       até 19 anos: junior
#       até 20 anos: master
from datetime import date
ano_nasc = int(input('Digite o ano de nascimento do Atleta: '))
ano_atual = date.today().year

if ano_atual - ano_nasc <= 9:
    print('Sua categoria é MIRIM')
elif ano_atual - ano_nasc <= 14:
    print('Sua categoria é INFANTIL')
elif ano_atual - ano_nasc <= 19:
    print('Sua categoria é JUNIOR')
elif ano_atual - ano_nasc <= 25:
    print('Sua categoria é SÊNIOR')
elif ano_atual - ano_nasc > 25:
    print('Sua categoria é MASTER.')
