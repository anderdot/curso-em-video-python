# Desafio 002: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem
# de boas-vindas.
from cores import cor

nome = input('Digite seu nome: ')
print('Seja bem-vindo, {}{}{}.'.format(cor.verde, nome, cor.reset))
