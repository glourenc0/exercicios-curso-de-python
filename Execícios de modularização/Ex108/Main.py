import moeda

p = float(input("Digite o preco: R$"))
print(f"A metade de R${moeda.moeda(p)} é R${moeda.moeda(moeda.metade(p))}")
print(f"O dobro de R${moeda.moeda(p)} é R${moeda.moeda(moeda.dobro(p))}")
print(f"Aumentado 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}")
print(f"Diminuindo 10%, temos {moeda.moeda(moeda.diminuir(p, 10))}")