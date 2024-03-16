soma = 0 
countMulheresMaior20 = 0
maiorIdadeHomem = 0
nomeMaisVelho = ""

for p in range(1, 5):
    print(f"-----{p}º Pessoa-----")
    nome = str(input("Nome: "))#
    idade = int(input("Idade: ").upper())
    sexo = str(input("Sexo [M/F]: ").upper())

    soma += idade
    mediaIdade = soma / 4

    if sexo == "M" and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
        
        
    if sexo == "F" and idade <= 20:
        countMulheresMaior20 += 1


print(f"A média de idade do grupo é de {mediaIdade} anos")
print(f"O homem mais velho tem {maiorIdadeHomem} e se chama {nomeMaisVelho}")
print(f"Ao todo são {countMulheresMaior20} mulher(es) com menos de 20 anos")