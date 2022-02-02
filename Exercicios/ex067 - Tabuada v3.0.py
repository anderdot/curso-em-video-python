# Desafio 067: Faça um programa que mostre a tabuada de vários números, um de 
# cada vez, para cada valor digitado pelo usuário. O programa será interrompido
# quando o número solicitado for negativo.
from cores import cor

while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    print('~' * 15)
    for i in range(1, 11):
        print(f'{num} x {i:2} = {cor.verde}{num * i}{cor.reset}')
    print('~' * 15)
