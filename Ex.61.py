print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Termo: '))
razao = int(input('Razaõ: '))
termo = primeiro
cont = 1

while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1 
print('Fim')
