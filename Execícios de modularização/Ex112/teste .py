from utilidades.moeda import settings
from utilidades.dado import dado

p = dado.leiaDinheiro("Digite o preco: R$")
settings.resumo(p)

