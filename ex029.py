vl = (float(input('Dígite a velocidade do seu carro:')))
if vl > 80:
    print('Você foi multado, sua multa é {:.2f}.'.format((vl-80)*7))
else:
    print('Parabéns, você está de acordo com a lei.')
