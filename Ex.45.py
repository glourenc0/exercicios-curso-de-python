from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print(''' Suas Opções
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é sua jogada?'))

if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
         print('Você ganhou!')
    elif jogador == 2:
         print('Tente novamente')
elif computador == 1:
    if jogador == 0:
          print('Tente novamente')
    elif jogador == 1:
         print('Empate')
    elif jogador == 2:
         print('Você ganhou!')
elif computador == 2:
    if jogador == 0:
        print('Você ganhou!')
    elif jogador == 1:
        print('Tente novamente')
    elif jogador ==2:
        print('Empate')
else:
    print('Erro tente novamente')
