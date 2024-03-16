t = ('Botafogo', 'Palmeiras', 'Bragantino', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Athletico-PR',
     'Fluminense', 'Fortaleza', 'São Paulo', 'Internacional', 'Cuiabá', 'Corinthians', 'Santos',
     'Bahia', 'Vasco da Gama', 'Cruzeiro', 'Goiás', 'Coritiba', 'América-MG')
print(f'Lista de times: {t}')
print('-=' *30)
print(f'Os 5 primeiros times do Brasileirão são: {t[0:5]}')
print('-=' *30)
print(f'Os 4 últimos colocados são: {t[-4:]}')
print('-=' *30)
print(f'Times em ordem alfabética {sorted(t)}')
print('-=' *30)
print(f'O São Paulo está na posição {t.index("São Paulo")+1}')