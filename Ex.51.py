termo = int(input("Qual é o termo: "))
razao = int(input("Qual é a razão: "))
decimo = termo + (10 - 1) * razao
for i in range (termo, decimo + razao, razao):
    print(i, end= " --> ")
print("Acabou")