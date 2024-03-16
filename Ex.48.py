cont = 0
soma = 0

for c in range (1, 501, 2):
    if c % 3 == 0: 
        print(c)
        cont += 1
        soma += c

print(f'A soma dos números múltiplos de 0 a 500 é {soma} foram {cont} valores somados')