sal = float(input('Salario atual: R$'))
aum = sal*15/100
print('O salario é R${}, com o aumento de 15% o salario passara para R${:.2f}'.format(sal, sal+aum))
