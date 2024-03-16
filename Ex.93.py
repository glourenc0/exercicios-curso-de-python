jogador = {}
partidas = []

jogador['nome'] = str(input("Qual o nome do jogador? "))
total = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for p in range (0, total):
    partidas.append(int(input(f"Quantas gols na partida {p}? ")))
jogador['gols'] = partidas [:]
jogador['total']  = sum(partidas)

print("-="*30)
print(jogador)
print("-="*30)

for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("-="*30)

print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.")
for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i}, fez {v} gols.')
print(f"Foi um total de {jogador['total']} gols.")