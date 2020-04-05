n1 = float(input('Escreva sua primeira nota: '))
n2 = float(input('Escreva sua segunda nota: '))
med = (n1 + n2) / 2
print('Sua média foi {:.1f},'.format(med), end='')
if med < 5.0:
    print('você foi \033[31mREPROVADO!!\033[m')
elif 7 > med >= 5:
    print('você está de \033[31mRECUPERAÇÃO!!\033[31m')
else:
    print('você foi aprovado \033[34mAPROVADO!!\033[m')
