peso = float(input('Diga seu peso:'))
altura = float(input('Diga sua altura:'))
imc = peso / (altura * altura)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está \033[31mabaixo do peso.')
elif imc == 18.5 or imc < 25:
    print('Você está no peso \033[34mideal.')
elif imc == 25 or imc < 30:
    print('Você está com \033[31msobrepeso.')
elif imc == 30 or imc < 40:
    print('Você está com \033[31mobesidade.')
else:
    print('Você está com \033[31mobesidade mórbida')
