# Desafio 061: Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os dez primeiros termos da progressão usando a estrutura while.
from cores import cor

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{cor.verde}{termo}{cor.reset}', end = ' → ')
    termo += razao
    cont += 1
print('Fim')