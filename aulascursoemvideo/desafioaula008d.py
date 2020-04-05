import random
name = input('nome1:')
name2 = input('name2')
name3 = input('name3')
name4 = input('name4')
lista = (name, name2, name3, name4)
sorteio = random.choice(lista)
print('o sorteado foi {}.'.format(sorteio))
