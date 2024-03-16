from datetime import datetime

dados = {}

dados['nome'] = str(input("Nome: "))
nasc = int(input("Ano de nascimento: "))
dados['idade'] = datetime.now().year - nasc
dados['carteiraTrab'] = int(input("Carteira de Trabalho (0 não tem): "))
if dados['carteiraTrab'] != 0:
    dados['anoCont'] = int(input("Ano de contratação: "))
    dados['salario'] = float(input("Salário: R$ "))
    dados['aposentadoria'] = (dados['anoCont'] + 35) - datetime.now().year + dados['idade']
print("-="*30)
for k, v in dados.items():
    print(f" - {k} tem o valor {v}")