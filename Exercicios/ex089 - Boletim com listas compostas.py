# Desafio 089: Crie um programa que leia nome e duas notas de vários alunos 
# e guarde tudo em uma lista composta. No final, mostre um boletim contendo 
# a média de cada um e permita que o usuário possa mostrar as notas de cada 
# aluno individualmente.
from cores import cor

ficha = []
while True:
    nome = input('Digite o nome do aluno: ')
    n1 = float(input('Digite a 1º nota do aluno: '))
    n2 = float(input('Digite a 2º nota do aluno: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    while True:
        escolha = input('Deseja cadastrar mais um aluno? [S/N]: ').strip().upper()[0]
        if escolha in 'SN':
            break
    if escolha == 'N':
        break
print(f'{" Boletim dos alunos ":-^40}')
print(f' {"Nº":<4}| {"NOME":<24}|{"MÉDIA":>7} ')
print('-' * 40)
v = f'{cor.verde}' # Deixa eu aprender função...
r = f'{cor.reset}'
for i, a in enumerate(ficha):
    print(f' {v}{i+1:<4}{r}| {v}{a[0].capitalize():<24}{r}|{v}{a[2]:>7}{r} ')

while True:
    print('-' * 40)
    aluno = int(input('Mostrar nota de qual aluno? [0 - Sair]: '))
    if aluno == 0:
        break
    if aluno <= len(ficha):
        aluno -= 1
        print(f'As notas de {v}{ficha[aluno][0]}{r} são {v}{ficha[aluno][1]}{r}')

