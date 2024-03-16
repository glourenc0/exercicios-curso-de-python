caracter = []
expressao = str(input("Digite uma expressão matemática: "))

for parentese in expressao:
    if parentese == "(":
        caracter.append("(")
    elif parentese == ")":
        if len(caracter)>0:
            caracter.pop()
        else:
            caracter.append(")")
            break

if len(caracter)==0:
    print("Sua expressão está válida")
else:
    print("Sua expressão está inválida")

