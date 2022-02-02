# Desafio 045: Crie um programa que faça o computador jogar jokenpô com você.
from cores import cor
from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
while True:
    jogador = int(input('Digite sua jogada: ')) - 1
    if 0 <= jogador <= 2:
        break; 
    else:
        print(f'{cor.vermelho}Opção Inválida!{cor.reset}')
print('{:^10}'.format('JO'))
sleep(0.5)
print('{:^15}'.format('KEN'))
sleep(0.5)
print('{:^20}'.format('PÔ'))
sleep(0.5)
print('Você jogou {1}{3}{0} e o computador {2}{4}{0} então'.format(
    cor.reset,
    cor.verde,
    cor.amarelo,
    itens[jogador],
    itens[computador]), 
    end = ' '
)
if computador == jogador:
    print(f'{cor.anil}empatou{cor.reset}!')
elif computador == 0: # Pedra
    if jogador == 1:
        print(f'você {cor.verde}ganhou{cor.reset}!')
    elif jogador == 2:
        print(f'você {cor.vermelho}perdeu{cor.reset}!')
elif computador == 1: # Papel
    if jogador == 0:
        print(f'você {cor.vermelho}perdeu{cor.reset}!')
    elif jogador == 2:
        print(f'você {cor.verde}ganhou{cor.reset}!')
elif computador == 2: # Tesoura
    if jogador == 0:
        print(f'você {cor.verde}ganhou{cor.reset}!')
    elif jogador == 1:
        print(f'você {cor.vermelho}perdeu{cor.reset}!')
