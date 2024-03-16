from random import randint

def sorteia(lista):
    for v in range(0, 5):
        valor = randint(1, 10)
        numeros.append(valor)
    print(f"Sorteando 5 valores da Lista: {numeros}")


def somaPar(lista):
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f"Somando os valores pares de {numeros}, temos {soma}")
    print()


# Programa principal 
numeros = []
sorteia(numeros)
somaPar(numeros)