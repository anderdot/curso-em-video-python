# Desafio 023: Leia um número e mostre na tela os digitos separados
from cores import cor

numero = int(input('Digite um número: '))
print('Unidade: {}{}{}'.format(cor.verde, numero % 10, cor.reset))
print('Dezena:  {}{}{}'.format(cor.verde, numero // 10 % 10, cor.reset))
print('Centena: {}{}{}'.format(cor.verde, numero // 100 % 10, cor.reset))
print('Milhar:  {}{}{}'.format(cor.verde, numero // 1000 % 10, cor.reset))
