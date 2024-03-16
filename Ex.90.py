dicionario = {}
dicionario["nome"] = str(input("Nome: "))
dicionario["media"] = float(input(f"Média do(a) {dicionario['nome']}: "))

if dicionario["media"] <= 3:
    dicionario["Situação"] = "Reprovado"
elif dicionario["media"] <= 5:
    dicionario["Situação"] = "Recuperação"
elif dicionario["media"]>= 7:
    dicionario["Situação"] = "Aprovado"

print("-="*30)

for k, v in dicionario.items():
    print(f"{k} é igual a {v}")