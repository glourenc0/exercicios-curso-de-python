from random import randint
from time import sleep
from operator import itemgetter

dicionario = {"Jogador1": randint(1,6),
              "Jogador2": randint(1,6),
              "Jogador3": randint(1,6),
              "Jogador4": randint(1,6)}
ranking = ()

print("Valores sorteados: ")
for k, v in dicionario.items():
    print(f"{k} tirou {v} no dado")
    sleep(1)

print("-="*30)
print("Ranking:")
ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"{i+1}° lugar: {v[0]} com {v[1]}.")
    sleep(1)
