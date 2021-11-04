# Leia duas notas de um aluno e calcule a media dizendo:
# - média abaixo de 5 reprovado
# - média entre 5.0 e 6.9 recuperação
# - média 7.0 ou superior aprovado

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
print('Média Final: {}'.format(media))

if media >= 7.0:
    print('PARABÉNS!! Você foi APROVADO(A)')
elif media >= 5.0 and media < 7.0:   # pode ser tb:   if 7 > media >= 5:
    print('ATENÇÃO!! Você está em RECUPERAÇÂO')
# elif media < 5.0:
#     print('Que BAD!! Você está REPROVADO(A)')
else:
   print('Que BAD!! Você está REPROVADO(A)')
