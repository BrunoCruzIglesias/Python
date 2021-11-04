#  Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#  Exemplos de palíndromos:
#
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input('Digite uma frase: ')).strip().upper() #strip elimina os espaços antes e depois da frase
palavras = frase.split()  # o split divide as palavras em lista
junto = ''.join(palavras) # e o join junta a lista sem os espaços numa string só
inverso = ''
for letra in range(len(junto) - 1, -1, -1):     #aqui foi a estrutura para inverter a string
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um PALÍNDROMO')
else:
    print('Não temos um PALÍNDROMO')

print('\n\n')
#fazendo sem o FOR ficaria:
frase = str(input('Digite uma frase: ')).strip().upper() #strip elimina os espaços antes e depois da frase
palavras = frase.split()  # o split divide as palavras em lista
junto = ''.join(palavras) # e o join junta a lista sem os espaços numa string só
inverso = junto[::-1]
print(junto, inverso)
if inverso == junto:
    print('Temos um PALÍNDROMO')
else:
    print('Não temos um PALÍNDROMO')

