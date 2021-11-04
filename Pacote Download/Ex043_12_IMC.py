# Cálculo de IMC
print("Vamos calcular seu IMC?")
nome = input("Digite o seu nome: ")
peso = float(input("Olá, {}, agora digite seu peso (em Kg, Ex: 68.9): " .format(nome)))
altura = float(input("Digite sua altura (em m, Ex: 1.80): "))

media = peso / (altura * altura)
print('Seu IMC é: {:.1f}'.format(media))
if media < 18.5:
    print("Abaixo do peso")
elif media >= 18.5 and media <= 24.9:  # poderia ser feito:  elif 18.5 <= media < 25:     /o python aceita esse tipo/
    print("Você está no seu peso ideal")
elif media>=25.0 and media<=29.9:       #                    elif 25 <= media < 30:
    print("Você está levemente acima do peso")
elif media>=30.0 and media<=34.9:       #                    elif 30 <= media < 35:
    print("Obesidade Grau 1")
elif media>=35.0 and media<=39.9:       #                    elif 35 <= media < 40:
    print("Obesidade Grau 2")
else:
    print("Obesidade grau 3(mórbida)")