from time import sleep
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
opcao = 0 

while opcao != 5:
    print('''          [1] Somar
          [2] Multiplicar
          [3] Maior número
          [4] Inserir novos números
          [5] Fechar o programa''')
    opcao = int(input('Escolha sua opção: '))
    
    if opcao == 1:
        soma = v1+v2
        print(f'A soma dos números {v1} e {v2} é {soma}')
    
    elif opcao == 2:
        multiplicar = v1 * v2
        print(f'A multiplicação entre os números {v1} e {v2} é {multiplicar}')
    
    elif opcao == 3:
        if v1 > v2:
            print(f'O maior número entre {v1} e {v2} é o {v1}')
        elif v2 > v1:
            print(f'O maior número entre {v1} e {v2} é o {v2}')
        else:
            print('Os números são iguais. Tente novamente com outros números')
    
    elif opcao == 4:
        print('Digite novos números')
        v1 = int(input('Digite o primeiro número: '))
        v2 = int(input('Digite segundo número: '))    

    elif opcao == 5:
        print('Finalizando')

    else:
        print('Opção inválida. Digite Novamente')
    sleep(2)
print('Fim do programa')    