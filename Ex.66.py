sum = 0
count = 0
values = 0

while values != 999:
    values = int(input('Digite um valor [999 para parar]: '))
    if values == 999:
        break
    sum += values
    count += 1
print(f'A soma dos {count} valores foi {sum}!') 