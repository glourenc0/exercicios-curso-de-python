def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0 
        else:
            return n
            
def leiaFloat(num):
    while True:
        try:
            n = float(input(num))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


#Programa Principal
numero1 = leiaInt("Digite um número Inteiro: ")
numero2 = leiaFloat("Digite um número Float: ")
print(f"O número inteiro digitado foi {numero1} e o número float foi {numero2}")