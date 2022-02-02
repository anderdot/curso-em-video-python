# Desafio 056: Desenvolva um programa que leia o nome, idade e o sexo de 4 pessoas.
# No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.
from cores import cor

somaIdade = 0
nomeVelho = 'Nenhum'
idadeVelho = 0
countMulheres = 0
for pessoa in range(0, 4):
    print('{:=^40}'.format(' {}ª pessoa '.format(pessoa + 1)))
    nome = input('Nome: ').strip().title()
    idade = int(input('Idade: '))
    while True:
        sexo = input('Sexo [M/F]: ').strip().upper()
        if sexo == 'M' or sexo == 'F':
            break;
    somaIdade += idade
    if sexo == 'M':
        if idadeVelho == 0:
            nomeVelho = nome
            idadeVelho = idade
        elif idade > idadeVelho:
            nomeVelho = nome
            idadeVelho = idade
    elif sexo == 'F' and idade < 20:
        countMulheres += 1
print('{:=^40}'.format(' Resultado '))
print(f'A média de idade do grupo é de {cor.verde}{somaIdade / 4}{cor.reset} anos.'.format())
print('O homem mais velho do grupo é o {1}{2}{0} com {1}{3}{0} anos.'.format(
    cor.reset,
    cor.verde,
    nomeVelho,
    idadeVelho
))
print(f'No grupo há {cor.verde}{countMulheres}{cor.reset} mulheres com menos de 20 anos.')
