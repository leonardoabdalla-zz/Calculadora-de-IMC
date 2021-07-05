print('--------------------Calculadora de IMC---------------------')
nome = input('Qual seu nome? ').capitalize()
peso = float(input('{} , qual seu peso? (KG) '.format(nome)))
altura = float(input('{} qual sua altura? (M) '.format(nome)))
imc = peso / (altura * altura)
pesoIdealMninimo = 18.5 * (altura ** 2)
pesoIdealMaximo = 25 * (altura ** 2)
if imc < 18.5:
    print('{}, seu imc é {:.1f}, você está abaixo do peso'.format(nome, imc))
    print('Seu peso ideal é entre {:.1f} e {:.1f}'.format(pesoIdealMninimo, pesoIdealMaximo))
elif imc >= 18.5 and imc <= 25:
    print('{}, seu imc é {:.1f}, você está no peso ideal'.format(nome, imc))
    print('Seu peso ideal é entre {:.1f} e {:.1f}'.format(pesoIdealMninimo, pesoIdealMaximo))
elif imc > 25 and imc <= 30:
    print('{}, seu imc é {:.1f}, você está com sobrepeso'.format(nome, imc))
    print('Seu peso ideal é entre {:.1f} e {:.1f}'.format(pesoIdealMninimo, pesoIdealMaximo))
elif imc > 30 and imc <= 40:
    print('{}, seu imc é {:.1f}, você está obeso'.format(nome, imc))
    print('Seu peso ideal é entre {:.1f} e {:.1f}'.format(pesoIdealMninimo, pesoIdealMaximo))
else:
    print('SEU IMC É DE {:.1f}\n =======OBESIDADE MÓRBIDA!!!=======')
    print('Seu peso ideal é entre {:.1f} e {:.1f}'.format(pesoIdealMninimo, pesoIdealMaximo))