from Interface.interface import *
from Arquivo.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastras', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar um conteúdo do arquvio
        lerArquivo(arq)
    elif resposta == 2:
        #Opção cadastrar uma nova pessoa
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo Sistema')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[31m')
    sleep(2)