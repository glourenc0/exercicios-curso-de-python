pessoa = {}
galera = []
soma = media = 0
while True:
    pessoa.clear()

    pessoa['nome'] = str(input("Nome: "))

    while True:
        pessoa['sexo'] = str(input("Sexo: [M/F]")) .upper() .strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print("Erro! Responda apenas Feminino ou Masculino.")

    pessoa['idade']=int(input("Idade: "))
    soma += pessoa['idade']

    galera.append(pessoa.copy())

    while True:
        continuar = str(input("Deseja continuar: [S/N]")) .upper().strip()[0]
        if continuar in 'SN':
            break
        print("Erro! Digite corretamente")
    if continuar == 'N':
        break

print("-="*30)
print(f"A) Ao todo temos {len(galera)} pessoas cadastradas.")
media = soma / len(galera)
print(f"B) A média de idade é de {media:5.2f} anos.")
print(f"C) as mulheres cadastradas foram ", end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f"{p['nome']} ", end="")
print()
print(f"D) Lista das pessoas que estão acima da média: ", end="")
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f"{k} = {v}; ", end='')
        print()
print("<< ENCERRADO >>")
