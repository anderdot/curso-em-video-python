# Desafio 027: Digitado um nome mostre o primeiro e último nome.
from cores import cor

n = input('Digite seu nome completo: ').strip()
nome = n.split()
print('Primeiro nome: {}{}{}'.format(cor.verde, nome[0], cor.reset))
print('Último nome: {}{}{}'.format(cor.verde, nome[len(nome) - 1], cor.reset))
