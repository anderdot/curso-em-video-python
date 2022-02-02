# Desafio 041: A confederação nacional de natação precisa de um programa que leia o
# ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 25 anos: Sênior
# Acima: Master
from cores import cor
from datetime import date

atual = date.today().year
anoNascimento = int(input('Digite seu ano de nascimento: '))
idade = atual - anoNascimento
print(f'O Atleta tem {cor.verde}{idade}{cor.reset} anos e se classifica como', end=' ')
if idade <= 9:
    print(f'{cor.verde}mirim{cor.reset}.')
elif idade <= 14:
    print(f'{cor.verde}infantil{cor.reset}.')
elif idade <= 19:
    print(f'{cor.verde}junior{cor.reset}.')
elif idade <= 25:
    print(f'{cor.verde}sênior{cor.reset}.')
else:
    print(f'{cor.verde}master{cor.reset}.')
