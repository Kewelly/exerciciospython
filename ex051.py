pt = int(input('Escreva o primeiro termo da P.A: '))
r = int(input('Escreva a razão da P.A: '))
decimo = pt + (10 - 1) * r
for i in range(pt, decimo+r, r):
    print(i, end= '-')
print('FIM')
# for i in range(pt, pt + r * 10, r):
#    print(i)
