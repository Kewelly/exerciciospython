via = float(input('Quantos km tem a sua viajem?'))
if via <= 200:
    print('O valor da sua viajem será {:.2f}'.format(via * 0.50))
else:
    print('O valor da sua passagem será {:.2f}'.format(via * 0.45))
