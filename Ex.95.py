time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str(input("Qual o nome do jogador? "))
    total = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    partidas.clear()

    for p in range (0, total):
        partidas.append(int(input(f"Quantas gols na partida {p+1}? ")))
    jogador['gols'] = partidas [:]
    jogador['total']  = sum(partidas)
    time.append(jogador.copy())
    while True:
        continuar = str(input("Quer continuar [S/N] ")).upper().strip()[0]
        if continuar in 'SN':
            break
        print("Erro! Digite a resposta correta.")
    if continuar == "N":
        break
print("-=" *30)
print("cod ", end="")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
print("-"*40)
for k, v in enumerate(time):
    print(f"{k:>3} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("-"*40)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar)"))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"Erro! Não existe jogador com código {busca}")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}: ")
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i} fez {g} gols.')
    print('-'*40)
print("Volte Sempre")