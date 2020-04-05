s = 0
c = 0
for p in range(1, 500, 2):
    if p %3 == 0:
        s += p
        c += 1
print('A soma de todos os {} valores solicitados é {}'.format(c, s))

