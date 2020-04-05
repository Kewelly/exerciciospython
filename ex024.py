#como eu fiz
'''cidade = input('Escreva o nome de uma cidade:')
n1 = cidade.split()
n2 = ('santo' in n1[0])
print(n2)'''

#coreção
cid = str(input('Dígite uma cidade:')).strip()
print(cid[0:5].upper()== 'SANTO')