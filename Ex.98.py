from time import sleep 

def contagem(a, b):
    for n in range(a, b):
        print(f"{n} ", end="", flush = True)
    
    print()
    print("-=" * 30)
    print("Contagem de 10 até 0 de 2 em 2")


def contagem2(a, b, c):
    for i in range(a, b, c):
        print(f"{i} ", end="", flush= True)
        
    print()
    print("-=" * 30)
    print("Agora é sua vez de personalizar a contagem!")

def contagem3(a, b, c):
    for e in range(a, b, c):
        print(f"{e} ", end="", flush = True)
    print()

#Programa Principal
print("-=" * 30)
print("Contagem de 1 até 10 de 1 em 1")
contagem(1, 11)
contagem2(10, -0, -2)
a = int(input("Início: "))
b = int(input("Fim: "))
c = int(input("Passo: " ))
contagem3(a, b, c)