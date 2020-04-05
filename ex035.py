r1 = float(input('escreva um valor'))
r2 = float(input('escreva um valor'))
r3 = float(input('escreva um valor'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas formam um triângulo!')
else:
    print('As retas não formam um triângulo!')