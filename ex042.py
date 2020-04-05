r1 = float(input('escreva um valor'))
r2 = float(input('escreva um valor'))
r3 = float(input('escreva um valor'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas formam um triângulo,')
    if r1 == r2 and r1 == r3:
        print('\033[34mEquilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('\033[34mIsóscelos')
    else:
        print('\033[34mEscaleno')
else:
    print('As retas não formam um triângulo!')
