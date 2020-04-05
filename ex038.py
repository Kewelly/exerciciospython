n1 = int(input('Escreva um número: '))
n2 = int(input('Esreva outro número: '))
if n1 > n2:
    print('O número \033[4m{}\033[m é maior que número \033[4m{}\033[m!!'.format(n1, n2))
elif n2 > n1:
    print('O número \033[4m{}\033[m é maior que o número \033[4m{}\033[m!!'.format(n2, n1))
else:
    print('Os valores são iguais!!')
