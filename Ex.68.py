from random import randint

ganhou = True
cont = 0

print('-==' * 10)
print('Vamos jogar par ou ímpar')
print('-==' * 10)

while ganhou == True:

    aleatorio = randint(0,10)
    jogador = int(input('Digite um valor: '))
    tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper() [0]
    computador = aleatorio

    resultado = jogador + computador 
    resto = resultado % 2 == 0

    if tipo == 'P' and resto == True:
        print(f'Parabéns você ganhou!!! Você escolheu {jogador} e o computador escolheu {computador}3')
        cont += 1

    elif tipo == 'I' and resto == False:
        print(f'Parabéns você ganhou!!! Você escolheu {jogador} e o computador escolheu {computador}')
        cont += 1

    else:
        break
print(f'Game Over! Você escolheu {jogador} e o computador escolheu {computador}')

