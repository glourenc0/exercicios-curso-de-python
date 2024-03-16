lista = []
continuar = "S"
n = lista.append(int(input("Digite um valor: ")))
continuar = str(input("Deseja continuar digitando? ")) .upper().strip()[0]

while continuar == "S":
       n = lista.append(int(input("Digite outro valor: ")))
       continuar = str(input("Deseja continuar digitando? ")) .upper().strip()[0]
lista.sort(reverse=True)
print("-="*30)
print(f"{len(lista)} números digitados ")
print(lista)
if 5 in lista:
    print("O valor 5 foi digitado")
else:
    print("O valor 5 não foi digitado")
