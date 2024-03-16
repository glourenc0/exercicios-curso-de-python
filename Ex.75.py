n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o última número: ')))

print(f'Você digitou os valores: {n}')
print(f'O número 9 apareceu {n.count(9)}')
if 3 in n:
    print(f'O primeiro valor 3 foi digitado na {n.index(3)+ 1}° posição ')
else:
    print('Não foi digitado o valor 3')
print('Os números pares são: ', end='')

for par in n :
    if par % 2 == 0:
        print(par, end=' ')
