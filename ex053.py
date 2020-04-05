frase = str(input('Escreva uma frase: '))
pali = (frase[::-1])
if frase == pali:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo. ')
