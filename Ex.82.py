pares = []
impares = []

while True:
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    continuar = str(input("Deseja continuar digitando? [S/N]")) .upper() .strip()[0]
    if continuar != "S":
        break
lista_concatenada = pares + impares
print(f"Lista: {lista_concatenada}")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")