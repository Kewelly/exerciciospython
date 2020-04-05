s = 0
for i in range(0, 6):
    n = int(input('Dígite um número: '))
    if n %2 == 0:
        s = s + n
print('A soma dos números pares é {}'.format(s))
