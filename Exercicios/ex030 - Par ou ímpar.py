# Desafio 030: Digitado um número aparecer na tela se ele é par ou impar.
from cores import cor

numero = float(input('Digite um número: '))
print('O número é {}{}{}.'.format(
    cor.verde, 
    'par' if numero % 2 == 0 else 'ímpar', 
    cor.reset))
