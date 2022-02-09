# Desafio 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários 
# em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
from cores import cor

pessoas = []
pessoa = {}
soma = 0

while True:
    pessoa['nome'] = input('Digite um nome: ')
    while True:
        pessoa['sexo'] = input('Qual sexo? [M/F]: ').strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
    pessoa['idade'] = int(input('Digite sua idade: '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())
    pessoa.clear()
    while True:
        escolha = input('Deseja cadastrar mais um? [S/N]: ').strip().upper()[0]
        if escolha in 'SN':
            break
    if escolha == 'N':
        break
print(f'{" Conclusão ":-^40}')
print(f'Foram cadastradas {cor.verde}{len(pessoas)}{cor.reset} pessoas.')
media = soma / len(pessoas)
print(f'A média de idades é de {cor.verde}{media:.2f}{cor.reset} anos.')
print('As mulheres cadastradas são ', end=f'{cor.verde}')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{cor.verde}{p["nome"]}', end=f'{cor.reset}, ')
print()
print('As pessoas com a idade acima da média são:')
for p in pessoas:
    if p['idade'] >= media:
        print(f' - {cor.verde}{p["nome"]}{cor.reset} com {cor.verde}{p["idade"]}{cor.reset} anos.')
