def ficha(jog='<Desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols no campeonato.')


#Programa principal
jogador = str(input("Nome do Jogador: "))
gols = str(input("Número de gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    ficha(gol = gols)
else:
    ficha(jogador, gols)