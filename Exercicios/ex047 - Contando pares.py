# Desafio 047: Crie um programa que mostre na tela todos os números pares que
# estão no intervalo de 1 a 50.
from cores import cor

for i in range(2, 51, 2):
    print('{:2}'.format(i), end = ' ')
    if i % 10 == 0:
        print()
print(f'Número de iterações: {cor.verde}{int(i / 2)}{cor.reset}.')
