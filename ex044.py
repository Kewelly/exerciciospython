produto = float(input('Qual o valor do produto ? '))
pag = input('Forma de pagamento: ')
des10 = produto * 10 / 100
des5 = produto * 5 / 100
juros = produto * 20 / 100
if pag == 'á vista' or pag == 'cheque':
    print('O produto a vista/cheque tem 10% de desconto,o preço passará á {}'.format(produto - des10))
elif pag == 'á vista no cartão':
    print('O produto á vista no cartão tem 5% de desconto, o produto passará á {}'.format(produto - des5))
elif pag == '2x no cartão':
    print('O produto custa {}'.format(produto))
else:
    print('O produto terá 20% de juros, passará a custar {}'.format(produto + juros))
