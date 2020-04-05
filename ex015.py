dia = int(input('Quantidade de dias:'))
km = float(input('Quantidade de Km:'))
din = dia*60.0 + km*0.15
print('O valor a paga do carro alugado é R${:.2f}.'.format(din))