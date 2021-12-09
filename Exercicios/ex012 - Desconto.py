# Desafio 012: Faça um programa que leia o preço de um produto e mostre na tela aplicando 
# 5% de desconto
from cores import cor

preco = float(input('Digite o preço do produto: R$ '))
print('O valor com 5% de desconto é R$ {}{:.2f}{} reais.'.format(
    cor.verde,
    preco - preco * 5 / 100,
    cor.reset))
