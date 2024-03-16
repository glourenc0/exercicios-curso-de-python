t = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
     'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'quatorze', 'quinze', 'dezesseis', 'dezesste', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entro 0 e 20: '))
    if n > -1 and n < 21:
        break
    print('Tente Novamente. ', end='')
print(f'Você digitou o número {t[n]}')

