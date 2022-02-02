# Desafio 068: faça um programa que jogue par ou impar com o computador. O jogo
# só será interrompido quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.
from cores import cor
from random import randint

vitoria = 0
while True:
    print('~' * 45)
    while True:
        escolha = input('Você quer par ou ímpar? [P/I]: ').strip().upper()[0]
        if escolha in 'PI':
            break
        
    while True:
        jogador = int(input('Qual número? [0-10]: '))
        if jogador >= 0 and jogador <= 10:
            break
    
    print()
    computador = randint(0, 10)
    print('Você escolheu {1}{2}{0} e jogou {1}{3}{0}.'.format(
        cor.reset,
        cor.verde,
        'par' if escolha == 'P' else 'ímpar',
        jogador
    ))
    print('Restou {1}{2}{0} para o computador, que jogou {1}{3}{0}.'.format(
        cor.reset,
        cor.verde,
        'par' if escolha != 'P' else 'ímpar',
        computador
    ))
    
    print('A soma foi de {1}{2}{0}, um número {1}{3}{0}.'.format(
        cor.reset,
        cor.verde, 
        jogador + computador,
        'par' if (jogador + computador) % 2 == 0 else 'ímpar'))
    
    resultado = 'perdeu'
    if escolha == 'P':
        if (jogador + computador) % 2 == 0:
            resultado = 'ganhou'
    else:
        if (jogador + computador) % 2 != 0:
            resultado = 'ganhou'
            
    print('Portanto... você {1}{2}{0}.'.format(
        cor.reset,
        cor.verde if resultado == 'ganhou' else cor.vermelho,
        resultado
    ))
    if resultado == 'ganhou':
        vitoria += 1
    else:
        break
print(f'Você teve {vitoria} vitória(s) consecutiva(s).')
