# Desafio 073: Crie uma tupla preenchida com os 20 primeiros colocados da tabela
# do campeonato brasileiro de futebol, na ordem de colocação, depois mostre:
# A) Os 5 primeiros.
# B) Os 4 últimos colocados.
# C) Times em ordem alfabética
# D) Em que posição esta o time da ~chapecoense~ -> vascão
from cores import cor

times = (
    'América-MG',
    'Atlético',
    'Atlético-GO',
    'Atlético-MG',
    'Avaí',
    'Botafogo',
    'Bragantino',
    'Ceará',
    'Corinthians',
    'Coritiba',
    'Cuiabá',
    'Flamengo',
    'Fluminense',
    'Fortaleza',
    'Vasco',
    'Juventude',
    'Internacional',
    'Palmeiras',
    'Santos',
    'São Paulo')

print(f'{cor.verde}{" Os cinco primeiros colocados ":~^60}{cor.reset}')
print(times[:5])
print(f'{cor.verde}{" Os quatro últimos colocados ":~^60}{cor.reset}')
print(times[-4:])
print(f'{cor.verde}{" Times em ordem alfabética ":~^60}{cor.reset}')
print(sorted(times))
print(f'{cor.verde}{" Em que posição ta o Vascão ":~^60}{cor.reset}')
print(f'{times.index("Vasco") + 1}ª posição')
