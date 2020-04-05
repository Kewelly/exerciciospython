from random import choices
print('+-+-'*20)
print('Vamos jogar Jokenpô :D')
print('PEDRA, PAPEL, TESOOOURA...')
jogador1 = input()
jogador2 = choices(['pedra', 'papel', 'tesoura'])[0]
print(jogador2)
if (jogador2 == 'pedra' and jogador1 == 'tesoura') or (jogador2 == 'papel' and jogador1 =='pedra') or (jogador2 == 'tesoura' and jogador1 == 'papel' ):
    print('Jogador2 ganhou.')
elif (jogador1 == 'pedra' and jogador2 == 'tesoura') or (jogador1 == 'papel' and jogador2 =='pedra') or (jogador1 == 'tesoura' and jogador2 == 'papel' ):
    print('Jogador1 ganhou.')
elif jogador1 == jogador2:
    print('Empate, Jogue novamente!')
else:
    print('Opção inválida, Tente Novamente')
print('+-+-'*20)