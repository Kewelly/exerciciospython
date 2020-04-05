from datetime import date
nas = int(input('Escreva o ano que você nasceu: '))
idade = date.today().year - nas
print('Você tem {} anos.'.format(idade))
saldo1 = idade - 18
saldo2 = 18 - idade
if idade > 18:
    print('Você deveria ter se alistado há {} anos atrás.'.format(saldo1))
elif idade < 18:
    print('Você ainda irá se alistar, falta {} anos.'.format(saldo2))
else:
    print('É hora de você se alistar aos serviços militares')

