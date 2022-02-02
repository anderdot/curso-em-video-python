# Desafio 063: Escreva um programa que leia um número n inteiro qualquer e mostre na
# tela os n primeiros elementos de uma sequência de Fibonacci.
# ex. 0 - 1 - 1 - 2 - 3 - 5 - 8
from cores import cor

n = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
cont = 3

print('{1}{2}{0} → {1}{3}{0}'.format(cor.reset, cor.verde, t1, t2), end = ' → ')
while cont <= n:
    tx = t1 + t2
    print(f'{cor.verde}{tx}{cor.reset}', end = ' → ')
    t1 = t2
    t2 = tx
    cont += 1
print('FIM')
