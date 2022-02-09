# Desafio 093: Crie um programa que gerencie o aproveitamento de um jogador 
# de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo 
# isso será guardado em um dicionário, incluindo o total de gols feitos 
# durante o campeonato.
from cores import cor

jogador = {}
gols = []
jogador['nome'] = input('Digite o nome do jogador: ')
jogador['partidas'] = int(input('Digite a quantidade de partidas jogadas: '))
for i in range(0, jogador['partidas']):
    gols.append(int(input(f'Quantos gols fez na {i + 1}ª partida: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print(f'{" Jeito basico ":-^40}')
print(jogador)
print(f'{" Usando for ":-^40}')
for k, v in jogador.items():
    print(f'O campo {cor.verde}{k}{cor.reset} tem o valor {cor.verde}{v}{cor.reset}.')
print(f'{" Detalhes das partidas ":-^40}')
for k, v in enumerate(jogador['gols']):
    print(f'Na {cor.verde}{k + 1}ª{cor.reset} partida marcou {cor.verde}{v}{cor.reset} gol(s).')
print(f'Um total de {cor.verde}{jogador["total"]}{cor.reset} gol(s).')
