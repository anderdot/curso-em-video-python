# Desafio 019: Um professor quer sortear um dos seus quatro alunos para apagar o 
# quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome 
# escolhido.
from cores import cor
from random import choice

nomes = []
for i in range(1, 5):
    nomes.append(input('{}º aluno: '.format(i)))

print('O Escolhido foi o {}{}{}'.format(cor.verde, choice(nomes), cor.reset))

# for nome in nomes:
#     print('{}'.format(nome))