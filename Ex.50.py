soma = 0
cont = 0
for c in range(1,7):
    num = int(input("Digite o {} valor: ".format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print("Você me informou {} números e as soma dos números pares é {}".format(cont, soma))