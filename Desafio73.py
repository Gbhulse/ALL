tab = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco')

print(f'Lista de time do Brasileirão {tab}')
print(f'Os 5 primeiros são {tab[0:5]}')
print(f'Os 4 últimos são {tab[-4:]}')
print(f'Times em ordem alfabética {sorted(tab)}')
print(f'A posição da BAHIA é {tab.index("Bahia")+1}')