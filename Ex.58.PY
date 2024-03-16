from random import randint

r = randint(0,10)
palpites = r 
tentativas = 1

n = int(input('tente advihar o número que estou pensando: '))

while not n == palpites:
    
    if n < palpites:
        n = int(input('Um pouco mais: '))
        tentativas += 1

    elif n > palpites:
        n  = int(input('Um pouco menos: '))
        tentativas += 1


print(f'Acertou com {tentativas} tentativas, e o número que estava pensando era {palpites}')

