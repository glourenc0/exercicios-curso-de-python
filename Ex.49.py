result = 0

i = int(input('Digite a tabuada que deseja: '))

for c in range (1, 11):
    result = i * c 
    print(f'{i} x {c} = {result}')