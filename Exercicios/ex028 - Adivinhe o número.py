# Desafio 028: O computador deve pensar em um número de 0 a 5 e você tenta adivinhar.
from cores import cor
from random import randint
from time import sleep

pensado = randint(0, 5)
print('-=-' * 15)
print('Você? mero mortal. Ousa me desafiar?')
print('            HA HA HA HA')
print('-=-' * 15)
sleep(1)
numero = int(input('Pode tentar. Digite um número: '))

print('-=-' * 15)
if numero == pensado:
    print('Essa nãããão. Fui derrotado x.x')
else:
    print('É impossivel me vencer! Eu escolhi {}{}{}.'.format(
        cor.verde,
        pensado,
        cor.reset))
print('-=-' * 15)
