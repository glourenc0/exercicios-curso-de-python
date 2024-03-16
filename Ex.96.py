def area(largura, comprimento):
    a = largura * comprimento
    print(f"A área de um terreno {largura}x{comprimento} é {a} metros quadrados")


#Programa principal
print(f"{'Controle de Terrenos':>40}")
print("-="*30)
largura = float(input("Largura (M): "))
comprimento = float(input("Comprimento (M): "))
area(largura, comprimento)
