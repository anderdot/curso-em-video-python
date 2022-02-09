# Desafio 091: Crie um programa onde 4 jogadores joguem um dado e tenham 
# resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou 
# o maior número no dado.
from cores import cor
from random import randint
from operator import itemgetter

jogo = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6),
}

print(f'{" Valores Sorteados ":-^30}')
for k, v in jogo.items():
    print(f'{cor.verde}{k}{cor.reset} tirou {cor.verde}{v}{cor.reset} no dado.')

print(f'{" Ranking ":-^30}')
jogo = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(jogo):
    print(f"{'{1}{2}º{0} lugar: {1}{3}{0} com {1}{4}{0}.':^30}".format(
        cor.reset,
        cor.verde,
        i + 1,
        v[0],
        v[1]
    ))
    