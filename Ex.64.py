num = count = sum = 0

num = int(input('Digite um número [Digite 999 para parar] '))
while num != 999:
    sum += num
    count += 1
    num = int(input('Digite um número [Digite 999 para parar] '))
    
print(f'Você digitou {count} números e a soma entre eles é {sum}')
