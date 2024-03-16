def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor
    

#Programa princpal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')




#Outra Solução
def leiaint(num):
    valor = input(num)
    while valor.isnumeric() == False:
        print("Erro! Digite um número.")
        valor = input(num)
    print(f"Você digitou o número {valor}")
    

n = leiaint("Digite um número: ")