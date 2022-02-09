# Desafio 086: Crie um programa que crie uma matriz de dimensão 3x3 e preencha com
# valores lidos pelo teclado.
# No final, mostra a matriz na tela, com a formação correta.
from cores import cor

matriz = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]
]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l + 1}][{c + 1}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
