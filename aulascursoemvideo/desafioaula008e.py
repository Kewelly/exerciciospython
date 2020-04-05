import random
name = input('nome1:')
name2 = input('name2')
name3 = input('name3')
lista = (name, name2, name3)
sorteio = random(lista)
print('o sorteado foi {}.'.format(sorteio))