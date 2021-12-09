# Desafio 009: faça um programa que leia um número inteiro e mostre sua tabuada.
from cores import cor

num = int(input('Digite um número: '))
print('-' * 15)
for i in range(1, 11):
    print('{} x {:2} = {}{}{}'.format(num, i, cor.verde, num * i, cor.reset))
print('-' * 15)
