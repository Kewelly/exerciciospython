frase = str(input('Escreva uma frase:')).strip()
print('A letra "A" aparece {} vezes'.format(frase.upper().count('A')))
print('A primeira vez que a letra "A" aparece é na posição {}'.format(frase.upper().find('A')+1))
print('A última vez que a letra "A" aparece e na posição {}'.format(frase.upper().rfind('A')+1))

