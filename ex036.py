cas = float(input('Qual o valor da casa ?'))
sal = float(input('Salário do comprador?'))
ano = int(input('Quantos anos vai demorar para pagar ?'))
mês = ano * 12
val = cas / mês
por = sal * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de {:.2f}'.format(cas, ano, val))
if val < por:
    print('O seu empréstimo foi \033[1;32m aceito \033[m')
else:
    print('Seu empréstimo foi \033[1;31m negado \033[m')
