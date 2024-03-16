contH = contidade = contidadeF = 0

while True:
    print('Cadastre uma pessoa')
    print('-' * 10)
    idade = int(input('Idade: '))
    if idade >= 18:
        contidade +=1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M] ')).strip().upper() [0]
        if sexo == 'M':
            contH += 1
        if sexo == 'F' and idade <= 20:
            contidadeF += 1
            
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper() [0]
    if continuar == 'N':
        break
    print('-' * 10)

print(f'Total de pessoas com mais de 18 anos {contidade}')
print(f'Ao todo temos 1 homem(s) cadastrado(s) {contH}')
print(f'Total de mulheres com menos de 20 anos {contidadeF}')