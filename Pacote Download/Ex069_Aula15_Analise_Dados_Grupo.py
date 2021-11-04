#Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.
contidade = contsexo = contmulher = 0
while True:
    print('-' * 30)
    print('CADASTRO DE PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]? ')).strip().upper()
    if idade >= 18:
        contidade += 1
    if sexo in "Mm":
        contsexo += 1
    if sexo in 'Ff' and idade < 20:
        contmulher += 1
    while sexo not in 'MmFf':
        print('-' * 20)
        sexo = str(input('Sexo [M/F]? ')).strip().upper()[0]
    print('-=' * 20)
    perg = str(input('Quer cadastrar mais uma pessoa [S/N]? ')).strip().upper()[0]
    print('-=' * 20)
    while perg not in 'SsNn':
        perg = str(input('Quer cadastrar mais uma pessoa [S/N]? ')).strip().upper()
        print('-=' * 20)
    if perg in 'Nn':
        break
print('=' * 10, 'Fim do Programa', '=' * 10)
print(f'{contidade} Pessoas tem mais de 18 anos')
print(f'Foram cadastrados {contsexo} homens')
print(f'{contmulher} mulheres tem menos de 20 anos')
