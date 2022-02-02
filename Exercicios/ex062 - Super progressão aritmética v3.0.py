# Desafio 062: Refaça o Desafio 061, perguntando para o usuário se ele quer mostrar mais
# alguns termos. O programa encerra quando ele disser que quer ver 0 termos.
from ast import While
from cores import cor

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{cor.verde}{termo}{cor.reset}', end = ' → ')
        termo += razao
        cont += 1
    print('PAUSE')
    mais = int(input('Deseja ver mais quantos termos: '))
print('FIM')
print(f'Foram exibidos {cor.verde}{total}{cor.reset} termos.')
