temp = []
princ = []

while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()

    c = str(input("Quer continuar? [S/N] ")) .upper().strip() [0]
    if c != "S":
        break
print("-=" * 30)
print(f"Foi cadastrado {len(princ)} pessoas.")
print(f"O maior peso é de {maior}Kg. Peso de ", end="")
for p in princ:
    if p[1] == maior:
        print(f"[{p[0]}] ", end="")
print()
print(f"O menor peso é de {menor}Kg. Peso de ", end="")
for p in princ:
    if p[1] == menor:
        print(f"[{p[0]}] ", end="")
print()