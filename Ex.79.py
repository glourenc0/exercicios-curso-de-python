lista = []
lista.append(int(input('Digite um número: ')))
print('Número adicionado com sucesso!')
while True:
    continuar = str(input(f'Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'S':
        valor = int(input('Digite outro número: '))
        if valor in lista:
            print('Número repetido.Não vou adicionar!')
        else:
            lista.append(valor)
            print('Número adicionado com sucesso!')
    else:
        break
print('-='*30)
print(f'Você adicionou o(s) número(s) {sorted(lista)} na lista')