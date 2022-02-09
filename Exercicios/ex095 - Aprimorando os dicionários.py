# Desafio 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada 
# jogador.
from cores import cor

jogadores = []
jogador = {}
gols = []
while True:
    jogador['nome'] = input('Digite o nome do jogador: ')
    jogador['partidas'] = int(input('Digite a quantidade de partidas jogadas: '))
    for i in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols fez na {i + 1}ª partida: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    gols.clear()
    jogador.clear()
    while True:
        escolha = input('Deseja cadastrar mais um? [S/N]: ').strip().upper()[0]
        if escolha in 'SN':
            break
    if escolha == 'N':
        break
    
print(f'{" Placar de jogadores ":-^60}')
print(f' {"Nº":<4}| {"NOME":<20}| {"GOLS":<23}| {"Total":>5}')
print('-' * 60)
for k, v in enumerate(jogadores):
    print(f' {cor.verde}{k + 1:<3}{cor.reset}', end=' ')
    print(f'| {cor.verde}{v["nome"]:<19}{cor.reset}', end=' ')
    print(f'| {cor.verde}{str(v["gols"]):<22}{cor.reset}', end=' ')
    print(f'| {cor.verde}{v["total"]:>5}{cor.reset}', end=' ')
    print()
print('-' * 60)
while True:
    while True:
        escolha = int(input('Mostrar os dados de que jogador? [0 - Sair]: '))
        if escolha >= 0 and escolha <= len(jogadores):
            break
    if escolha == 0:
        break
    escolha -= 1 # os dados mostrados começam em 1
    titulo = f' Mostrando os dados de {jogadores[escolha]["nome"]} '
    print(f'{titulo:-^60}')
    for i, v in enumerate(jogadores[escolha]['gols']):
        print(f'Na {cor.verde}{i + 1}ª{cor.reset} partida fez {cor.verde}{v}{cor.reset} gols.')
    print(f'Um total de {cor.verde}{jogadores[escolha]["total"]}{cor.reset} gols.')
    print('-' * 60)
