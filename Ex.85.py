lista = [[], []]
for c in range(1,8):
    n = int(input(f"Digite o {c}º valor: "))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

lista[0].sort()
lista[1].sort()
print(f"Números pares digitados: {lista[0]}")
print(f"Números impares digitados: {lista[1]}")
