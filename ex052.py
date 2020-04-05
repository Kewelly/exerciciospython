n = int(input('Dígite um número: '))
for i in range(n-1, 1, -1):
    if n%i == 0:
        print('Não é número primo.')
        break
else:
    print('É número primo.')
