# Desafio 084: Faça um programa que leia o nome e o peso de várias pessoas, guardando
# tudo em uma lista. No final, mostre:
# A) quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves
from cores import cor

temp = []
pessoas = []
while True:
    print(f'{" " + str(len(pessoas) + 1) + "º Pessoa ":-^30}')
    temp.append(input('Digite o nome: '))
    temp.append(float(input('Digite o peso: ')))
    if len(pessoas) == 0:
        menor = maior = temp[1]
    else:
        menor = min(temp[1], menor)
        maior = max(temp[1], maior)
    pessoas.append(temp[:])
    temp.clear()
    while True:
        escolha = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if escolha in 'SN':
            break
    if escolha == 'N':
        break
print(f'Foram cadastradas {cor.verde}{len(pessoas)}{cor.reset} pessoas.')
for p in pessoas:
    if p[1] == menor:
        print(f'{cor.verde}{p[0]}', end=f'{cor.reset}, ')
print(f'são os mais leves, com {cor.verde}{menor}{cor.reset}kg.')
for p in pessoas:
    if p[1] == maior:
        print(f'{cor.verde}{p[0]}', end=f'{cor.reset}, ')
print(f'são os mais pesados, com {cor.verde}{maior}{cor.reset}kg.')
