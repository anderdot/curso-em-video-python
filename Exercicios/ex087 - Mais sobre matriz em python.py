# Desafio 087: Aprimore o exercicio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
from cores import cor

matriz = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]
]
soma_pares = soma_coluna = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l + 1}][{c + 1}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if c == 2:
            soma_coluna += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            else:
                maior = max(maior, matriz[l][c])
    print()
print(f'A soma de todos os valores pares digitados é {cor.verde}{soma_pares}{cor.reset}.')
print(f'A soma dos valores da terceira coluna é {cor.verde}{soma_coluna}{cor.reset}.')
print(f'O maior valor da segunda linha é {cor.verde}{maior}{cor.reset}.')
