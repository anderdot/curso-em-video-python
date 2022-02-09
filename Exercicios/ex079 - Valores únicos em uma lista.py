# Desafio 079: Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre em uma lista. Caso o número ja exista lá dentro, ele não será adicionado
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
from cores import cor

numeros = []
while True:
    numero = int(input('Digite um número: '))
    if numero not in numeros:
        numeros.append(numero)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado... não adicionado.')
    while True:
        escolha = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if escolha in 'SN':
            break
    if escolha == 'N':
        break
print('-==-' * 10)
numeros.sort()
print(f'Os números digitados únicos foram: {cor.verde}{numeros}{cor.reset}.')
