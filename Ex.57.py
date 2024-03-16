sexo = str(input('Digite o seu sexo: [M/F] ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Informe novamente: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado')
    