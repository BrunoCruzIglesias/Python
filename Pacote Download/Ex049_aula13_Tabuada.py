# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

n = int(input('Qual número você deseja saber a tabuada? '))
for c in range(0, 11):
    print('{} x {:2} = {:5}'.format(n, c, (n * c))) #esse :5 dentro das chaves diz o alinhamento de casas decimais
