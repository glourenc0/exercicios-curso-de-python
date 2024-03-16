print('-'*10)
print('Loja')
print('-'*10)

precoTotal = maisde1000 = menor = 0
cont = 0 
barato = ''

while True:
    nomeProduto = str(input('Nome do produto: '))
    precoProduto = int(input('Preço do produto: '))
    cont +=1 

    if precoProduto >= 1000:
        maisde1000 += 1
    
    if cont == 1 or precoProduto < menor:
        menor = precoProduto
        barato = nomeProduto
    
    precoTotal = precoTotal + precoProduto 
    
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper() [0]
    if continuar == 'N':
        break

print(f'O valor total da compra é de R${precoTotal}') 
print(f'{maisde1000} produtos custam mais de R$1000')  
print(f'O produto mais barato foi a (o) {barato} que custa R${menor}')  