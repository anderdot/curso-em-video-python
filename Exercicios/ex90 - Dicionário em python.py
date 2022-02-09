# Desafio 090: Faça um programa que leia nome e média de um aluno, guardando 
# também a situação em um dicionário. No final, mostre o conteúdo da estrutura 
# na tela.
from cores import cor

aluno = {}
aluno['nome'] = input('Digite o nome: ')
aluno['media'] = float(input(f'Digite a média do {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print(f'{" Situação ":-^40}')
for k, v in aluno.items():
    print(f' - {cor.verde}{k}{cor.reset} é igual a {cor.verde}{v}{cor.reset}')
