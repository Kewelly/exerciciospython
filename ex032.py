from datetime import date
ano = int(input('Dígite um ano'))
bi = ano % 4
if ano == 0:
    ano = date.today().year
if bi == 0 and ano % 100 != 0 or ano % 400 == 0:#
    print('Ano {} é bissexto'.format(ano))
else:
    print('Ano {} não é bissexto'.format(ano))
