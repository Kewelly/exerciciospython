import random
from time import sleep
n1 = random.randint(0, 5)
adivinhe = int(input('Adivinhe um número entre 0 à 5:'))
print('PROCESSANDO...')
sleep(3)
if n1 == adivinhe:
    print('acertou, o número que pensei foi {}'.format(n1))
else:
    print('errou, o número que pensei foi {}'.format(n1))
