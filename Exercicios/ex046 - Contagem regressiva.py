# Desafio 046: Faça um programa que mostre na tela uma contagem regressiva para o
# estouro de fogos de artificio, indo de 10 a 0, com uma pausa de 1 segundo entre elas.
from cores import cor
from time import sleep
from random import randint

print('Os fogos começam em:')
for i in range(10, 0, -1):
    if i > 3:
        print(i)
    else:
        print(f'{cor.amarelo}{i}{cor.reset}')
    sleep(0.5)
explosao = randint(7, 20)
cores = [cor.anil, cor.amarelo, cor.azul, cor.branco, 
         cor.cinza, cor.roxo, cor.verde, cor.vermelho]
print(f'{cores[randint(0, 7)]}P', end = '')
for i in range(explosao):
    print('{}{}'.format(
        cores[randint(0, 7)],
        'O' if randint(0, 1) == 0 else 'o'    
    ), end = '')
print(f'{cores[randint(0, 7)]}W')
