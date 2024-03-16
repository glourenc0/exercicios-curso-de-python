from math import factorial
n = int(input('Digite um número para calcular o seu fatorial: '))

'''fatorial = factorial(n)

print(f'O fatorial do número {n} é {fatorial}')'''

c = n 
f = 1 
print (f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c} ', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

