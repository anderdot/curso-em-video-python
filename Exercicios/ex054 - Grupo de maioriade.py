# Desafio 054: Crie um programa que leia o ano de nascimento de sete pessoa.
# No final, mostre quantas pessoa não atingiram a maioriade e quantas ja são de maiores.
from cores import cor
from datetime import date

atual = date.today().year
maior = 0
for i in range(0, 7):
    ano = int(input(f'Digite o ano de nascimento da {i + 1}º pessoa: '))
    if atual - ano >= 21:
        maior += 1
print('No total tivemos {1}{2}{0} maiores de idade e {1}{3}{0} menores de idade.'.format(
    cor.reset,
    cor.verde,
    maior,
    7 - maior
))
