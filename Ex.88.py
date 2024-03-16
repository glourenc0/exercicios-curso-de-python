from random import randint
from time import sleep
print("--"*20)
print(" "*10, "JOGO DA MEGA SENA",)
print("--"*20)

lista = []

n = int(input("Quantos jogos você quer que eu sorteie? "))
print("-="*5, f"Sorteando {n} jogos", "-="*5)

for c in range(1, n+1):
    
    for x in range (0,6):
        random = randint(1,60)
        lista.append(random)
    print(f"Jogo {c}: {lista}")
    lista.clear()
    sleep(1)