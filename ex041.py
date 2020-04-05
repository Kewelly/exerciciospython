from datetime import date
nas = int(input('Escreva o ano que você nasceu: '))
idade = date.today().year - nas
print('O atleta tem {} ans.'.format(idade))
if idade <= 9:
    print('Categoria mirim.')
elif idade <= 14:
    print('Categoria infantil.')
elif idade <= 19:
    print('Categoria junior.')
elif idade <= 25:
    print('Categoria sênior.')
else:
    print('Categoria master')
