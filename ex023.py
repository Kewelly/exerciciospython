#eu fiz assim
'''n1 = input('Dígite um número:')
print('Milhar {}'.format(n1[0]))
print('centena {}.'.format(n1[1]))
print('dezena {}'.format(n1[2]))
print('unidade{}'.format(n1[3]))'''

#correção
numero = int(input('Dígite um número:'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Unidade {}\nDezena {}\nCentena {}\nMilhar {}'.format(u, d, c, m))
