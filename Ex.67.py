value = 0

while value >= 0:
    print('-=='* 10)
    value = int(input('Quer ver a tabuada de qual valor? '))
    print('-=='* 10)
    
    if value < 0:
        break

    for i in range (1,11):
        print(f'{value} x {i} = {value * i}')

print('Fim do Programa')