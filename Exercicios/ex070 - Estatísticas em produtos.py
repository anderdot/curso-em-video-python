# Desafio 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$ 1000 reais.
# C) Qual o nome do produto mais barato.
from cores import cor

i = 1
total = mais1000 = nomeBarato = precoBarato = 0
while True:
    p = ' ' + str(i) + 'º produto '
    print(f'{p:~^40}')
    nome = input('Digite o nome do produto: ').strip()
    while True:
        preco = float(input('Digite o preço do produto: R$ '))
        if preco >= 0:
            break
    
    total += preco
    if preco > 1000:
        mais1000 += 1
    
    if i == 0 or min(precoBarato, preco) == preco:
        nomeBarato = nome
        precoBarato = preco
    while True:
        escolha = input('Deseja continuar cadastrando? [S/N]: ').strip().upper()[0]
        if escolha in 'SN':
            break
    if escolha == 'N':
        break
p = ' Nota Fiscal '
print(f'{p:~^40}')
print(f'O total da compra foi de R$ {cor.verde}{total:,.2f}{cor.reset} reais.')
print(f'Comprado(s) {cor.verde}{mais1000}{cor.reset} produto(s) que custa mais de R$ 1,000,00 reais.')
print(f'O produto mais barato foi {cor.verde}{nomeBarato}{cor.reset}, custando R$ {cor.verde}{precoBarato:,.2f}{cor.reset}.')
