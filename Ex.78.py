maior = 0
menor = 0 
valor = []
for c in range (0,5):
    valor.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        menor = maior = valor[c]
    else:
        if valor[c] > maior:
            maior = valor[c]
        if valor[c] < menor:
            menor = valor[c] 
    

print('-='*20)
print(f'Você digitou os valores {valor}')
print(f'O maior valor digitado foi {maior} na(s) posição(ões) ', end='')
for  i, v in enumerate(valor):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} na(s) posição(ões) ', end='')
for i, v in enumerate(valor):
    if v == menor:
        print(f'{i}...', end='')
print()
