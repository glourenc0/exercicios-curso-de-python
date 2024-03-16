lista = []

while True:
    nome = str(input("Nome: "))
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2
    lista.append([nome, [n1, n2], media])
    c = str(input("Deseja continuar? [S/N] ")) .upper() .strip()[0]
    if c != 'S':
        break
print("-="*30)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
print("-"*26)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print("-="*35)
    b = int(input("Mostrar notas de qual aluno? (999 Interrompe): "))
    if b == 999:
        print("Finalizando...")
    if b <= len(lista) - 1:
        print(f"Notas de {lista[b][0]} são {lista[b][1]}")    