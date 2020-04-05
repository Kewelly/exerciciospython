salario = float(input('Quanto é o seu salário?'))
aum1 = salario*15/100
aum2 = salario*10/100
if salario < 1250:
    print('O seu salário teve um aumento de {}'.format(salario+aum1))
else:
    print('O seu salário teve um aumento de {}'.format(salario+aum2))
