n1 = int(input('digite um número'))
n2 = int(input('digite outro numero'))
s = n1+n2
if s % 2 == 0:
 print('A soma do número {} com o número {} é igual a \033[32m{}'.format(n1,n2, s))
else:
    print('A soma do número {} com o número {} é igual \033[31m{}'.format(n1, n2, s))
