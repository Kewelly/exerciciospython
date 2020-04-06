from datetime import date
maior = 0
menor = 0
data = date.today().year
for pessoa in range(1, 8):
    nas = int(input(f'Dígite o ano de nascimento da {pessoa}° pessoa: '))
    idade = data - nas
    if idade < 18:
        menor += 1
    elif idade >= 18:
        maior += 1
print(f'{menor} são menores de idade,')
print(f'{maior} são maiores de idade')
